#!/usr/bin/env python3

#
# This file is part of LiteX.
#
# Copyright (c) 2018-2019 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause

import os
import sys
import json

from litex.build import tools

def main():
    # 检查命令行参数是否足够
    if len(sys.argv) < 2:
        print("usage: litex_read_verilog verilog_file [module]")
        exit(1)

    # 获取Verilog文件和模块名
    verilog_file = sys.argv[1]
    json_file = verilog_file + ".json"
    module = None if len(sys.argv) < 3 else sys.argv[2]

    # 使用Yosys将Verilog转换为JSON
    yosys_v2j = "\n".join([
        "read_verilog -sv {}".format(verilog_file),  # 读取Verilog文件
        "proc",  # 处理模块
        "write_json {}.json".format(verilog_file)  # 将结果写入JSON文件
    ])
    tools.write_to_file("yosys_v2j.ys", yosys_v2j)  # 将Yosys脚本写入文件
    os.system("yosys -q yosys_v2j.ys")  # 执行Yosys脚本

    # 加载JSON文件并转换为Migen模块
    f = open(json_file, "r")
    j = json.load(f)

    # 创建模块列表
    modules = [module] if module is not None else j["modules"].keys()

    # 创建Migen定义
    for module in modules:
        migen_def = []
        migen_def.append("class {}(Module):".format(module))  # 定义模块类
        migen_def.append(" "*4 + "def __init__(self):")  # 定义构造函数
        for name, info in j["modules"][module]["ports"].items():
            length = "" if len(info["bits"]) == 1 else len(info["bits"])  # 获取信号长度
            migen_def.append(" " * 8 + "self.{} = Signal({})".format(name, length))  # 定义信号
        migen_def.append("")
        migen_def.append(" "*8 + "# # #")
        migen_def.append("")
        migen_def.append(" "*8 + "self.specials += Instance(\"{}\",".format(module))  # 添加实例
        for name, info in j["modules"][module]["ports"].items():
            io_prefix = {
                "input": "i",  # 输入信号前缀
                "output": "o",  # 输出信号前缀
                "inout": "io"  # 双向信号前缀
            }[info["direction"]]
            migen_def.append(" "*12 + "{}_{}=self.{},".format(io_prefix, name, name))  # 添加端口连接
        migen_def.append(" "*8 + ")")
        migen_def.append("")
        print("\n".join(migen_def))  # 打印Migen定义

    # 清理生成的文件
    os.system("rm yosys_v2j.ys")
    os.system("rm " + json_file)


if __name__ == "__main__":
    main()
