#!/usr/bin/env python3

#
# This file is part of LiteICLink.
#
# Copyright (c) 2020-2024 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause

import os
import argparse

from migen import *
from migen.genlib.resetsync import AsyncResetSynchronizer

from litex.gen import *

from litex.build.generic_platform import *

from litex_boards.platforms import lambdaconcept_ecpix5
from litex_boards.targets.lambdaconcept_ecpix5 import _CRG

from litex.soc.integration.soc_core import *
from litex.soc.integration.soc import SoCRegion
from litex.soc.integration.builder import *
from litex.soc.interconnect import wishbone

from liteiclink.serwb.genphy import SERWBPHY
from liteiclink.serwb.core import SERWBCore, SERIOCore

from liteeth.phy.ecp5rgmii import LiteEthPHYRGMII

from litescope import LiteScopeAnalyzer

# IOs ----------------------------------------------------------------------------------------------

serwb_io = [
    ("serwb_master", 0,
        Subsignal("clk", Pins("pmod0:0"), IOStandard("LVCMOS33")),
        Subsignal("tx",  Pins("pmod0:1"), IOStandard("LVCMOS33")),
        Subsignal("rx",  Pins("pmod0:2"), IOStandard("LVCMOS33")),
    ),
]

# SerWBDemoSoC ------------------------------------------------------------------------------------

class SerWBDemoSoC(SoCCore):
    def __init__(self, platform, with_analyzer=False):
        sys_clk_freq = int(25e6)

        # CRG --------------------------------------------------------------------------------------
        self.crg = _CRG(platform, sys_clk_freq)

        # SoCMini ----------------------------------------------------------------------------------
        SoCMini.__init__(self, platform, sys_clk_freq,
            csr_data_width       = 32,
            cpu_type             = "vexriscv",
            integrated_rom_size  = 0x10000,
            integrated_sram_size = 0x10000,
            with_timer           = True,
            ident                = "LiteICLink SerWB demo on ECPIX-5",
            ident_version        = True,
            with_uart            = True,
            uart_name            = "crossover",
        )

        # Etherbone --------------------------------------------------------------------------------
        self.ethphy = LiteEthPHYRGMII(
            clock_pads = self.platform.request("eth_clocks"),
            pads       = self.platform.request("eth"),
            rx_delay   = 0e-9
        )
        self.add_etherbone(phy=self.ethphy)

        # SerWB (Master) ---------------------------------------------------------------------------
        # PHY.
        # ----
        self.serwb_master_phy = SERWBPHY(
            device = platform.device,
            pads   = platform.request("serwb_master"),
            mode   = "master",
        )

        # Core.
        # -----
        self.serwb_master_core = SERWBCore(self.serwb_master_phy, self.clk_freq, mode="slave",
            etherbone_buffer_depth = 1,
            tx_buffer_depth        = 8,
            rx_buffer_depth        = 8,
        )

        # Add SerWB as Slave to SoC.
        # --------------------------
        self.bus.add_slave("serwb", self.serwb_master_core.bus, SoCRegion(origin=0x40000000, size=0x20000000))

        # SerIO ------------------------------------------------------------------------------------

        # SerIO.
        # ------
        self.serio0 = SERIOCore(serwb_core=self.serwb_master_core, port=1)
        self.serio1 = SERIOCore(serwb_core=self.serwb_master_core, port=2)

        # Leds -------------------------------------------------------------------------------------
        leds_pads = []
        for i in range(4):
            rgb_led_pads = platform.request("rgb_led", i)
            self.comb += [getattr(rgb_led_pads, n).eq(1) for n in "gb"] # Disable Green/Blue Leds.
            leds_pads += [getattr(rgb_led_pads, n) for n in "r"]
        self.comb += [
            leds_pads[0].eq(~self.serwb_master_phy.init.ready),
            leds_pads[1].eq(~self.serwb_master_phy.init.error),
            leds_pads[2].eq(self.serio0.o[1]), # Counter from Slave through SerIO.
            leds_pads[3].eq(self.serio1.o[1]), # Counter from Slave through SerIO.
        ]

        # Analyzer ---------------------------------------------------------------------------------
        if with_analyzer:
            analyzer_signals = [
                self.serwb_master_phy.init.fsm,
                self.serwb_master_phy.serdes.rx.data,
                self.serwb_master_phy.serdes.rx.comma,
                self.serwb_master_phy.serdes.rx.idle,
                self.serwb_master_phy.serdes.tx.data,
                self.serwb_master_phy.serdes.tx.comma,
                self.serwb_master_phy.serdes.tx.idle,
            ]
            self.analyzer = LiteScopeAnalyzer(analyzer_signals, 256, csr_csv="analyzer.csv")

# Build --------------------------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="LiteICLink SerWB demo on ECPIX5")
    parser.add_argument("--build",         action="store_true", help="Build bitstream")
    parser.add_argument("--load",          action="store_true", help="Load bitstream (to SRAM)")
    parser.add_argument("--with-analyzer", action="store_true", help="Add LiteScope Analyzer")
    args = parser.parse_args()

    platform = lambdaconcept_ecpix5.Platform(toolchain="trellis")
    platform.add_extension(serwb_io)
    soc     = SerWBDemoSoC(platform, with_analyzer=args.with_analyzer)
    builder = Builder(soc, csr_csv="csr.csv")
    builder.add_json("icebreaker_soc.json", 0x40000000, "icebreaker_soc")
    builder.build(run=args.build)

    if args.load:
        prog = soc.platform.create_programmer()
        prog.load_bitstream(os.path.join(builder.gateware_dir, soc.build_name + ".bit"))


if __name__ == "__main__":
    main()
