## Why Chip Copliot?

**Build a 100% Python-based SoC Design environment!** Chip-Copilot seeks for new agile Chip/SoC design methodologies, collaboration approaches and creation of reusable IPs and subsystems. 

**Trend #1**: Python-embedded DSLs are increasingly being used to improve the productivity of hardware design and verification.

**Trend #2**: LLMs are increasingly being used to improve the productivity of hardware design and verification.

There has been also an effort to establish principles and practices for agile Chip/SoC development by UC Berkeley [1] (2016). Their proposal **Agile Hardware Manifesto** includes the following four principles: 

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

## What methods and practices to increase agility of Chip/SoC development?
 
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

## Main Goals of Chip/SoC Copilot

The main focus of Chip/SoC Copilot is on large and complex SoCs in which integration expertise is essential. The main goals are：
1) creation of a versatile Chip/SoC template
2) development of agile Chip/SoC development design process

The problem for automating the whole process of designing an Chip/SoC:
1) Attaining a comprehensive description methodology to represent any potential IP adequately
2) Circumscribing how the connections between the different IPs, buses, and masters are amply described
3) Parsing the representation and generating the proper format and connections of all the Verilog modules that make up the SoC
4) Adhering to an acceptable runtime period to fulfill the purposes of the automation process and render it attractive to designers. Thus, the efficiency of the process is critical, and its maintenance is inevitable to keep the project updated with the most modern technologies
5) Usability and achieving the no-man-in-the-loop goal, while ensuring the accessibility of all the files and generated outputs of the intermediate stages of the process to the designers to discern and reform
6) Avoiding huge compromises in the quality of the work produced, if compared with a fully manual design process. Hence, we articulate our project’s objectives as versatility, usability, extensibility, reliability, competence,and efficiency

## Chip/SoC Copilot：Reuse，Modularize，Automate

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

## What is Chip/SoC Copliot?

The Chip/SoC Copilot framework provides a convenient and efficient infrastructure to create and maintain SoC Platform.The SoC is generated using a custom generator written in Python [migen](https://www.controlpaths.com/2022/11/07/writing-verilog-code-using-python-with-migen/), which pulls together the CPU, peripherals, PAD, clock/reset tree, and creates the address mapping and the platform-support files needed to compile software for the core.

> How to Agile SoC：
> * 100% Python
> * Generator not module 
> * Just instance HDL Module and interconnect
