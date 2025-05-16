## Why SoC Copliot?

**Build a 100% Python-based SoC Design environment!** SoC-Copilot seeks for new agile SoC design methodologies, collaboration approaches and creation of reusable IPs and subsystems. 

**Trend #1**: Python-embedded DSLs are increasingly being used to improve the productivity of hardware design and verification.

**Trend #2**: LLMs are increasingly being used to improve the productivity of hardware design and verification.

There has been also an effort to establish principles and practices for agile SoC development by UC Berkeley [1] (2016). Their proposal **Agile Hardware Manifesto** includes the following four principles: 

> **1. Incomplete,fabricable prototypes over fully featured models**
> This principle means iterative, featuredriven development. Each prototype going through full RTL to GDSII toolflow offers accurate feedback on
> power, performance, and area. Thus, one is very near to tapeout readiness, and the number of features is feasible to manage the schedule

> **2. Collaborative, flexible teams over rigid silos**
> Engineers work in collaborative, flexible teams that handle all implementation stages. This is in contrast with the traditional setup with engineers assigned to particular tasks. One key benefit is reduced communication overhead and decreased risks of misunderstandings

> **3. Improvement of tools and generators over the improvement of the instance**
> The human effort is spent on creating a tool that automatically creates the instance. This improves the reusability and reconfigurability of the components and reduces verification costs

> **4. esponse to change over following a plan (Iterative design)**
> The human effort is spent on conducting rapid changes instead of solving problems with rigid plans. There is no doubt that requirements would not change. Agile Hardware Development, however, sees changes as a means to enhance competitiveness

> **5. Predictable schedule and fixed cadence**
> Set a clear pace for each tapeout and fit the IP selection, development, and integration to the planned schedule. This means prioritizing schedule over features like agile software methodologies

## What methods and practices to increase agility of SoC development?
 
> * [Chipyard](https://github.com/ucb-bar/chipyard) is an open source framework for agile development of Chisel-based systems-on-chip. It will allow you to leverage the Chisel HDL, Rocket Chip SoC generator, and other Berkeley projects to produce a RISC-V SoC with everything from MMIO-mapped peripherals to custom accelerators. Chipyard contains processor cores (Rocket, BOOM, cva6), vector units (Saturn, Ara), accelerators (Gemmini, NVDLA), memory systems, and additional peripherals and tooling to help create a full featured SoC.Chipyard supports multiple concurrent flows of agile hardware development, including software RTL simulation, FPGA-accelerated simulation (FireSim), automated VLSI flows (Hammer), and software workload generation for bare-metal and Linux-based systems (FireMarshal).
>
> * [Blackparrot](https://github.com/black-parrot/black-parrot) platform base their fast development iterations on the open source RTL component libraries BaseJump STL and HardFloat. Development is guided by three core principles: **Be Tiny, Be Modular, Be Friendly.**
> 1) **Be Tiny** When choosing among alternatives, we choose the option that results in a smaller, more understandable code base and in less die area, simpler critical paths, and fewer bugs. The result is a code base that is as small and understandable as possible, and hardware that is PPA efficient. We take care to not implement esoteric and performance noncritical components in RTL, and to avoid a common problem in recent **generator-based RTL** methodologies: a multitude of tunable knobs in which most combinations have been untested and yield dubious PPA benefit. If a feature is required by the RISC-V spec but is not performance critical, we implement it through emulation. The code is “all the RTL you need and nothing that you do not.”
> 2) **Be Modular** We employ clean, latency-insensitive interfaces that do not rely on knowledge of the other module’s internals. This allows multiple contributors to work independently of each other, and to minimize bugs that emerge from incomplete understanding of the entire code base.
>
> * [LiteX](https://github.com/enjoy-digital/litex) framework described with [Migen](https://github.com/m-labs/migen), provides a convenient and efficient infrastructure to create FPGA Cores/SoCs. GitHub-hosted SoC builder/IP library and utilities that can be used to create SoCs and full FPGA designs. Besides being open-source and BSD licensed, its originality lies in the fact that its IP components are entirely described using Migen Python internal DSL, which simplifies its 0design in depth. LiteX already supports various softcores CPUs and essential peripherals, with no dependencies on proprietary IP blocks or generators. 
>
> * [SoCGen](https://github.com/habibagamal/SoC_Automation) is an SoC design automation tool that takes a simple, schematic-like JSON description of the SoC architecture and generates the final GDS-II without any human intervention.
>  1) The first scenario is enabling end-users who are not experienced in SoC design to easily tape-out chips with the desired system behavior. All the user has to do is describe the system architecture in a simple format, then start the flow.
>  2) The second scenario is experienced SoC designers can review the generated files at each intermediate step of hardening then do the required modifications to address any concerns. In addition, experienced designers can benefit from the flexibility of the tool and the ease of reiterating the design through the flow. 

## Main Goals of SoC Copilot

The main focus of SoC Copilot is on large and complex SoCs in which integration expertise is essential. The main goals are：
1) creation of a versatile SoC template
2) development of agile SoC development design process

The problem for automating the whole process of designing an SoC:
1) Attaining a comprehensive description methodology to represent any potential IP adequately
2) Circumscribing how the connections between the different IPs, buses, and masters are amply described
3) Parsing the representation and generating the proper format and connections of all the Verilog modules that make up the SoC
4) Adhering to an acceptable runtime period to fulfill the purposes of the automation process and render it attractive to designers. Thus, the efficiency of the process is critical, and its maintenance is inevitable to keep the project updated with the most modern technologies
5) Usability and achieving the no-man-in-the-loop goal, while ensuring the accessibility of all the files and generated outputs of the intermediate stages of the process to the designers to discern and reform
6) Avoiding huge compromises in the quality of the work produced, if compared with a fully manual design process. Hence, we articulate our project’s objectives as versatility, usability, extensibility, reliability, competence,and efficiency

## SoC Copilot：Reuse，Modularize，Automate

> **Reuse：** Extensible and parameterizable designs
> * System Verilog
> * Python HDL 
> * Chisel Generator
> 
> **Modularize：** Agile design and development
> * Hierarchical design to reduce tool time
> * Optimize designs at the component level
> * Black-box designs for use across teams
> * SCRUM-like task management
> * Sprinting to “tape-ins”
> * Establish design interfaces early (RoCC, Basejump)
> * Use latency-insensitive interfaces to remove crossmodule timing dependencies
> * Identify specific deliverables between different teams(esp. analog→digital)
> 
> **Automate**
> * Abstracted implementation and testing flows
> * Develop implementation flow adaptable to arbitrary designs
> * Use validated IP components to focus only on integration testing
> * Use high-level testing abstractions to speed up test development (PyMTL)


## Python HDL
  - [migen](https://github.com/m-labs/migen) - Meta HDL, Python toolbox for building complex digital hardware, 2011+
  - [Amaranth](https://github.com/amaranth-lang/amaranth) - Refreshed migen Python toolbox, 2018+
  - [MyHDL](https://github.com/myhdl/myhdl) - Process based HDL, verification framework included, 2004+
  - [Pyrope](https://masc.soe.ucsc.edu/pyrope.html) - Python-like language supporting "fluid pipelines" and "live flow", 2017+
  - [PyRTL](https://github.com/UCSBarchlab/PyRTL) - Meta HDL, simulator suitable for research, 2019
  - [PyMTL](https://github.com/cornell-brg/pymtl) - Process based HDL, verification framework included, 2014+
  - [veriloggen](https://github.com/PyHDI/veriloggen) - Python, Verilog centric meta HDL with HLS like features, 2015-?
  - [HDLGen](https://github.com/WilsonChen003/HDLGen) - Tool for processing of embedded Perl or Python in Verilog，2021+
  - [ipyxact](https://github.com/olofk/ipyxact) - Python-based IP-XACT parser
  - [pymtl3](https://github.com/pymtl/pymtl3) - Python hardware generation, simulation, and verification framework, 2019
  - [pyverilog](https://github.com/PyHDI/Pyverilog) - Python design toolkit for Verilog HDL

> * Chisel [31] is based on Scala language and thus inherits the modern SW language features such as parameterized types, abstract data types, operator overloading, and type inference. The Chisel generates to RTL HDL model of the HW, but also the Chisel model can be translated to a cycle-accurate C++ executable for fast simulation. 
>
> * PyMTL [20] supports multilevel modeling on functional, cycle-accurate, and register-transfer levels. One of the key design principles is the modularity of the framework. That is achieved by dividing the platform into frontend, intermediate representations and passes similar to the LLVM compiler architecture. OpenPiton platform [8] uses also a PyMTL-based PyOCN network on chip generator in their work on developing custom SoC chips.
> 
> * PyRTL [13] is a python library for HW modeling similar to PyMTL3. The main difference is that it is a compact core library for HW development, which provides simplicity, usability, and clarity. The PyRTL can be extended with standard python modules, such as math modules to extend modeling capabilities. Verilog and Chisel FIRRTL code can be generated from PyRTL.

## Open Source SoC Generator and Platform

* [chipyard](https://github.com/ucb-bar/chipyard) - Agile RISC-V SoC Design Framework.
* [Litex](https://github.com/enjoy-digital/litex) - SoC builder framework based python
* [SoCMake](https://github.com/HEP-SoC/SoCMake) - Hardware and software build system and package manager based on CMake
* [SoCGen](https://github.com/habibagamal/SoC_Automation) - automates SoC design by taking in a JSON description of system and producing final GDS-II. 
* [Blackparrot](https://github.com/black-parrot/black-parrot) - open-source, Linux-capable, cache-coherent, RV64GC multicore
* [OpenESP](https://github.com/sld-columbia/esp) - Heterogeneous SoC architecture and IP design platform
* [openfasoc](https://github.com/idea-fasoc/OpenFASOC) - Open Source FASOC generators
* [openpiton](https://github.com/PrincetonUniversity/openpiton) - General purpose, multithreaded manycore processor
* [pulp](https://github.com/pulp-platform/pulp) - Multicore RISC-V based SoC
* [pulpissimo](https://github.com/pulp-platform/pulpissimo) - Single core RISC-V based SoC
* [bender](https://github.com/pulp-platform/bender) - Dependency management tool for hardware projects.
* [fusesoc](https://github.com/olofk/fusesoc) - Package manager and build abstraction tool for FPGA/ASIC development.
* [mflowgen](https://github.com/mflowgen/mflowgen) - Build-system generator for ASIC and FPGA design-space exploration.
* [orbit](https://github.com/chaseruskin/orbit) - Package manager and build tool for HDLs
* [siliconcompiler](https://github.com/siliconcompiler/siliconcompiler) - Python based build system and package manager for hardware.
* [Caravel](https://github.com/efabless/caravel) - template SoC for Efabless Open MPW and chipIgnite shuttles based on the Sky130 node from SkyWater Technologies
* [X-HEEP](https://github.com/esl-epfl/x-heep) Platform is a RISC-V MCU described in SystemVerilog that can be configured to target small and tiny platforms as well as extended to support accelerators.
* [iEDA](https://github.com/OSCC-Project/iEDA) - RTL2GDS infrastructure
* [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) - Complete RTL2GDS platform

> * [pulpissimo](https://github.com/pulp-platform/pulpissimo) A single-core platform within the PULP family, designed to target ultra-low-power edgecomputing applications. Depending on performance requirements, designers can configure the platform with the CV32E20 or CV32E40P cores. PULPissimo has been integrated with various accelerators, including the aforementioned multi-CPU cluster, neural network accelerators, CGRAs, eFPGAs, etc. Many silicon prototypes have been implemented, which demonstrate best-in-class energy efficiency in a wide range of applications.
> * However, PULPissimo provides only a generic AXI 32 bit slave and a 64 bit master external interfaces that are used to connect the multi-CPU cluster, while the other accelerators have been integrated by forking and modifying the original RTL code. Such external interfaces may limit accelerators’ bandwidth. Moreover, the platform lacks native support for external interrupts/events and power control, which is crucial for efficient power management. Lastly, the platform does not offer configurability options to select memory size, bus topology, and memory addressing mode, or to change the included peripherals, which limit area, bandwidth, and power-space exploration.
> 
> * [Cheshire](https://github.com/pulp-platform/pulpissimo) The limitations mentioned above have been partially addressed by another PULP-based platform, called Cheshire. Cheshire is based on the CVA6 and allows designers to choose the number of external slave and master ports to connect their custom accelerators. Furthermore, the platform allows for the configuration of the internal last-level cache (LLC) size and of the necessary peripherals, providing the flexibility needed to target specific application requirements.
> * However, Cheshire has been designed for high-performance systems and consumes up to 300 mW, making it unsuitable for most ultra-low-power devices, which typically operate in the range of tens of mW. Furthermore, Cheshire lacks support for external interrupts and power control, which has implications for its overall energy efficiency, as the accelerators are usually power-hungry. Lastly, designers do not have the option to select the core type, bus topology, and memory addressing mode.
>
> * Chipkit [46] uses a template-based code generation implemented in python to generate control and status registers for HW implementation with related SW API and documentation.
> 
> * OpenPiton [8] platform consists of a reused Ariane Linux-capable 64-bit RISC-V CPU core, PyOCN network on chip generator compilation framework for open source EDA tools, and FuseSoC IP management tool.
>
> * OpenESP [32] platform is a GUI-based tool covering accelerator IPs and SoC design tool flows. The ESP platform addresses verification, FPGA synthesis, device drivers, and test applications based on design parameters defined by the user. On the SoC, level connectivity is also addressed in the form of generated routing tables, memory maps, device trees, and SW header files. 
>
> * [Blackparrot](https://github.com/black-parrot/black-parrot) An open-source Linux-capable platform designed to accommodate one or multiple customdesigned accelerators. The platform showcases a mesh of heterogeneous tiles, offering the flexibility to compose 64 bit BlackParrot cores, L2 cache slices, I/O, DRAM controllers, and accelerators in various configurations.
> * However, it does not allow for selecting the core type, bus topology, and memory addressing mode. Additionally, the absence of essential peripherals commonly used in edge devices, such as I2Cs, GPIOs, timers, DMAs, interrupt controllers, and a power manager to implement low-power strategies, restricts the usage of the platform for real applications deployed on ultra-low-power edge applications. Moreover, the platform’s internal integration of accelerators, as opposed to external plug-ins, involves forking and modifying the original RTL code, leading to greater effort and higher development costs. Lastly, the 64 bit architecture of BlackParrot targets high-performance systems and is unsuitable for ultra-low-power edge devices.
>
> * Chipyard [1]. On the contrary, the Rocket chip generator [26], which has been subsequently incorporated and expanded into the Chipyard platform, offers extensive configuration options. Using the open-source Chisel, designers can craft their system, providing flexibility and customization. The platform offers a wide range of core types, including Ariane, CV32E20, Rocket, and BOOM, allowing designers to tailor the system’s performance to meet specific application requirements. Additionally, the memory size and peripherals can be customized, further enhancing its adaptability.
> * However, even though Chipyard enables accelerators to be integrated into the design using the Chisel language, the platform does not offer external master and slave ports for the connectivity of accelerators. As a result, designers need to invest time in becoming familiar with the Chisel language to successfully configure the architecture and integrate custom accelerators. Furthermore, Chipyard does not provide support for any specific power reduction strategies. Given the critical importance of power efficiency in ultra-low-power applications, designers are forced to implement power-saving techniques manually to achieve the desired energy efficiency level.
>
> * [LiteX](https://github.com/enjoy-digital/litex) and OpenESP. Two other notable SoC generators are LiteX and ESP. LiteX serves as a framework thought to explore various FPGA-based architectures. On the other hand, ESP is an open-source platform designed for heterogeneous SoC design and prototyping on FPGAs. Both platforms offer configurable options, allowing designers to customize core type, memory size, peripherals, and the number of external master and slave ports, making them adaptable to various application requirements.
> * However, LiteX and ESP focus on FPGA development only and do not offer support for ASIC design flow. Such limitations hinder their applicability in projects aimed at silicon implementations and present difficulties in accurately estimating the platform energy consumption, crucial when evaluating the impact of integrated accelerators. Moreover, they lack built-in support for external interrupts and power control.
>
> * 

## What is SoC Copliot?

The SoC Copilot framework provides a convenient and efficient infrastructure to create and maintain SoC Platform.The SoC is generated using a custom generator written in Python [migen](https://www.controlpaths.com/2022/11/07/writing-verilog-code-using-python-with-migen/), which pulls together the CPU, peripherals, PAD, clock/reset tree, and creates the address mapping and the platform-support files needed to compile software for the core.

> How to Agile SoC：
> * 100% Python
> * Generator not module 
> * Just instance verilog Module and interconnect

## Implement a Simple SoC

[SoC](https://lab.whitequark.org/notes/2016-10-19/implementing-a-simple-soc-in-migen/) consists of the three main parts: the mor1kx wrapper, the SoC gateware, and the ROM code.

## Reuse Verilog Module

Most of the open-source/shared LiteX designs are directly described in Migen/LiteX, but LiteX but is also **heavily used** to integrate/reuse traditional **Verilog/VHDL** cores (commercial or open-source) and also to integrate cores described in **Spinal-HDL, nMigen or other high level HDL DSL** through **Verilog**.

It is for example very common to create mixed language SoC similar to the following one:

![](https://user-images.githubusercontent.com/1450143/141784446-e60d3905-6f1c-4773-89b9-dfe2074b5686.png)

In this SoC, the integration and most of the cores are directly described with Migen/LiteX but external cores are also integrated:

- The [VexRiscv](https://github.com/SpinalHDL/VexRiscv) CPU, described in [Spinal-HDL](https://github.com/SpinalHDL/SpinalHDL) language, is integrated as a verilog standalone core in the LiteX SoC (Pre-generated verilog configuration from https://github.com/litex-hub/pythondata-cpu-vexriscv or https://github.com/litex-hub/pythondata-cpu-vexriscv_smp).
- The [LiteDRAM](https://github.com/enjoy-digital/litedram) core is in this case integrated as verilog standalone core, generated from a [LiteDRAM's Generator](https://github.com/enjoy-digital/litedram/blob/master/litedram/gen.py) and a `.yml` configuration file (ex: [Arty's yml](https://github.com/enjoy-digital/litedram/blob/master/examples/arty.yml))  with: `litedram_gen arty.yml`
- Core 0 is a VHDL core.
- Core 1 is a Verilog core.

>Note: The VexRiscv configurations can also be directly generated from design's parameters/Spinal-HDL sources when the configuration is not cached/present, where verilog is just used as an intermediate language for the integration.

# Basics
Integrating an external core in LiteX that is not written in native Migen/LiteX is pretty straightforward and follows the exact sames rules than other design flows; the tool just needs to know:

- **The configuration of the core (through parameters) and the description of the interfaces** for the integration in the design.
- **The list of sources describing the core** that will be passed to the toolchain for synthesis, place and route.

# Instantiate a core in the design
Doing the instance of the core in the design configures the core and specifies the interfaces. The framework will then consider the **core as a blackbox with known name and interfaces** and will only discover its contents and integrate it during the synthesis of the design.

To instantiate a core in LiteX we are simply reallying on Migen's Instance:
```python3
din    = Signal(32)
dout   = Signal(32)
dinout = Signal(32)
self.specials += Instance("custom_core",
   p_DATA_WIDTH = 32,
   i_din     = din,
   o_dout    = dout,
   io_dinout = dinout
)
```
The first parameters of the `Instance` is the Module's name (`custom_core` in our example) followed by the parameters and ports of the Module:

Prefixes are used to specify the type of interface:
* `p_` for a Parameter (Python's `str` or `int` or Migen's `Const`).
* `i_` for an Input port (Python's `int` or Migen's `Signal`, `Cat`, `Slice`).
* `o_` for an Output port (Python's `int` or Migen's `Signal`, `Cat`, `Slice`).
* `io_` for a Bi-Directional port  (Migen's `Signal`, `Cat`, `Slice`).

If you are **already familiar with VHDL/Verilog**, you can see that the approach is **very similar** to the one you are already using in these languages, with just more flexibility thanks to Python :)

## A few Python's tricks for Instances:
While an instance has to be declared as a single block in (System)Verilog/VHDL, it's not mandatory with Migen/LiteX since Migen's Instance is relying on a Python's Dict: It's possible to have a lot more flexibility and prepare the Instance's parameters in conditionally or in advance:

```python3
# Create a Dict for the Parameters/IOs.
params_ios = dict()

# Add the Parameters.
params_ios.update(
   p_DATA_WIDTH = 32
)
# Add the IOs.
params_ios.update(
   i_din     = din,
   o_dout    = dout,
   io_dinout = dinout
)
# Do the Instance:
self.specials += Instance("custom_core", **self.params_ios)
```
Splitting the Instance allows the use of Python as a powerful pre-processor to define the Parameters and/or assign the IOs.

This can be very useful to update some Parameters/IOs of the Instance from methods; for example allowing the update the CPU reset address from the design:
```python3
def set_reset_address(self, reset_address):
	self.cpu_params.update(i_externalResetVector=Signal(32, reset=reset_address)) 
```

It can also provide some interesting flexibility to connect group of ports, as done for example below to connect an abitrary number of FIFOs ports when re-integrating a LiteDRAM's standalone core in LiteX design:

```python3
for i in range(fifo_ports):
	litedram_params.update(**{
		# FIFO In.
		f"i_user_fifo_{i}_in_valid": axis_in[i].valid,
		f"o_user_fifo_{i}_in_ready": axis_in[i].ready,
		f"i_user_fifo_{i}_in_data" : axis_in[i].data,
		
		# FIFO Out.
		f"o_user_fifo_{i}_out_valid": axis_out[i].valid,
		f"i_user_fifo_{i}_out_ready": axis_out[i].ready,
		f"o_user_fifo_{i}_out_data" : axis_out[i].data,
})
```
...Or do a one-line connect of a bus with a different name for each bit to a bus of the LiteX design, as done for example on the [LiteICLink ECP5's SerDes](https://github.com/enjoy-digital/liteiclink/blob/master/liteiclink/serdes/serdes_ecp5.py):
```python3
serdes_params.update(**{
# CHX TX — data
**{f"i_CHX_FF_TX_D_{n}" : tx_bus[n] for n in range(tx_bus.nbits)}
})
```
>Note: Python restricts Dict creation/update to 255 items, so large Instances have to split the Dict creation as just described above.

# Adding the sources of a core to the design

With the `Instance`,  the design is now aware of the configuration and interfaces of the integrated core but **still don't know from where this core comes and in which language it is described**.

Adding the sources of the core to the design will allow LiteX to pass these informations to the synthesis toolchain and let the toolchain do the synthesis of the core and integration in the design.

Adding the **single source to the LiteX design** is done with `platform.add_source(...)`
```python3
platform.add_source("core.v")   # Will automatically add the core as Verilog source.
platform.add_source("core.sv")  # Will automatically add the core as System-Verilog source.
platform.add_source("core.vhd") # Will automatically add the core as VHDL source.
```
As can be seen, to simplify things for the User, **LiteX automatically determines the language** based on the file extension:
|      Extension    | Language       |
|-------------------|----------------|
| .vhd, .vhdl, .vho | VHDL           |
| .v, .vh, .vo      | Verilog        |
| .sv, .svo         | System Verilog |

Still to simplify things for User, it is possible to **pass multiple sources at once** with `platform.add_sources(...)`:

```python3
platform.add_sources(path="./",
  "core0.v",
  "core1.vhd",
  "core2.sv"
)
```

Or **just provide the path** and let LiteX automatically collect and add the sources:
```python3
platform.add_source_dir(path="./")
```

This last method is **however not always possible** for all external cores: Some projects provide different implementation of the same module: One for simulation, one specialized for one type of FPGA, etc... and the synthesis toolchain will not be able to automatically select the one to use. In theses cases, the previous methods manually specifying the sources should be used.

For more information about the supported parameters of these methods, the LiteX source code be consulted.

# Reusing a (System)Verilog/VHDL core

Just do the `Instance` in your LiteX design and add the source to the LiteX platform as just described just above.

> Note: For verilog cores [litex_read_verilog](https://github.com/enjoy-digital/litex/blob/master/litex/tools/litex_read_verilog.py) tool can be useful to generate the Instance template.

# Reusing a Amaranth/Spinal-HDL/Chisel/etc... core

This is very similar than reusing a Verilog/VHDL core with just one extra step: **Generate** the Amaranth/Spinal-HDL/Chisel/etc.. core **as a verilog core** :)

# Examples of more complex integration

The [Betrusted.io](https://github.com/betrusted-io) project relies on LiteX for the integration and makes heavy use of external Verilog/System Verilog cores. This can then be a good source of integration examples such as [the integration of an I2C core from  OpenCores](https://github.com/betrusted-io/gateware/blob/master/gateware/i2c/core.py).

# Reusing other type of cores

In some cases, some encrypted cores or proprietary core formats needs to be passed to the toolchain: On Xilinx design you'll generally have to integrate `.xci` files or `.tcl` scripts that will automatically generate the cores.

Most of these use-cases are probably already supported by LiteX but aren't (yet) documented here. Please have a look at the LiteX source code, the different LiteX [ressources](https://github.com/enjoy-digital/litex/wiki/Tutorials-Resources), [projects](https://github.com/enjoy-digital/litex/wiki/Projects) or at the targets from [LiteX-Boards](https://github.com/litex-hub/litex-boards/tree/master/litex_boards/targets) to find similar integration cases.



## Table of Contents

- [Basics](#basics)
- [Instantiate a core in the design](#instantiate-a-core-in-the-design)
  - [A few Python's tricks for Instances:](#a-few-pythons-tricks-for-instances)
- [Adding the sources of a core to the design](#adding-the-sources-of-a-core-to-the-design)
- [Reusing a (System)Verilog/VHDL core](#reusing-a-systemverilogvhdl-core)
- [Reusing a Amaranth/Spinal-HDL/Chisel/etc... core](#reusing-a-amaranthspinal-hdlchiseletc-core)
- [Examples of more complex integration](#examples-of-more-complex-integration)
- [Reusing other type of cores](#reusing-other-type-of-cores)
  - [Table of Contents](#table-of-contents)
  - [LiteX Design Flow in a nutshell](#litex-design-flow-in-a-nutshell)
  - [What is Migen?](#what-is-migen)
    - [Comb](#comb)
    - [Sync](#sync)
    - [Submodules](#submodules)
    - [Specials](#specials)
      - [Instances](#instances)
      - [MultiReg](#multireg)
  - [Module Attributes](#module-attributes)
  - [FSMs](#fsms)
  - [ClockDomains](#clockdomains)
  - [Physical Constraints](#physical-constraints)
    - [Pin Constraints](#pin-constraints)
    - [Timing Constraints](#timing-constraints)
  - [Timing Reports \& Schematics](#timing-reports--schematics)
  - [Softcores](#softcores)
    - [CSRs: Config and Status Registers](#csrs-config-and-status-registers)
  - [Design Patterns](#design-patterns)
    - [Timing Delays](#timing-delays)
    - [Module I/O](#module-io)
    - [Streams](#streams)
    - [Records](#records)
    - [Multi-Domain Clocking](#multi-domain-clocking)
  - [Debugging](#debugging)
    - [Litescope](#litescope)
      - [Litescope Sampler](#litescope-sampler)
      - [Litescope Bridge](#litescope-bridge)
      - [Litescope Host](#litescope-host)
      - [FSM Support](#fsm-support)
    - [Netlist](#netlist)
  - [Reference](#reference)


## LiteX Design Flow in a nutshell

LiteX is an open-source Python-based SoC (System on Chip) builder framework designed to simplify FPGA development. It provides a flexible and modular architecture that allows developers to create custom digital designs ranging from simple controllers to complex, CPU-based systems. This introduction provides an overview of LiteX's purpose, architecture, and core components.

At its core, LiteX is a tool that enables you to:

1. Define your hardware in Python using the Migen HDL library
2. Integrate various IP cores from the LiteX ecosystem
3. Connect these components using standardized buses and interfaces
4. Generate HDL code (Verilog/VHDL) for FPGA implementation
5. Build and flash designs to supported FPGA boards
6. Debug and interact with your designs through various interfaces

LiteX implements a design flow that takes you from Python code to a running FPGA system.




LiteX relies on a Python toolbox called [Migen](https://github.com/m-labs/migen). In addition to a build environment, it provides a set of IP blocks. 

LiteX natively supports Linux/x86. It requires Python 3.5 or later. You'll need to manually download, install, and provision your back-end tools (e.g., Vivado/ISE), and you'll also need to install a gcc cross-compiler to any softcore CPU you plan to use in your designs.

1. Describe your design in Python using the migen toolbox and LiteX IP by customizing a `Module` object (typically by subclassing `SoCSDRAM`, which is a subclass of `SoCCore` which subclasses the base `Module` class)
2. Describe your build environment by customizing a `Platform` object (typically by subclassing the `XilinxPlatform` class which itself subclasses the `GenericPlatform` base class)
3. Run a function which passes your `Platform` object to a `Builder` object, and invokes the `build()` method which:
   - Creates a `top.v` file: a single, flat verilog netlist of your entire design modulo a few exceptions
   - Creates a `top.xdc` file: constraints that locate pins, defines clocks, and eliminates false paths
   - If a CPU is configured, generates and builds a BIOS binary to be compiled into the design
   - If a toolchain is configured, creates a `top.tcl` file which drives the proprietary synth/place/route/bitgen "backend" toolchain
   - Attempts to run the proprietary back-end tool (Vivado will be assumed for this doc, but ISE is also supported)
4. Run `make` in the `firmware` directory, which builds your firmware binary (`firmware.bin`)
5. Upload `top.bit` to the FPGA -- typically over JTAG via openOCD
6. Upload `firmware.bin` to the FPGA -- typically via UART or Ethernet, using the `flterm` host-native application and the `serialboot` command
7. Interact with your firmware's REPL loop using flterm
8. If you designed a `litescope` into your design (an ILA like Chipscope), configure triggers and download traces using an analyzer script, which relies on a helper program called litex_server
9. Find bugs & go back to step 1!

## What is Migen?

Migen is the Python toolbox that is used to create a description of your hardware design. It abuses Python's object-oriented class and method system to create a design tree embodied as a single mega-object using a process called "finalization".

For design description, the base class is a "Module". It has five key attributes used to organize the elements that describe any hardware design:

- Comb
- Sync
- Submodules
- Specials
- ClockDomains

Each of these attributes is a list, and a design is described by appending an element to the appropriate list. Once all the lists have been populated, the submodules are collected and then finalized into a single, huge verilog netlist.

The elements that go into a design description are numerous, but the most common one you'll encounter is `Signal()`, followed distantly by `ClockDomain()` and `Instance()`.

A `Signal()`, as its name implies, is a named net. By default, a `Signal()` has a bit width of 1. An n-bit signal is created by `Signal(n)`. Groups of Signals() can be bundled together in `Records()` and `Streams()`, more on that later. A `Signal()` has no inherent direction, clock domain, or meaning. It picks this all up based on how you use it: which attribute of the `Module` class you've assigned it to, and so forth.

> **Caution**: In Migen, you can specify the number of bits for a `Signal()` by doing `Signal(max=8)`. Counter to what you think it should do, `max` is *exclusive* (but `min` is *inclusive*), so `Signal(max=8)` cannot actually hold the number `8`. It can hold the number `7`, because it will infer only three bits for the directive `max=8`. I was not in the room when this was decided.

> **Tip**: Dangling references and signal name typos will result in Python crashes during the finalization process, and you are expected to dig through the stack trace to find the problem. Because finalization disassociates the locality of a reference from the code that created it, this can be difficult. It helps to have an IDE with a debug mode that allows you to click into a stack level and then inspect variables at various stack levels to try and identify where you went wrong.

> **Caution**: Forgetting to add new objects to one of the five key Module attributes means it will not be finalized. Thus, *you* might see your logic in the Python code, but if it doesn't get finalized, it might as well just be commented out as far as migen is concerned.

Let's look at what each of these five attributes are, one at a time.

### Comb

The `comb` attribute is a list of "combinational" logic operations. The verilog equivalent is everything that occurs outside an `always @(posedge)` block, e.g., all your assign statements. Since `comb` is a list, you append operations onto the list using Python list syntax. `self` is a shortcut to your module object, and `.comb` is how you reference the `comb` attribute:

```python
foo = Signal()  # these are all one-bit wide by default
bar = Signal()
baz = Signal()
mumble = Signal()
self.comb += [
    foo.eq(bar),
    baz.eq(foo & mumble),  # trailing commas at the end of a list are OK in python
]
```

This is the verilog equivalent of:

```verilog
wire foo;
wire bar;
wire baz;
wire mumble;
assign foo = bar;
assign baz = foo & mumble;
```

You'll notice that there's no `=` operator -- assignment (and thus declaration of which signal in the source and sink) is done by invoking `.eq()` on the sink and putting the source as the argument for a signal. However, most arithmetic operations are available between Signals, e.g., `~` is invert, `&` is and, `|` is or, `+` is add, `*` is multiply. I think there's also divide and I have no idea about signed types.

### Sync

The `sync` attribute is the list of synchronous operations. Items added to this list will generally infer a clocked register.

"But to what clock domain?" I hear you ask. Migen starts with a single, default clock domain called `sys`. Its frequency is defined by passing a mandatory `clk_freq` argument to the `SoCSDRAM` base class, and it's up to you to actually hook up a clock generator that is at the right frequency.

You can also specify which clock domain you want registers to go to by adding a modifier to the `sync` attribute. The migen methodology prescribes *not* assigning a clock domain until a module is instantiated. So if a sub-module's design can be implemented in a single, synchronous domain, just use the generic `sync` attribute. If the sub-module requires two clock domains, it's actually recommended to make up a "descriptive" name for the module, such as `write` and `read` clock domains for a FIFO. Then, when the modules are created, the all the clocks can be renamed to be consistent with the instantiating-module level clock names using a function called `ClockDomainsRenamer()`.

Clear as mud? Some examples will help.

```python
foo = Signal()
bar = Signal()
bar_r = Signal()
self.sync += [
    bar_r.eq(bar),
    foo.eq(bar & ~bar_r),
]
```

This is the verilog equivalent of:

```verilog
wire bar;
reg foo = 1'd0;  // yes, the autogen code will use decimal constants
reg bar_r = 1'd0;
always(@posdege sys_clk) begin
    bar_r <= bar;
    foo <= bar & bar_r;
end
```

Again, `sys_clk` is implicit because we used a "naked" `self.sync`. And, note that the "zero" initializer of every register is part of the migen spec (so if you forget to hook up an input to an output, you get zeros injected at the break and no warnings or errors thrown by the verilog compiler).

If you wanted to do two clock domains, you might do something like this:

```python
class Baz(Module):
    def (self):
        foo = Signal()
        bar_r = Signal()
        bar_w = Signal()
        self.sync.read += bar_r.eq(foo)   # when adding just one item to the list, you can use +=
        self.sync.write += bar_w.eq(foo)
```

This is the verilog equivalent of:

```verilog
wire foo;
reg bar_r = 1'd0;
reg bar_w = 1'd0;
always(@posedge read_clk) begin
    bar_r <= foo;
end
always(@posedge write_clk) begin
    bar_w <= foo;
end
```

Easy enough, but where does `read_clk` and `write_clk` come from? Notice how I encapsulated the Python in a module called `Baz()`. To assign them in an upper level function, do this:

```python
mybaz = Baz()
mybaz = ClockDomainsRenamer( {"write" : "sys", "read" : "pix"} )(mybaz)
self.submodules += mybaz  # I'll describe why this is important later, but it's IMPORTANT
```

What's happened here is the the `write` domain of this instance of `Baz()` got assigned to the (default) `sys` clock domain, and the `read` domain got assigned to a `pix` clock domain (which presumably, you've created in the `ClockDomains` attribute, more on how to do that later). As you can see here, the `ClockDomainsRenamer` lets us go from the local names of the function to the instance names used by the actual design, based on a Python dictionary that has the format `{"submodule1_clock" : "actual1_clock", "submodule2_clock" : "actual2_clock", ...}`.

The final re-assignment of `mybaz` to `mybaz` isn't mandatory, but since you never want to use the original instance of it, it's helpful to discard any possibility of confusing yourself with the old an new versions by re-assigning the modified object to its original name.

There's one other trick for `ClockDomainsRenamer`. Quite often you're looking to actually rename the default `sys` clock to something else, because most modules are written just adding items to the base `sync` domain (and hence the default sys clock domain) This leads to this shortcut:

```python
myfoo = Foo()
myfoo = ClockDomainsRenamer("pix")(myfoo)
self.submodules += myfoo
```

The one argument is automatically expanded by the ClockDomainsRenamer to the dictionary `{"sys":"lone_argument_clk"}`.

### Submodules

Noticed how above, I was particular to include a line `self.submodules += myfoo` or similar at the end of every example? This has to do with the submodules attribute.

Designs can be hierarchical in migen. That's a good thing, but you have to tell migen about the submodules, or else they don't do anything. You tell migen about a submodule -- and thus include it for flattening and netlisting -- by adding it to the `submodule` attribute. Forgetting to do so will silently fail, throwing no errors and leaving you wondering why the submodule you thought you included is outputting nothing but 0.

Here's a simple example:

```python
myfoo = Foo()
myfoo = ClockDomainsRenamer("pix")(myfoo)
self.submodules += myfoo
```

versus

```python
myfoo = Foo()
myfoo = ClockDomainsRenamer("pix")(myfoo)
```

What's the difference? In the first one, we remembered to add our module to the submodules list. In the second one, we created the submodule, did something to it, but didn't add it to the submodules list.

The second one is perfectly valid Python syntax; it will compile and run, and the verilog generated will throw no errors, but if you look at the netlist, the entire contents of the `myfoo` instance is missing from the generated netlist.

In other words, it's extremely easy to forget to add something to the submodules list, and forgetting to do so means the submodule is never flattened during the build process and thus never sent to the code generator. And because migen initializes all registers to 0, the absence of the module will result in perfectly valid verilog being generated that throws no errors.

So I try to include that line in every example, even the short ones, to save you the headache and trouble.

One other confusing bit about adding something to submodules is that later references go through `self`. Easier to see code than explain:

```python
self.submodules.myfoo += Foo()
self.comb += self.myfoo.subsignal.eq(othersignal)
```

In the example above, you added `Foo()` to `submodules.myfoo`, but later on you /reference/ it through `self.myfoo`.

### Specials

Specials are how migen handles certain design elements that don't fit into the comb/sync paradigm or have to pierce the abstraction layer and do something platform or implementation-specific.

On the Xilinx platform, these are the specials I'm aware of:

- Instantiating a verilog module or primitive
- MultiReg
- AsyncResetSynchronizer
- DifferentialInput
- DifferentialOutput
- Memory

You might be tempted to stick a special in the `submodules` attribute, but that won't work because their template class is `Special`, not `Module`. Like all the other attributes, you add to a special by just using the `+=` pattern:

```python
self.specials += MultiReg(consume.q, consume_wdomain, "write")
self.specials += Instance("BUFG", i_I=self.pll_sys, o_O=self.cd_sys.clk)
```

#### Instances

The `Instance` special is particularly handy. You use this to summon blocks like `BUFG`, `BUFIO`, `BUFR`, `PLLE2`, `MMCME2` and so forth. The format of an Instance special is as follows:

```python
Instance( "VERILOG_MODULE_NAME", ...list of parameters or ios.... )
```

So if a verilog module has a template like this:

```verilog
foo #(
    .PARAM1("STRING_PARAM"),
    .PARAM2(5.0)
)
foo_inst(
    .A(A_THING),  // output: A
    .B(B_THING),  // input: B
    .C(C_THING),  // inout: C
);
```

The Instance format would look like this:

```python
migen_sigA = Signal()
migen_sigB = Signal()
migen_sigC = Signal()
self.specials += [
Instance("foo",
            p_PARAM1="STRING_PARAM",
            p_PARAM2=5.0,
            i_A=migen_sigA,
            o_B=migen_sigB,
            io_C=migen_sigC
            ),
]
```

If you're looking to instance a module that's your own verilog and not part of the Xilinx primitives, you can add the verilog file with a platform command:

```python
self.platform.add_source("full/path/to_module/module1.v")
```

This leaves the module hierarchy intact, and you also have to add all submodules referenced by your verilog to the path as well.

Specials can also be used to refer to vendor IP. For example:

```python
# ila
platform.add_source("ila_0/ila_0.xci")
probe0 = Signal(6)
self.comb += probe0.eq(Cat(spi_pads.clk, spi_pads.cs_n, spi_pads.wp, spi_pads.hold, spi_pads.miso, spi_pads.mosi))
self.specials += [
    Instance("ila_0", i_clk=self.crg.cd_sys.clk, i_probe0=probe0),
]
platform.toolchain.additional_commands += [
    "write_debug_probes -force {build_name}.ltx",
]
```

#### MultiReg

MultiReg is a one-bit synchronizer for crossing asynchronous domains. By default, it creates two registers that go into a `sys` clock domain, but you can change which domain it goes to by specifying an `odomain` parameter:

```python
self.specials += MultiReg( input_domainA, output_domainB, "pix" )
```

Will take signal `input_domainA`, instantiate two registers in the `pix` domain, and the `output_domainB` will be synchronized accordingly. The reason this is in a special block is there are some attributes added to prevent retiming optimization from modifying the synchronizer structure: presumably if you did this just using `self.sync` operations you might not get the expected outcome after optimizations.

Migen includes a whole bunch of clock-domain crossing tools, including a `PulseSynchronizer` and `Grey` counters. Take a look inside the `migen/genlib/cdc.py` file for some ideas.

## Module Attributes

- [FSMs](#fsms)
- [ClockDomains](#clockdomains)
- [Physical Constraints](#physical-constraints)
- [Timing Reports & Schematics](#timing-reports--schematics)
- [Softcores](#softcores)
- [Design Patterns](#design-patterns)
- [Debugging](#debugging)
- [IP Cores](#ip-cores)
- [Simulation](#simulation)
- [Configuration](#configuration)
- [Glossary](#glossary)

## FSMs

FSMs are finite state machines. They are implemented using the `sync` attribute in Migen.

Migen supports a native syntax for creating FSMs. You can create an FSM in the current module by invoking the FSM() function, and then using .act() accessors to delineate new states within the FSM. Here's a basic example of how this works.

```python
fsm = FSM()
self.submodules.fsm = fsm   # need this to enable litescope debugging

fsm.act("WAIT_SOF",
    reset_words.eq(1),
    If(self.address_valid &
       self.frame.sof,
       NextState("TRANSFER_PIXELS")
    )
)
fsm.act("TRANSFER_PIXELS",
    self.transfer_enable.eq(1),
    If(self.address_count == self.frame_length,
       NextState("EOF")
    )
)
fsm.act("EOF",
    If(~dram_port.wdata.valid,
        NextState("WAIT_SOF")
    )
)
```

This FSM creates three states, WAIT_SOF, TRANSFER_PIXELS, and EOF, and cycles between them based on the conditions coded in the If() statements.

> **Warning**: *Direct vs. NextValue* There are two ways to set outputs within an FSM: direct, and NextValue(). The example above only uses the direct method. Direct value settings clear to zero in every state where they are not mentioned. Thus, the statement "self.transfer_enable.eq(1)" inside of "TRANSFER_PIXELS" only sets transfer_enable to 1 during that state only, and in all other states, the value is zero. Furthermore, transfer_enable is a result of an purely combinational computation on the state bit, so it changes to 1 upon entering TRANSFER_PIXELS. 
>
> Alternatively, one can use NextValue(signal, value), as in, "NextValue(self.transfer_enable, 1)". This macro does two things: (1) the value is latched, so it persists even after leaving the state (it does not clear to zero unless explicitly cleared) and (2) the value will not change until one clock edge later.

> **Caution**: It appears one can use both direct and NextValue at the same time without triggering a compilation error. The behavior, however, depends on if there is a previous NextValue() that could conflict with the direct setting. Which one "wins" depends upon the ordering of the two statements in the top.v generate by Migen. At least in one version, the synchronous statements are lower in the file than the asynchronous statements, and thus the NextValue() call would override the direct call in the case of a conflict. However, if there is no conflict between NextValue and direct, this will cause the value to change upon entering the state and it will persist until cleared.

By convention, the first FSM.act() entry is also the reset state of the FSM. This is because as far as I can tell the state bits are encoded staring from 0 going up with each successive FSM.act() call, and FPGAs by default initialize their registers to 0. If you want to explicitly designate a reset state, use the "reset_state=" argument when creating the FSM object, e.g.:

```python
fsm = FSM(reset_state = "WAIT_SOF")
```

The default clock domain of an FSM is, as always, "sysclk". You can remap this using the ClockDomainsRenamer:

```python
fsm = ClockDomainsRenamer("new_clk_domain")(FSM())
```

Alternatively if you want the entire module to be synchronous and in a different domain, don't rename the FSM immediately upon creation, but rename the entire module at the point where it is instantiated (e.g. allow all the self.sync's to be default (sysclk) and then remap sysclk for the whole domain using the ClockDomainsRenamer at one level up the tree).

## ClockDomains

ClockDomains are used to organize the clock domains in your design. They are implemented using the `ClockDomains` attribute in Migen.

## Physical Constraints

Physical Constraints are used to place and route your design on the FPGA. They are implemented using the `Platform` object in LiteX.

### Pin Constraints

To be written -- how to add pin location constraints to your project.

### Timing Constraints

To be written -- how to add additional timing constraints to your project.

## Timing Reports & Schematics

Timing Reports and Schematics are used to analyze the timing of your design. They are implemented using the `Platform` object in LiteX.

## Softcores

Softcores are used to implement the CPU in your design. They are implemented using the `SoCCore` class in Migen.

### CSRs: Config and Status Registers

Configuration and status registers are how you get a softcore to "peek" and "poke" memory. They map addresses to lines that you can wiggle or observe.

The nomenclature of migen is:

- "CSRStorage" = "output" (from CPU's perspective) = "write" or "stores"
- "CSRStatus" = "input" (from CPU's perspective) = "read" or "loads"

There's also a "generic" CSR which is both read and write. You can use this, but the width is limited to less than the CSR bus width.

You can add CSRs to modules (but not the top level SoC instantiation), because CSR C-code APIs are auto-generated based on the module's name. No name, no API.

> **Caution**: CSRs are a bit odd, by default they are byte-wide registers that are on 32-bit word boundaries. So a "32-bit" CSR is actually broken into four bytes spanning a total address space of 16 bytes. You can specify 32-bit wide CSRs but you'll probably run into compatibility issues with other IP librariers that have hard-coded the 8-bit assumption.

> **Warning**: If you allocate too many CSRs, you can overflow the CSR address space width without warning. If you find your CPU isn't booting after a recompile, try adding the line "csr_address_width=15" to your BaseSoC arguments. The default width is 14 bits.

Here's a very simple example of how to use CSRs to talk to an external IP block written in verilog.

```python
class I2Csnoop(Module, AutoCSR):
    def __init__(self, pads):
        self.edid_snoop_adr = CSRStorage(8)
        self.edid_snoop_dat = CSRStatus(8)

        reg_dout = Signal(8)
        self.An = Signal(64)  
        self.Aksv14_write = Signal() 
        self.specials += [
            Instance("i2c_snoop",
                     i_SDA=~pads.sda,
                     i_SCL=~pads.scl,
                     i_clk=ClockSignal("eth"),
                     i_reset=ResetSignal("eth"),
                     i_i2c_snoop_addr=0x74,
                     i_reg_addr=self.edid_snoop_adr.storage,
                     o_reg_dout=reg_dout,
                     o_An=self.An,
                     o_Aksv14_write=self.Aksv14_write,
                     )
        ]
        self.comb += self.edid_snoop_dat.status.eq(reg_dout)
```

Other sections talk more about using self.specials to create an external verilog block, but basically, there is a verilog module called i2c_snoop.v that's instantiated here, and the CPU is wired up to the snoop module to query what data has been captured by the snooper from a given address. So, edid_snoop_adr is a CSRStorage(8) -- it's an "output" of the CPU that's 8 bits wide driving into the verilog block. And edid_snoop_dat is a CSRStatus(8) -- it's an "input" of the CPU that's 8 bits wide that reads the data presented by the verilog block. Note that all signals are assumed synchronous to the "sys" clock domain, but in this case i2c_snoop is plugged into the "eth" clock domain. For this purpose, it's OK because we guarantee at the firmware level we don't read the I2C block when the data is changing, but you will need to add MultiRegs or other forms of synchronizers if whatever you're driving from the CPU isn't in the "sys" clock domain.

In order to trigger the auto-generation of the CSR code, you have to add it to the csr_peripherals block of your SoC. This is usually up near the top of your SoC definition, a bit like this:

```python
class VideoOverlaySoC(BaseSoC):
    csr_peripherals = [
        "i2c_snoop",  # if this doesn't exist, the APIs won't get generated
        "analyzer",
    ]
    csr_map_update(BaseSoC.csr_map, csr_peripherals)

    def __init__(self, platform, *args, **kwargs):
        BaseSoC.__init__(self, platform, *args, **kwargs)

        platform.add_source(os.path.join("overlay", "i2c_snoop.v"))
        self.submodules.i2c_snoop = i2c_snoop = I2Csnoop(hdmi_in0_pads)  # the submodule name here must match the csr_peripherals string
```

You'll end up getting a set of CSR helper functions located in the csr.h file. You want to use the helper functions because they hide the wart CSR space being byte-wide data strided on word boundaries.

```c
/* i2c_snoop */
#define CSR_I2C_SNOOP_BASE 0xe000b000
#define CSR_I2C_SNOOP_EDID_SNOOP_ADR_ADDR 0xe000b000
#define CSR_I2C_SNOOP_EDID_SNOOP_ADR_SIZE 1
static inline unsigned char i2c_snoop_edid_snoop_adr_read(void) {
    unsigned char r = MMPTR(0xe000b000);
    return r;
}
static inline void i2c_snoop_edid_snoop_adr_write(unsigned char value) {
    MMPTR(0xe000b000) = value;
}
#define CSR_I2C_SNOOP_EDID_SNOOP_DAT_ADDR 0xe000b004
#define CSR_I2C_SNOOP_EDID_SNOOP_DAT_SIZE 1
static inline unsigned char i2c_snoop_edid_snoop_dat_read(void) {
    unsigned char r = MMPTR(0xe000b004);
    return r;
}

///// included here to illustrate the CSR space byte-to-word weirdness
#define CSR_HDMI_IN1_DMA_SLOT1_ADDRESS_ADDR 0xe00088f8
#define CSR_HDMI_IN1_DMA_SLOT1_ADDRESS_SIZE 4
static inline unsigned int hdmi_in1_dma_slot1_address_read(void) {
    unsigned int r = MMPTR(0xe00088f8);
    r <<= 8;
    r |= MMPTR(0xe00088fc);
    r <<= 8;
    r |= MMPTR(0xe0008900);
    r <<= 8;
    r |= MMPTR(0xe0008904);
    return r;
}
static inline void hdmi_in1_dma_slot1_address_write(unsigned int value) {
    MMPTR(0xe00088f8) = value >> 24;
    MMPTR(0xe00088fc) = value >> 16;
    MMPTR(0xe0008900) = value >> 8;
    MMPTR(0xe0008904) = value;
}
```

With these helper functions, dumping the memory space of the I2C snooper is quite easy:

```c
int i;
for(i = 0; i < 256; i++) {
    if((i % 16) == 0) {
        wprintf("\r\n %02x: ", i);
    }
    i2c_snoop_edid_snoop_adr_write(i);
    wprintf("%02x ", i2c_snoop_edid_snoop_dat_read());
}
```

In addition to providing convenient APIs on the C-code firmware side, CSRs also provide some convenience on the hardware Python side.

- You can specify the reset value by passing the reset=value parameter (for both Storage and Status)
- `.re` is a "write" strobe -- the .re attribute provides a single-cycle pulse when a CSRStorage is updated
- `.we` is a "read" strobe -- the .we attribute provides a single-cycle pulse when a CSRStatus is read
- **yes, you read those two lines above correctly. in Litex, .re is a write, and .we is a read.** I was not in the room when this was decided.
- if write_from_dev=True is passed as a parameter to CSRStorage, the device can flip the storage bit (allowing it to work as an input, oddly enough), by providing data on .dat_w, and strobing .we. Difference between this and CSR is reads are not guaranteed atomic when CSRStorage is made writeable.

If you're using a straight-up CSR (not a Storage or Status), the accessors for the stored value is the .r attribute, and the data you're sending back to the CPU is connected via the .w attribute.

## Design Patterns

A collection of design patterns enabled by the migen toolbox.

### Timing Delays

Timing delays -- inserting pipeline registers to equalize delays between control and data paths -- is a common task. There's a few ways to do it in Migen. Here's some examples.

The simplest way to create a delay is to make it manually:

```python
sig = Signal()
sig1 = Signal()
sig2 = Signal()
sig3 = Signal()
self.sync += [
    sig3.eq(sig2), # three clock cycles delay
    sig2.eq(sig1),
    sig1.eq(sig),
]
```

This can get cumbersome for busses. Here's an example of creating a record that defines a bus, and then using a parameterizeable function that builds the delay pipe with a for loop.

```python
rgb_layout = [  # define the bus layout as a record
    ("r", 8),
    ("g", 8),
    ("b", 8)
] 

class TimingDelayRGB(Module):
    def (self, latency):
        self.sink = stream.Endpoint(rgb_layout)    # "inputs"
        self.source = stream.Endpoint(rgb_layout)  # "outputs"

        for name in list_signals(rgb_layout):
            s = getattr(self.sink, name)
            for i in range(latency):
                next_s = Signal(len(s))
                self.sync += next_s.eq(s)          # self.sync means this module by default is using "sys" clock
                s = next_s
            self.comb += getattr(self.source, name).eq(s)

class MyModule(Module):
    def (self):
        timing_rgb_delay = TimingDelayRGB(4) 
        timing_rgb_delay = ClockDomainsRenamer("pix_o")(timing_rgb_delay)  # remap the default "sys" clock to local "pix_o" domain
        self.submodules += timing_rgb_delay                   # if you forget this line, the timing delay won't be generated in the verilog netlist

        self.hdmi_out0_rgb = hdmi_out0_rgb = stream.Endpoint(rgb_layout) 
        self.hdmi_out0_rgb_d = hdmi_out0_rgb_d = stream.Endpoint(rgb_layout) 
        self.comb += [
            hdmi_out0_rgb.b.eq(core_source_data_d[0:8]),   # wire up the input record
            hdmi_out0_rgb.g.eq(core_source_data_d[8:16]),
            hdmi_out0_rgb.r.eq(core_source_data_d[16:24]),
            hdmi_out0_rgb.valid.eq(core_source_valid_d),

            timing_rgb_delay.sink.eq(hdmi_out0_rgb),       # wire the input record to the timingdelay element

            hdmi_out0_rgb_d.eq(timing_rgb_delay.source)    # hdmi_out0_rgb_d is 4 cycles delayed from hdmi_out0_rgb
        ]
```

So this uses a `record` with `r,g,b` fields, takes a latency parameter, and automatically iterates through the latency depth and creates a set of daisy-chained registers.

Note that in the `TimingDelayRGB()` module, we're iterating through and using the same variable name, `next_s` over and over again. It would seem that this wouldn't make a delay, but rather a whole bunch of wires all tied to the same signal. However, `next_s` is just a temporary variable name, and the `Signal()` `**object**` assigned to it is always unique because every call to `Signal()` creates a brand new `Signal()` object.

Breaking it down step by step:

```python
next_s = Signal(len(s))
```

Is creating a new `Signal()` object, with a globally unique ID, and temporarily binding it to `next_s`.

```python
self.sync += next_s.eq(s)
```

This adds the `next_s` `Signal` to the `sync` list. What happens is migen automatically sees that the object referenced by `next_s` is unique, and resolves this by internally appending a unique number to `next_s` to make the instance unique. If you look at the generated verilog, you'll see `next_s1`, `next_s2`, `next_s3`, ... and so forth as it "uniquefies" the instances added to the sync attribute list.

```python
s = next_s
```

This line just stashes the reference to the Signal so the next iteration of the loop can wire up the daisy chain.

If instead of creating a new `Signal()` object and assigning it to `next_s`, but instead referencing an existing signal with the same globally unique ID, you would in fact have a whole series of `Signal`s just wire-OR'd together.

Here's another design pattern for doing timing delays.

```python
for i in range(rgb2ycbcr.latency + chroma_downsampler.latency):
    next_de = Signal()
    next_vsync = Signal()
    self.sync.pix += [
        next_de.eq(de),
        next_vsync.eq(vsync)
    ]
    de = next_de
    vsync = next_vsync
```

This is an in-line approach to creating the delays, reasonably compact and doesn't require templates to be defined for every signal group.

A final design pattern is to implement a synchronous buffer using a memory element to implement a delay:

```python
class _SyncBuffer(Module):
    def (self, width, depth):
        self.din = Signal(width)
        self.dout = Signal(width)
        self.re = Signal()

        produce = Signal(max=depth)
        consume = Signal(max=depth)
        storage = Memory(width, depth)
        self.specials += storage

        wrport = storage.get_port(write_capable=True)
        self.specials += wrport
        self.comb += [
            wrport.adr.eq(produce),
            wrport.dat_w.eq(self.din),
            wrport.we.eq(1)
        ]
        self.sync += _inc(produce, depth)

        rdport = storage.get_port(async_read=True)
        self.specials += rdport
        self.comb += [
            rdport.adr.eq(consume),
            self.dout.eq(rdport.dat_r)
        ]
        self.sync += If(self.re, _inc(consume, depth))
```

This uses the "Memory" paradigm plus pointer arithmetic. It has the advantage that the delay can be varied dynamically (not at compile time) and can also be more efficient for long delays, since instead of eating FD's for delays it's using a block RAM. It does require some additional logic to wrap around the `SyncBuffer` to let it "fill" first to the depth you need for the delay before draining it.

### Module I/O

How streams & records can be used for module I/O

### Streams

More about how streams a can be used (asyncfifo, upconverter, downconverter, etc.)

### Records

...yah...i don't even know this one really, but it seems important...

### Multi-Domain Clocking

Design patterns and strategies for dealing with multiple clock domains

## Debugging

### Litescope

Litescope is the equivalent of the Xilinx ILA for Litex. It samples a set of signals into holding registers that can be read out via wishbone. Because it's wishbone-based, the data read out can occur via any wishbone bridge -- UART, ethernet, or PCI.

Only simple trigger conditions are supported (signal equals 1 or 0, no edges or compound statements)

So, the architecture of a litescope instantiation consists of two parts: the sampler, and the wishbone readout bridge.

#### Litescope Sampler

You'll need to modify three sections in your SoC description to add an analyzer. See below for the three sections called out:

```python
class MySoC(BaseSoC):
    csr_peripherals += "analyzer"  ## 1. need this to create the wishbone interface
    csr_map_update(BaseSoC.csr_map, csr_peripherals)
    
    def __init__(self, ...):
        # 2. add this inside your "init" function of your base SoC
        from litescope import LiteScopeAnalyzer
        analyzer_signals = [
            signal1,
            signal2,
        ]
        analyzer_depth = 128 # samples
        analyzer_clock_domain = "sys"
        self.submodules.analyzer = LiteScopeAnalyzer(analyzer_signals,
                                                     analyzer_depth,
                                                     clock_domain=analyzer_clock_domain)

    # 3. Add this function to your SoC definition to generate the analyzer definition file.
    builder = Builder(soc, output_dir="build",
                      compile_gateware=not args.nocompile_gateware,
                      csr_csv="test/csr.csv")
    vns = builder.build()
    soc.analyzer.export_csv(vns, "test/analyzer.csv") # Export the current analyzer configuration
```

Basically, you assign the signals to the analyzer_signals domain, and then instantiate the LiteScopeAnalyzer(). Here's the arguments to LiteScopeAnalyzer:

- analyzer_signals -- the array of signals to be sampled
- depth -- in this case 128. Depth is limited by the capacity of your FPGA (so it's width of analyzer_signals * depth < available memory)
- sampler domain -- the name of tho clock domain that your signals are coming from. `sys` by default.

You also need to hook `do_exit()` of your SoC description to generate the `analyzer.csv` file. You should change the path to wherever your analyzer readout script is located (couple sections down for more on that one). You also need to add `analyzer` to the CSR peripherals list so it shows up in the firmware address space. This function gets called automatically if it exists.

#### Litescope Bridge

You have many choices to extract data from the lightscope sampler. It's just another etherbone peripheral, so you could use the local softcore CPU to read out data. Or you can send commands over a bridge that translates e.g. UART, PCI express, or Ethernet to wishbone addresses and vice versa.

Here's an example of a UART bridge:

```python
# 1. define the pins
_io += [
    ("serial", 1,
        Subsignal("tx", Pins("B17")),
        Subsignal("rx", Pins("A18")),
        IOStandard("LVCMOS33")
    ),
]

# 2. instantiate the bridge
from litex.soc.cores.uart import UARTWishboneBridge

self.submodules.bridge = UARTWishboneBridge(platform.request("serial",1), 100e6, baudrate=115200)
self.add_wb_master(self.bridge.wishbone)
```

In this case, the first argument are the pads, the second is the sys clock frequency, and the third is the baud rate of the serial port. Apparently only 115200 is well-tested. You can try higher baud rates but you might have some bit errors.

Here's an example of an Ethernet bridge:

```python
# 1. define the pins
_io += [
    # RMII PHY Pads
    ("rmii_eth_clocks", 0,
        Subsignal("ref_clk", Pins("D17"), IOStandard("LVCMOS33"))
    ),
    ("rmii_eth", 0,
        Subsignal("rst_n", Pins("F16"), IOStandard("LVCMOS33")),
        Subsignal("rx_data", Pins("A20 B18"), IOStandard("LVCMOS33")),
        Subsignal("crs_dv", Pins("C20"), IOStandard("LVCMOS33")),
        Subsignal("tx_en", Pins("A19"), IOStandard("LVCMOS33")),
        Subsignal("tx_data", Pins("C18 C19"), IOStandard("LVCMOS33")),
        Subsignal("mdc", Pins("F14"), IOStandard("LVCMOS33")),
        Subsignal("mdio", Pins("F13"), IOStandard("LVCMOS33")),
        Subsignal("rx_er", Pins("B20"), IOStandard("LVCMOS33")),
        Subsignal("int_n", Pins("D21"), IOStandard("LVCMOS33")),
    ),
]

# 2. instantiate the bridge
from liteeth.phy.rmii import LiteEthPHYRMII
from liteeth.core import LiteEthUDPIPCore
from liteeth.frontend.etherbone import LiteEthEtherbone

self.submodules.phy = phy = LiteEthPHYRMII(platform.request("rmii_eth_clocks"), platform.request("rmii_eth"))
mac_address = 0x1337320dbabe
ip_address="10.0.11.2"
self.submodules.core = LiteEthUDPIPCore(self.phy, mac_address, convert_ip(ip_address), int(100e6))
self.submodules.etherbone = LiteEthEtherbone(self.core.udp, 1234, mode="master")
self.add_wb_master(self.etherbone.wishbone.bus)
```

> **Caution**: Etherbone only works with a _direct_ network connection between the FPGA and the host. NAT traversal seems to be broken, so if you're using a VM to hold your litex build environment, try plugging a USB ethernet dongle in and associating that directly with your VM, so you don't have to traverse a NAT.

The code above puts the ethernet bridge into the `sys` domain, which defaults to 100MHz. Because the etherbone packet engine contains a full stack for unpacking and responding to packets, timing might be tough to close at 100MHz. Here's an example of how to instantiate a reduced-frequency bridge, which seems to work just as well as the above code but doesn't have the timing closure issues. This assumes that the `eth` domain is set at 50MHz. In this design, the master PLL was modified to add a 50 MHz tap driving a `BUFG` to create the `clk_eth` domain.

```python
from liteeth.phy.rmii import LiteEthPHYRMII
from liteeth.core import LiteEthUDPIPCore
from liteeth.frontend.etherbone import LiteEthEtherbone

phy = LiteEthPHYRMII(platform.request("rmii_eth_clocks"), platform.request("rmii_eth"))
phy = ClockDomainsRenamer("eth")(phy)
mac_address = 0x1337320dbabe
ip_address="10.0.11.2"
core = LiteEthUDPIPCore(phy, mac_address, convert_ip(ip_address), int(50e6), with_icmp=True)
core = ClockDomainsRenamer("eth")(core)
self.submodules += phy, core

etherbone_cd = ClockDomain("etherbone")
self.clock_domains += etherbone_cd
self.comb += [
    etherbone_cd.clk.eq(ClockSignal("sys")),
    etherbone_cd.rst.eq(ResetSignal("sys"))
]
self.submodules.etherbone = LiteEthEtherbone(core.udp, 1234, mode="master", cd="etherbone")
self.add_wb_master(self.etherbone.wishbone.bus)
```

There's no architectural reason why you can't have both a UART bridge and an etherbone bridge master in the same design. You could leave both in and just choose the interface you like to debug the chip.

However, the extra hardware and complication in the wishbone fabric can cause timing closure and resource consumption issues.

#### Litescope Host

OK, now you've got an analyzer and a bridge. How do you actually pull the data out? There is a helper program called `litex_server` which is meant to be run on your host -- either on the computer with the UART adapter, or the other side of the ethernet connection. `litex_server` can drive a multiplicity of bridge interfaces, as specified by command line arguments:

- `litex_server --udp --udp-ip 10.0.11.2 &` would start an ethernet server for the above example
- `litex_server --uart --uart-port /dev/ttyUSB0 --uart-baudrate 115200 &` would start a UART server, assuming an FTDI available on `/dev/ttyUSB0`

Once you've got the server running in the background, you can connect to it with a wishbone client program. For example, you can read not just the litescope ILA, but you can read out anything on the wishbone, such as the XADC if you have it instantiated in your SoC:

```python
#!/usr/bin/env python3
from litex.tools.litex_client import RemoteClient

wb = RemoteClient()
wb.open()

print("Temperature: ")
t = wb.read(0xe0005800)
t <<= 8
t |= wb.read(0xe0005804)
print(t * 503.975 / 4096 - 273.15, "C")

wb.close()
```

To read out the analyzer, you can use this script:

```python
from litex.tools.litex_client import RemoteClient
from litescope.software.driver.analyzer import LiteScopeAnalyzerDriver

wb = RemoteClient()
wb.open()

analyzer = LiteScopeAnalyzerDriver(wb.regs, "analyzer", debug=True)

analyzer.configure_subsampler(1)  ## increase this to "skip" cycles, e.g. subsample
analyzer.configure_group(0)

# trigger conditions will depend upon each other in sequence
analyzer.add_falling_edge_trigger("soc_videooverlaysoc_hdmi_in0_timing_payload_vsync")
analyzer.add_rising_edge_trigger("soc_videooverlaysoc_hdmi_in0_timing_payload_de")
analyzer.add_trigger(cond={"soc_videooverlaysoc_hdmi_in0_timing_payload_hsync" : 1}) 

analyzer.run(offset=32, length=128)  ### CHANGE THIS TO MATCH DEPTH
analyzer.wait_done()
analyzer.upload()
analyzer.save("dump.vcd")

wb.close()
```

Note that this assumes the files `analyzer.csv` and `csr.csv` are in the same directory. They are both kicked out by the Litex build environment, and `analyzer.csv` contains the fully specified names of the signals you're monitoring, which you should use to set trigger conditions.

The same analyzer wishbone readout script works regardless of the bridge interface you're using. The `litex_server` takes care of all of that.

Once you've got your `dump.vcd` file, you can view it with a program like `gtkwave`.

#### FSM Support

FSM support is relatively new as of July 2018. See this commit:

https://github.com/enjoy-digital/litescope/commit/bfd06f819ee20f7678bbfe96d03cc960fcbc97e8

Note that for FSM support to work, the FSM has to be explicitly named as a submodule so you can instantiate it in the analyzer section. In other words, this does not work:

```python
fsm = FSM()
self.submodules += fsm
```

Because in this case, there's no explicit name for the FSM in the submodules tree, and referring to the "fsm" element of the submodule won't resolve reliably. However, this works:

```python
fsm = FSM()
self.submodules.fsm = fsm
```

In this case, you can refer to the fsm by name because you've given it the name "fsm" in the submodule tree.

### Netlist

To be written: looking in `top.v` is often the fastest way to pick out subtle bugs in your Python code


## Reference

1. Lee, Yunsup, et al. "An agile approach to building RISC-V microprocessors." IEEE Micro 36.2 (2016): 8-20.