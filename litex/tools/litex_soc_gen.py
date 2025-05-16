#!/usr/bin/env python3

#
# This file is part of LiteX.
#
# Copyright (c) 2022 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause

"""
LiteX standalone SoC generator.

这个生成器将LiteX的范围缩小到CPU/外设的选择和集成，以及创建具有MMAP/流式DMA接口的SoC，
这些SoC可以重新集成到外部设计(或LiteX SoC)中。
可以将其视为一个迷你版的Nios SOPC Builder/ Zynq或Microblaze子系统生成器，
它提供了重用LiteX支持的任何CPU的可能性 :)
"""

import argparse

from migen import *

from litex.build.generic_platform import *

from litex.soc.integration.soc_core import *
from litex.soc.integration.soc import SoCRegion
from litex.soc.integration.builder import *
from litex.soc.interconnect import wishbone
from litex.soc.interconnect import axi

# IOs/Interfaces -----------------------------------------------------------------------------------

def get_common_ios():
    """获取通用IO接口定义
    
    返回:
        list: 包含时钟和复位信号的IO定义列表
    """
    return [
        # 时钟/复位信号
        ("clk", 0, Pins(1)),  # 时钟信号
        ("rst", 0, Pins(1)),  # 复位信号
    ]

def get_uart_ios():
    """获取UART接口定义
    
    返回:
        list: 包含UART TX和RX信号的IO定义列表
    """
    return [
        # 串口信号
        ("uart", 0,
            Subsignal("tx",  Pins(1)),  # 发送信号
            Subsignal("rx", Pins(1)),   # 接收信号
        )
    ]

def get_debug_ios(debug_width=8):
    """获取调试接口定义
    
    参数:
        debug_width (int): 调试信号宽度
        
    返回:
        list: 包含调试信号的IO定义列表
    """
    return [
        ("debug", 0, Pins(debug_width)),  # 调试信号
    ]

# Platform -----------------------------------------------------------------------------------------

class Platform(GenericPlatform):
    """平台类
    
    用于生成Verilog代码的平台类
    """
    def build(self, fragment, build_dir, build_name, **kwargs):
        """构建方法
        
        参数:
            fragment: 要构建的模块
            build_dir: 构建目录
            build_name: 构建名称
            **kwargs: 其他参数
        """
        os.makedirs(build_dir, exist_ok=True)  # 创建构建目录
        os.chdir(build_dir)  # 切换到构建目录
        conv_output = self.get_verilog(fragment, name=build_name)  # 获取Verilog输出
        conv_output.write(f"{build_name}.v")  # 写入Verilog文件

# LiteX SoC Generator ------------------------------------------------------------------------------

class LiteXSoCGenerator(SoCMini):
    """
    
    用于生成独立SoC的类，继承自SoCMini
    """
    def __init__(self, name="litex_soc", sys_clk_freq=int(50e6), **kwargs):
        """初始化SoC生成器
        
        参数:
            name (str): SoC名称
            sys_clk_freq (int): 系统时钟频率
            **kwargs: 其他SoC参数
        """
        # 平台初始化 ---------------------------------------------------------------------------------
        platform = Platform(device="", io=get_common_ios())  # 创建平台实例
        platform.name = name  # 设置平台名称
        platform.add_extension(get_uart_ios())  # 添加UART接口

        # CRG初始化 ----------------------------------------------------------------------------------
        self.submodules.crg = CRG(  # 创建时钟复位生成器
            clk = platform.request("clk"),  # 获取时钟信号
            rst = platform.request("rst"),  # 获取复位信号
        )

        # SoC初始化 ----------------------------------------------------------------------------------
        if kwargs["uart_name"] == "serial":
            kwargs["uart_name"] = "uart"  # 统一UART名称
        SoCCore.__init__(self, platform, clk_freq=sys_clk_freq, 
                        ident=f"LiteX standalone SoC - {name}", **kwargs)  # 初始化SoC核心

        # MMAP从接口 --------------------------------------------------------------------------------
        s_bus = {  # 选择总线类型
            "wishbone" : wishbone.Interface(),  # Wishbone总线
            "axi-lite" : axi.AXILiteInterface(),  # AXI-Lite总线
        }[kwargs["bus_standard"]]
        self.bus.add_master(name="mmap_s", master=s_bus)  # 添加主设备
        platform.add_extension(s_bus.get_ios("mmap_s"))  # 添加总线IO
        wb_pads = platform.request("mmap_s")  # 获取总线引脚
        self.comb += s_bus.connect_to_pads(wb_pads, mode="slave")  # 连接总线引脚

        # MMAP主接口 --------------------------------------------------------------------------------
        m_bus = {  # 选择总线类型
            "wishbone" : wishbone.Interface(),  # Wishbone总线
            "axi-lite" : axi.AXILiteInterface(),  # AXI-Lite总线
        }[kwargs["bus_standard"]]
        wb_region = SoCRegion(origin=0xa000_0000, size=0x1000_0000, cached=False)  # 创建总线区域
        self.bus.add_slave(name="mmap_m", slave=m_bus, region=wb_region)  # 添加从设备
        platform.add_extension(m_bus.get_ios("mmap_m"))  # 添加总线IO
        wb_pads = platform.request("mmap_m")  # 获取总线引脚
        self.comb += m_bus.connect_to_pads(wb_pads, mode="master")  # 连接总线引脚

        # 调试接口 ----------------------------------------------------------------------------------
        platform.add_extension(get_debug_ios())  # 添加调试接口
        debug_pads = platform.request("debug")  # 获取调试引脚
        self.comb += [
            # 导出调试信号
            debug_pads[0].eq(0),  # 信号0
            debug_pads[1].eq(1),  # 信号1
            # 等等...
        ]

# Build --------------------------------------------------------------------------------------------
def main():
    """主函数
    
    解析命令行参数并生成SoC
    """
    # 参数解析
    from litex.soc.integration.soc import LiteXSoCArgumentParser
    parser = LiteXSoCArgumentParser(description="LiteX standalone SoC generator")
    target_group = parser.add_argument_group(title="Generator options")
    target_group.add_argument("--name",          default="litex_soc", help="SoC名称")
    target_group.add_argument("--build",         action="store_true", help="构建SoC")
    target_group.add_argument("--sys-clk-freq",  default=int(50e6),   help="系统时钟频率")
    builder_args(parser)  # 添加构建器参数
    soc_core_args(parser)  # 添加SoC核心参数
    args = parser.parse_args()  # 解析参数

    # 创建SoC实例
    soc = LiteXSoCGenerator(
        name         = args.name,  # SoC名称
        sys_clk_freq = int(float(args.sys_clk_freq)),  # 系统时钟频率
        **soc_core_argdict(args)  # SoC核心参数
    )

    # 构建SoC
    builder = Builder(soc, **builder_argdict(args))  # 创建构建器
    builder.build(build_name=args.name, run=args.build)  # 构建SoC

if __name__ == "__main__":
    main()  # 运行主函数
