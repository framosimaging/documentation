Software
============

Introduction
--------------------

At FRAMOS, we know the challenge of getting started with new technology. The idea behind the Software Package is to allow embedded software engineers quick access to a streaming system and to provide the required tools to extend and adapt it according to their application needs and use.

What the software package and driver are:

- A reference for a custom sensor implementation
- Demonstrating how to use the required interfaces
- Demonstrating how to communicate with the image sensor
- Demonstrating how to generally initialize and configure the image sensor
- Provide initial image streaming output to the user space
- Demonstrating how to run basic image processing on pixel data

**Supported Processor Platforms**

The table below shows which platforms are supported by the standard driver package, and how many FSMs can at maximum be operated in parallel.


Sensor Module Compatibility Table
=================================

+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| **Sensor Module** | **NVIDIA Jetson  | **NVIDIA AGX Xavier /    | **NVIDIA Jetson Nano, TX2 NX,    | **DragonBoard**   | **96Boards Consumer Edition / Xilinx Development Boards** |
|                   | TX2**            | AGX Orin**               | Xavier NX**                      | **410c**          |                                                           |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-AR0144        | 4                |                          | 2                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-AR0521        | 4                |                          | 2                                | 2                 | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-AR1335        | 4                |                          | 2                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-HDP230        | 4                | 4                        | 2                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX264        | 2                | 4                        | -                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX283        | 2                | 4                        | -                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX290        | 4                |                          | 2                                | 2                 | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX296        | 4                |                          | 2                                | 2                 | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX297        | 4                |                          | 2                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX304        | 2                | 4                        | -                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX327        | 4                |                          | 2                                | 2                 | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX334        | 2                | 4                        | -                                | 2                 | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX335        | 4                |                          | 2                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX412        | 4                |                          | 2                                | 2                 | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX415        | 4                |                          |                                  |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX462, 662   | 4                |                          |                                  |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX464        | 4                |                          |                                  |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX477        | 4                |                          |                                  |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX485, 585   | 4                |                          |                                  |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX565, 568   | 4                |                          | 2                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX577        | 4                |                          | 2                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX675        | 4                |                          | 2                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX678        | 4                |                          | 2                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX715        | 4                |                          | 2                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+
| FSM-IMX530        | 2                | 4                        | -                                |                   | HW only, driver development on project basis              |
+-------------------+------------------+--------------------------+----------------------------------+-------------------+-----------------------------------------------------------+


NVIDIA Jetson Family
---------------------------

The software package provided with the Development Kits of the FRAMOS Sensor Module Ecosystem for NVIDIA Jetson platforms provides a reference implementation of sensor and device drivers for MIPI CSI-2. It contains a minimum feature set demonstrating how to utilize the platform-specific data interface and communication implementation, as well as the initialization of the image sensor and implementation of basic features.

a. Package Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Platform and device drivers with Linux for Tegra Support
- V4L2 based subdevice drivers (low-level C API)
- Streamlined V4L2 library (LibSV) providing generic C/C++ API
- Display Examples:

  - OpenCV (Software)
  - LibArgus (Hardware)

b. Supported Devices
~~~~~~~~~~~~~~~~~~~~~~

- NVIDIA Jetson Nano Developer Kit (B01)
- NVIDIA Jetson TX2 Developer Kit
- NVIDIA Jetson TX2 NX Developer Kit
- NVIDIA Jetson Xavier NX Developer Kit
- NVIDIA Jetson Orin NX SoM with carrier Jetson Nano Developer Kit
- NVIDIA Jetson AGX Xavier and AGX Orin Developer Kit


Platform and Sensor Device Drivers
------------------------------------------

The driver divides into two main parts that are configured in separate ways – the image modes and the general features of the image sensor.

a. Image Modes
~~~~~~~~~~~~~~

These are major attributes that impact the image data stream formatting. They require a static pre-configuration within the device tree (DT):

- Image / streaming resolution
- Pixel format / bit depth
- Data rate / lane configuration

Each driver provides access to 3 – 5 pre-built configurations, reflecting the main operation modes of the imager. Besides the full resolution, which is always available, they allow receiving image streams in common video resolutions like VGA, Full HD, and UHD as supported or as make sense by the imagers, and utilize sensor features like ROI and binning.

These configurations act as examples for implementation and are available as source code. Due to the size limitation of the device tree, it is not possible to integrate an extensive set of options.


b. General Features
~~~~~~~~~~~~~~~~~~~~~

These are attributes of the image sensor that do not manipulate the data stream formatting. The drivers provided with the Software Pack integrate the sensor features as shown in the table below.


Legend:

- ✔ : V4L (libsv) and libargus
- ▲ : V4L (libsv)
- ✖ : Not Supported/Implemented

.. table:: Supported sensor features on NVIDIA Jetson Family
   :name: table-42
   :widths: auto

   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | Pre-Implemented| Gain           | Frame Rate     | Exposure Time  | Flip/Mirror    | IS Mode        | Sensor Mode ID | Test Pattern   | Black Level    | HDR Output     | Broadcast      | Data Rate      | Synchronizing  |                |
   | Features per   | (Analog /      |                |                |                | (Master /      |                | Output         |                |                |                |                | Master         |                |
   | Model          | Digital)       |                |                |                | Slave)         |                |                |                |                |                |                |                |                |
   +================+================+================+================+================+================+================+================+================+================+================+================+================+================+
   | FSM-AR0144     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-AR0521     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-AR1335     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-HDP230     | ✔              | ✔              | ✔              | ✔              | ▲              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX264     | ✔              | ✔              | ✔              | ✔              | ▲              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX283     | ✔              | ✔              | ✔              | ✔              | ▲              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX290     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX296     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX297     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX304     | ✔              | ✔              | ✔              | ✔              | ▲              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX327     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX334     | ✔              | ✔              | ✔              | ✔              | ▲              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX335     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX412     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX415     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX462     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX464     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX477     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX485     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX530     | ✔              | ✔              | ✔              | ✔              | ▲              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX565,568 | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX577     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX675     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX678     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+
   | FSM-IMX715     | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✔              | ✖              | ✖              | ✖              | ✖              | ✖              | ✖              |
   +----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+----------------+



Further features, as they are supported by the image sensor, can be integrated into the driver sources using the image sensor datasheet.


Image Pre-Processing Examples
-----------------------------------------

The provided image processing examples show the general mechanisms of data handling for image processing using 3rd-party libraries. The OpenCV example provides data that is raw (mono) or demosaiced (color) and not further optimized for visual experience, while the LibArgus example leverages the discrete ISP (Image Signal Processor) inside the Jetson SoC to optimize image reproduction.

a. Argus Camera Example:
~~~~~~~~~~~~~~~~~~~~~~~~

- Using hard ISP in NVIDIA Jetson SoCs, the most performant option for image preprocessing
- Only applicable for color sensors (color processing cannot be disabled)
- Most performant option
- Utilizes the libArgus closed-source library, with support and tuning on an individual basis through FRAMOS
- Example Implementation: Shows Demo Tuning per FSM Devkit

.. table:: ISP capabilities / limitations of NVIDIA Jetson Family
   :name: table-43
   :widths: auto

   +-------------------------------+-----------------+----------------+----------------+
   |                               | Xavier          | Tegra X2       | Tegra X1       |
   |                               | (AGX, NX)       | (TX2, TX2 NX)  | (TX1, Nano)    |
   +===============================+=================+================+================+
   | Performance                   |                 |                |                |
   +-------------------------------+-----------------+----------------+----------------+
   | Max. # of streams through ISP | 16              | 12             | 6              |
   +-------------------------------+-----------------+----------------+----------------+
   | Pixel Bandwidth (max.)        | 2 Gpix/s        | 1.4 Gpix/s     | 1.4 Gpix/s     |
   +-------------------------------+-----------------+----------------+----------------+
   | Image Resolution (max.)       | 64 MP           | 24 MP          | 24 MP          |
   +-------------------------------+-----------------+----------------+----------------+
   | Image Width (max.)            | 6144 px         | 6144 px        | 6144 px        |
   +-------------------------------+-----------------+----------------+----------------+

The software package provided with our FSM Devkits contains a functionally and performance-limited example configuration for the Jetson ISP. The configuration is sensor and lens-related and demonstrates the combination of our standard kit in environments illuminated with fluorescent light, such as in offices or laboratories.

b. Supported Features in Default Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. table:: Default tuning of NVIDIA Jetson, supplied with FSM Devkits
   :name: table-20
   :widths: auto

   +-------------------------------------------+-----------------------------------------+
   | Feature                                   | Supported Configuration                 |
   +===========================================+=========================================+
   | Lens Considered (Type)                    | Yes (Devkit Lens)                       |
   +-------------------------------------------+-----------------------------------------+
   | IR Cut Filter (Type)                      | Yes (650nm/50%)                         |
   +-------------------------------------------+-----------------------------------------+
   | Sensor Configuration                      | Driver Default                          |
   +-------------------------------------------+-----------------------------------------+
   | Demosaic                                  | Yes                                     |
   +-------------------------------------------+-----------------------------------------+
   | Black Level Compensation                  | Yes (Calibrated)                        |
   +-------------------------------------------+-----------------------------------------+
   | Bad Pixel Correction                      | Yes (Calibrated)                        |
   +-------------------------------------------+-----------------------------------------+
   | Color Correction                          | Yes (Calibrated)                        |
   +-------------------------------------------+-----------------------------------------+
   | Auto White Balance (A, TL84, D65)         | Limited (Calibrated for TL84 only)      |
   +-------------------------------------------+-----------------------------------------+
   | Manual White Balancing                    | Limited (Not Calibrated)                |
   +-------------------------------------------+-----------------------------------------+
   | Lens Shading / Falloff Correction         | Limited (Calibrated for Devkit lens)    |
   +-------------------------------------------+-----------------------------------------+
   | Noise Reduction                           | Limited (Not Calibrated)                |
   +-------------------------------------------+-----------------------------------------+
   | Sharpening                                | Limited (Not Calibrated)                |
   +-------------------------------------------+-----------------------------------------+
   | Auto Exposure, Gain, Gamma, Color/Tone,   | Requires Application Specific Tuning    |
   | Contrast Tuning                           |                                         |
   +-------------------------------------------+-----------------------------------------+

**Note**: Demosaicing is always active and can’t be disabled. For monochrome sensors refer to libSV to bypass the ISP.

A fully featured calibration will be required to achieve the best performance and stable results, even in variable lighting conditions. As an NVIDIA camera partner, FRAMOS provides full ISP configurations for standard setups on request. Full custom calibration services considering lens and application-specific requirements for sophisticated applications are provided on a per-project basis.

c. OpenCV Example:
~~~~~~~~~~~~~~~~~~~~~~

- Open software library
- Easy to use and large feature set
- Very resource-hungry (CPU)
- Not recommended for pre-processing
- Example Implementation: Demosaicing, Displaying

Due to limited performance and extreme resource utilization, the image pre-processing support utilizing the CPU will not be further enhanced. This does not affect users of OpenCV for their purposes.
