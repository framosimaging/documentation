# Functional Adapter (FFA)

FRAMOS Functional Adapters (FFAs) extend the capabilities of the FSM Ecosystem by providing additional functionalities through PixelMate™ interfaces on both input and output. These adapters can perform various roles, such as image pre-processing or interface adaptation, thereby enabling high-performance vision applications across different platforms. The FFA series ensures robust connectivity, signal management, and flexibility for diverse application needs, including industrial automation and advanced driver-assistance systems (ADAS).

![FFA-1](FFA-1.png)

**Figure 10: Block Diagram of components in MIPI CSI-2 chain with optional FFA on top FSM chain.

As an example, Figure 10 shows the block diagram of two FSMs connected
to a processor board with their appropriate adapters (FSA, FPA). In the
lower chain (#2), the FSM+FSA combination is directly connected to the
FPA via the generalized PixelMate™ connector. In the upper chain (#1)
contains an FFA (pair) with PixelMate™ in- and output. This FFA can be a
single PCB performing i.e. image pre-processing, as well as a pair of
boards acting as interface adapters, converting the interface completely
(SerDes) or partially (connector/cable type) back and forth.

## Key Features

- **Seamless Integration**: PixelMate™ interfaces on both input and output ensure smooth integration into existing FSM chains.
- **Versatile Functionality**: FFAs can perform a range of tasks from simple signal conversion to complex image pre-processing.
- **High-Speed Data Transfer**: Supports high-speed data transfer rates up to 12 Gbps, suitable for uncompressed video data, I2C communication, GPIOs, and power delivery.
- **Robust Design**: Includes test points for critical signals and offers various configurations to support different sensor and processor board requirements.
- **Enhanced Signal Management**: Provides signal level translation, power conversion, and additional sensor control through I2C access.

## Getting Started

To begin, navigate to the specific FFA model documentation relevant to your project. Each section provides in-depth technical details, ensuring you have the necessary information to fully leverage the potential of FRAMOS Functional Adapters.

Thank you for choosing FRAMOS Functional Adapters. We are dedicated to supporting your vision system development with robust, high-performance solutions. For any additional assistance, please refer to our support section or contact our technical support team.

```{toctree}
:maxdepth: 2
:hidden:

FFA-GMSL-SerDes.rst
FFA-MC.rst
FFA-FFC.rst
```