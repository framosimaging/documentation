FSA Datasheets
==============================

The FRAMOS Sensor Adapter (FSA) datasheets provide comprehensive technical information and specifications for different FSA models, which are integral components of the FRAMOS sensor ecosystem. These datasheets cover various FSA models designed to support different sensor module configurations and data output types, including Sub-LVDS, SLVS, SLVS-EC, and MIPI CSI-2 (D-PHY). The datasheets are structured to provide details on setup configurations, functional blocks, interface descriptions, pinout tables, and technical drawings.

Overview of FSA Models
----------------------

The FSA models cater to different sensor technologies and data output requirements, ensuring compatibility and optimal performance in various imaging applications. Below is an overview and differentiation of the FSA models discussed in the provided datasheets:

1. **FSA-FTx/A**
   - **Purpose**: Designed for sensor modules with native MIPI CSI-2 data output. It supports seamless connectivity between FSMs and the target processor board via the FPA.
   - **Key Features**:
     - Supports single or multiple sensor setups.
     - Handles voltage generation, power-up sequencing, and reference clock generation.
     - Reduces noise and heat generation by shifting power functions to the FSA.
   - **Functional Blocks**: Signal routing, voltage generation, power-up sequencing, driving frequency generation, and EEPROM for configuration/ID.

2. **FSA-FTx/A-00G**
   - **Purpose**: Targets Sub-LVDS, SLVS, and SLVS-EC sensor modules requiring data conversion to MIPI CSI-2. It provides flexibility for different sensor output types and data chains.
   - **Key Features**:
     - Converts Sub-LVDS and SLVS data outputs to MIPI CSI-2 format.
     - Offers native data streaming options.
     - Each FSA variant is tailored to specific FSMs, ensuring compatibility and optimal data handling.
   - **Functional Blocks**: Signal routing, voltage generation, power-up sequencing, master clock and slave timing generation, and image data conversion.

3. **FSA-FTx/BC**
   - **Purpose**: Ideal for applications requiring pure Sub-LVDS, SLVS, or SLVS-EC data output without conversion to MIPI CSI-2. This FSA model is designed for high-speed data transmission without data format changes.
   - **Key Features**:
     - Supports pure data chains without conversion.
     - Maintains compatibility with Sub-LVDS, SLVS, and SLVS-EC sensor setups.
     - Suitable for use cases where direct sensor-to-processor communication is required.
   - **Functional Blocks**: Signal routing, voltage generation for image sensors, and power-up sequencing.

Differentiation Between FSA Models
----------------------------------

The FSA models differ primarily in their target applications and data handling capabilities:

- **Data Conversion vs. Native Streaming**: 
  - The **FSA-FTx/A** is designed for direct MIPI CSI-2 output, while the **FSA-FTx/A-00G** offers data conversion from Sub-LVDS and SLVS to MIPI CSI-2, providing flexibility for different data output requirements.
  - The **FSA-FTx/BC**, on the other hand, does not perform any data conversion and is suited for applications where maintaining the native data output format (Sub-LVDS, SLVS, SLVS-EC) is critical.

- **Sensor Compatibility**: 
  - Each FSA model supports specific sensor technologies and data outputs. The **FSA-FTx/A** is primarily for FSMs with native MIPI CSI-2 outputs, while the **FSA-FTx/A-00G** and **FSA-FTx/BC** cater to sensors with Sub-LVDS, SLVS, and SLVS-EC outputs.

- **System Configuration**:
  - The **FSA-FTx/A** and **FSA-FTx/A-00G** models can be configured for multiple sensor setups, while the **FSA-FTx/BC** focuses on pure data transmission without conversion.

Conclusion
----------

The FSA datasheets provide critical information for selecting the right FRAMOS Sensor Adapter based on the specific requirements of your imaging application. By understanding the capabilities and differences of each FSA model, users can ensure optimal integration and performance within their sensor ecosystems. For detailed technical specifications, configurations, and interface descriptions, please refer to the respective FSA datasheets provided above.



.. toctree::
   :maxdepth: 2
   :hidden:

   FSAFTxA.rst
   FSAFTxA00G.rst
   FSAFTxBC.rst
  
