Image Pre-Processing Examples
====================================

The provided image processing examples show the general mechanisms of data handling for image processing using 3rd-party libraries. The OpenCV example provides data that is raw (mono) or demosaiced (color) and not further optimized for visual experience, while the LibArgus example leverages the discrete ISP (Image Signal Processor) inside the Jetson SoC to optimize image reproduction.

Argus Camera Example:
--------------------------

- Using hard ISP in NVIDIA Jetson SoCs, the most performant option for image preprocessing
- Only applicable for color sensors (color processing cannot be disabled)
- Most performant option
- Utilizes the libArgus closed-source library, with support and tuning on an individual basis through FRAMOS
- Example Implementation: Shows Demo Tuning per FSM Devkit

.. table:: ISP capabilities / limitations of NVIDIA Jetson Family
   :name: table-43
   :widths: auto

   +-------------------------------+----------------+----------------+----------------+
   |                               | Xavier          | Tegra X2       | Tegra X1      |
   |                               | (AGX, NX)       | (TX2, TX2 NX)  | (TX1, Nano)   |
   +===============================+================+================+================+
   | Performance                   |                |                |                |
   +-------------------------------+----------------+----------------+----------------+
   | Max. # of streams through ISP | 16             | 12             | 6              |
   +-------------------------------+----------------+----------------+----------------+
   | Pixel Bandwidth (max.)        | 2 Gpix/s       | 1.4 Gpix/s     | 1.4 Gpix/s     |
   +-------------------------------+----------------+----------------+----------------+
   | Image Resolution (max.)       | 64 MP          | 24 MP          | 24 MP          |
   +-------------------------------+----------------+----------------+----------------+
   | Image Width (max.)            | 6144 px        | 6144 px        | 6144 px        |
   +-------------------------------+----------------+----------------+----------------+

The software package provided with our FSM Devkits contains a functionally and performance-limited example configuration for the Jetson ISP. The configuration is sensor and lens-related and demonstrates the combination of our standard kit in environments illuminated with fluorescent light, such as in offices or laboratories.

Supported Features in Default Configuration
---------------------------------------------------

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

A fully featured calibration will be required to achieve the best performance and stable results, even in variable lighting conditions. As an NVIDIA camera partner, FRAMOS provides full ISP configurations for standard setups on request. Full custom calibration services considering lens and application-specific requirements for sophisticated applications are provided on a per-project basis.

**OpenCV Example:**
- Open software library
- Easy to use and large feature set
- Very resource-hungry (CPU)
- Not recommended for pre-processing
- Example Implementation: Demosaicing, Displaying

Due to limited performance and extreme resource utilization, the image pre-processing support utilizing the CPU will not be further enhanced. This does not affect users of OpenCV for their purposes.
