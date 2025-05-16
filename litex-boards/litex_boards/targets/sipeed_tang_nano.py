#!/usr/bin/env python3

#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2021 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause

# Build/Use
# ---------
# 1) Update CH552 firmware: https://qiita.com/ciniml/items/05ac7fd2515ceed3f88d
# 2) Build/Load design: ./sipeed_tang_nano.py --csr-csv=csr.csv --build --load
# 3) Patch litex_server (CH552 firmware seems to require receiving a few bytes before
# operating correctly...):
#diff --git a/litex/tools/remote/comm_uart.py b/litex/tools/remote/comm_uart.py
#index bb124fb3..d5a075fd 100644
#--- a/litex/tools/remote/comm_uart.py
#+++ b/litex/tools/remote/comm_uart.py
#@@ -29,6 +29,8 @@ class CommUART(CSRBuilder):
#         if hasattr(self, "port"):
#             return
#         self.port.open()
#+        for i in range(256):
#+            self.port.write(0)
#
#     def close(self):
#         if not hasattr(self, "port"):
# 4) Start litex_server at 1MBps (CH552 does not seem to work at traditional baudrates...):
# litex_server --uart --uart-port=/dev/ttyUSBX --uart-baudrate=1000000
# 5) Test UARTBone ex: litex_cli --regs

from migen import *

from litex.gen import *

from litex_boards.platforms import sipeed_tang_nano

from litex.soc.cores.clock.gowin_gw1n import  GW1NPLL
from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *
from litex.soc.cores.led import LedChaser

# CRG ----------------------------------------------------------------------------------------------

class _CRG(LiteXModule):
    def __init__(self, platform, sys_clk_freq):
        self.rst    = Signal()
        self.cd_sys = ClockDomain()

        # # #

        # Clk / Rst.
        clk24 = platform.request("clk24")
        rst_n = platform.request("user_btn", 0)

        # PLL.
        self.pll = pll = GW1NPLL(devicename=platform.devicename, device=platform.device)
        self.comb += pll.reset.eq(~rst_n)
        pll.register_clkin(clk24, 24e6)
        pll.create_clkout(self.cd_sys, sys_clk_freq)

# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCMini):
    def __init__(self, toolchain="gowin", sys_clk_freq=48e6, with_led_chaser=True, **kwargs):
        platform = sipeed_tang_nano.Platform(toolchain=toolchain)

        # CRG --------------------------------------------------------------------------------------
        self.crg = _CRG(platform, sys_clk_freq)

        # SoCMini ----------------------------------------------------------------------------------
        kwargs["uart_name"]     = "crossover"
        kwargs["uart_baudrate"] = 1e6 # CH552 firmware does not support traditional baudrates.
        kwargs["with_uartbone"] = True
        SoCMini.__init__(self, platform, sys_clk_freq, ident="LiteX SoC on Tang Nano", **kwargs)

        # Leds -------------------------------------------------------------------------------------
        if with_led_chaser:
            self.leds = LedChaser(
                pads         = platform.request_all("user_led"),
                sys_clk_freq = sys_clk_freq)

# Build --------------------------------------------------------------------------------------------

def main():
    from litex.build.parser import LiteXArgumentParser
    parser = LiteXArgumentParser(platform=sipeed_tang_nano.Platform, description="LiteX SoC on Tang Nano.")
    parser.add_target_argument("--flash",       action="store_true",      help="Flash Bitstream.")
    parser.add_target_argument("--sys-clk-freq",default=48e6, type=float, help="System clock frequency.")
    args = parser.parse_args()

    soc = BaseSoC(
        toolchain    = args.toolchain,
        sys_clk_freq = args.sys_clk_freq,
        **parser.soc_argdict
    )

    builder = Builder(soc, **parser.builder_argdict)
    if args.build:
        builder.build(**parser.toolchain_argdict)

    if args.load:
        prog = soc.platform.create_programmer()
        prog.load_bitstream(builder.get_bitstream_filename(mode="sram"))

    if args.flash:
        prog = soc.platform.create_programmer()
        prog.flash(0, builder.get_bitstream_filename(mode="flash", ext=".fs")) # FIXME

if __name__ == "__main__":
    main()
