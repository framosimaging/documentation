Introduction
++++++++++++

Introduction
~~~~~~~~~~~~~~~

The FRAMOS Sensor Modules are printed circuit boards, interfacing
various types of image sensors with standardized connectivity like
connector type, pinout, mechanical format and compatible accessories.
The goal of this is to provide various sensor boards that can be used
“off the shelf” to connect a variety of image sensors to a host system.
Starting from evaluation and proof-of-concept, but also in mass
production where adjustments to actual needs are easily possible.

The following chapter provides information on the generic attributes as
well as the individual modules, in addition to the individual FSM
datasheets.

Common Specification

In general, FSMs are differentiated by two main attributes:

-  Image sensor size dependent mechanical footprint (26.5 mm, 28 mm)

-  Data interface type specific pinout (MIPI CSI-2, LVDS)

All image sensor signals are routed directly from sensor to the 60-pin
connector. All passives visible on the PCB decouple the various power
loads of the image sensor. Please refer to the appropriate image sensor
documentation for further information.

Portfolio Overview of Sensor Modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The portfolio of sensor modules includes several FSMs, which are listed
with their main attributes on the following pages:

-  Native MIPI CSI-2 Modules – Global Shutters

-  Native MIPI CSI-2 Modules – Rolling Shutters

-  Sub-LVDS, SLVS and SLVS-EC Modules

These attributes describe the individual FSMs without any additional
hardware like FSA or FPA. They are defined by the integration of the
bare image sensor and are not manipulated or preprocessed in any way.

Native MIPI CSI-2 Modules
---------------------------------

**Global Shutters**

+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Model Name     | FSM-IMX297   | FSM-AR0144   | FSM-IMX296   | FSM-HDP230   | FSM-IMX568   | FSM-IMX565   |
+================+==============+==============+==============+==============+==============+==============+
| Shutter Type   | CMOS         | CMOS         | CMOS         | CMOS         | CMOS         | CMOS         |
|                | Global       | Global       | Global       | Global       | Global       | Global       |
|                | Shutter      | Shutter      | Shutter      | Shutter      | Shutter      | Shutter      |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Technology     | Pregius      | -            | Pregius      | -            | Pregius S    | Pregius S    |
|                | (Gen 2)(Bin) |              | (Gen2)       |              | (Gen4)       | (Gen4)       |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Resolution     | 0.4          | 1            | 1.6          | 2.3          | 5.1          | 12.3         |
| [MP]           |              |              |              |              |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Resolution     | 728 x 544    | 1280 x 800   | 1456 x 1088  | 1944 x 1204  | 2472 x 2064  | 4128 x 3008  |
| [HxV]          |              |              |              |              |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Max. Framerate | 120.9 FPS    | 60.3 FPS     | 60.4 FPS     | 59.9 FPS     | 96.2 FPS     | 42.6 FPS     |
| [FPS]          | (1-Lane)     | (2-Lane)     | (1-Lane)     | (4-Lane)     | (4-Lane)     | (4-Lane)     |
|                |              |              |              | 59.9 FPS     | 51.7 FPS     | 22.3 FPS     |
|                |              |              |              | (2-Lane)     | (2-Lane)     | (2-Lane)     |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Mono / Color   | Mono         | Color / Mono | Mono         | Color / Mono | Color / Mono | Color / Mono |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Sensor         | Sony         | onsemi       | Sony         | Pyxalis      | Sony         | Sony         |
| Manufacturer   |              |              |              |              |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Sensor Name    | IMX297LLR    | AR0144CSSM   | IMX296LLR    | HDPYX230-G   | IMX568AAMJ-M | IMX565AAMJ-C |
|                | /            | /            | /            | Mono /       | /            | /            |
|                | IMX297LQR    | AR0144CSSC   | IMX296LQR    | HDPYX230-G   | IMX568AAQJ-C | IMX565AAQJ-C |
|                |              |              |              | RGB          |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Application /  | Sensing      | Industrial   | Sensing      | Automotive   | Industrial   | Industrial   |
| Grade          |              |              |              |              |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Optical Format | 1/2.9        | 1/4          | 1/2.9        | 1/2.5        | 1/1.8        | 1/1.1        |
| [inch]         |              |              |              |              |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Pixel Size     | 6.9 x 6.9    | 3 x 3        | 3.45 x 3.45  | 3.2 x 3.2    | 2.74 x 2.74  | 2.74 x 2.74  |
| [µm]           |              |              |              |              |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Pixel Bitdepth | 10 bit       | 10 / 12 bit  | 10 bit       | 8 / 10 / 12  | 8 / 10 / 12  | 8 / 10 / 12  |
| [bit]          |              |              |              | / 14 / 16    | bit          | bit          |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Data Interface | MIPI CSI-2   | MIPI CSI-2   | MIPI CSI-2   | MIPI CSI-2   | MIPI CSI-2   | MIPI CSI-2   |
| [Type]         |              |              |              |              |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Data Interface | 1            | 1 / 2        | 1            | 2 / 4        | 2 / 4        | 2 / 4        |
| [# Lanes]      |              |              |              |              |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Communication  | I²C (4-wire  | I²C          | I²C (4-wire  | I²C          | I²C          | I²C          |
| Interface      | serial)      |              | serial)      |              |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Drive Frequency| 37.125 /     | 6 to 48      | 37.125 /     | 6 to 27      | 37.125 / 54 /| 37.125 / 54 /|
| [MHz]          | 74.25 / 54   |              | 74.25 / 54   |              | 74.25        | 74.25        |
|                |              |              |              |              |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Input Voltages | 1.2V, 1.8V,  | 1.2V, 1.8V,  | 1.2V, 1.8V,  | 1.2V, 1.8V,  | 1.1V, 1.8V,  | 1.1V, 1.8V,  |
|                | 3.3V         | 2.8V         | 3.3V         | 2.8V         | 2.9V, 3.3V   | 2.9V, 3.3V   |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Supported Lens | M12 or       | M12 or       | M12 or       | M12 or       | M12 or       | C/CS-Mount   |
| Mounts         | C/CS-Mount   | C/CS-Mount   | C/CS-Mount   | C/CS-Mount   | C/CS-Mount   | option       |
|                | options      | options      | options      | options      | options      |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+
| Board          | 26.5 mm x    | 26.5 mm x    | 26.5 mm x    | 26.5 mm x    | 26.5 mm x    | 26.5 mm x    |
| Dimensions     | 26.5 mm      | 26.5 mm      | 26.5 mm      | 26.5 mm      | 26.5 mm      | 26.5 mm      |
| [mm²]          |              |              |              |              |              |              |
+----------------+--------------+--------------+--------------+--------------+--------------+--------------+


**Rolling Shutters (Part 1/4) – up to 5 MP**

+------------------+-------------+-------------+-------------+-------------+
| Model Name       | FSM-IMX290  | FSM-IMX327  | FSM-IMX462  | FSM-IMX662  |
+==================+=============+=============+=============+=============+
| Shutter Type     | CMOS        | CMOS        | CMOS        | CMOS        |
|                  | Rolling     | Rolling     | Rolling     | Rolling     |
|                  | Shutter     | Shutter     | Shutter     | Shutter     |
+------------------+-------------+-------------+-------------+-------------+
| Technology       | Starvis     | Starvis     | Starvis +   | Starvis2    |
|                  |             |             | NIR         |             |
+------------------+-------------+-------------+-------------+-------------+
| Resolution       | 2.1         | 2.1         | 2.1         | 2.1         |
| [MP]             |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Resolution       | 1920 x      | 1920 x      | 1920 x      | 1920 x      |
| [HxV]            | 1080        | 1080        | 1080        | 1080        |
+------------------+-------------+-------------+-------------+-------------+
| Max. Framerate   | 120 FPS     | 60 FPS      | 120 FPS     | 97.8 FPS    |
| [FPS]            | (4-Lane)    | (4-Lane)    | (4-Lane)    | (4-Lane)    |
|                  | 60 FPS      | 60 FPS      | 60 FPS      | 97.8 FPS    |
|                  | (2-Lane)    | (2-Lane)    | (2-Lane)    | (2-Lane)    |
+------------------+-------------+-------------+-------------+-------------+
| Mono / Color     | Color       | Color       | Mono        | Color       |
+------------------+-------------+-------------+-------------+-------------+
| Sensor           | Sony        | Sony        | Sony        | Sony        |
| Manufacturer     |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Sensor Name      | IMX290LLR   | IMX327LQR1  | IMX462LQR-C | IMX662AAQR-C|
|                  | /           |             |             |             |
|                  | IMX290LQR   |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Application /    | Security    | Security    | Security    | Security    |
| Grade            |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Optical Format   | 1/2.8       | 1/2.8       | 1/2.8       | 1/2.8       |
| [inch]           |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Pixel Size       | 2.9 x 2.9   | 2.9 x 2.9   | 2.9 x 2.9   | 2.9 x 2.9   |
| [µm]             |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Pixel Bitdepth   | 10 / 12 bit | 10 / 12 bit | 10 / 12 bit | 10 / 12 bit |
| [bit]            |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Data Interface   | MIPI CSI-2  | MIPI CSI-2  | MIPI CSI-2  | MIPI CSI-2  |
| [Type]           |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Data Interface   | 2 / 4       | 2 / 4       | 2 / 4       | 2 / 4       |
| [# Lanes]        |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Communication    | I²C         | I²C         | I²C         | I²C         |
| Interface        |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Drive Frequency  | 37.125 /    | 37.125 /    | 37.125 /    | 24 / 27 /   |
| [MHz]            | 74.25       | 74.25       | 74.25       | 37.125 /    |
|                  |             |             |             | 74.25       |
+------------------+-------------+-------------+-------------+-------------+
| Input Voltages   | 1.2V,       | 1.2V,       | 1.2V,       | 1.1V,       |
|                  | 1.8V, 2.9V  | 1.8V, 2.9V  | 1.8V, 2.9V  | 1.8V, 3.3V  |
+------------------+-------------+-------------+-------------+-------------+
| Supported Lens   | M12 or      | M12 or      | M12 or      | M12 or      |
| Mounts           | C/CS-Mount  | C/CS-Mount  | C/CS-Mount  | C/CS-Mount  |
|                  | options     | options     | options     | options     |
+------------------+-------------+-------------+-------------+-------------+
| Board Dimensions | 26.5 x      | 26.5 x      | 26.5 x      | 26.5 x      |
| [mm²]            | 26.5        | 26.5        | 26.5        | 26.5        |
|                  |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+


**Rolling Shutters (Part 2/4) – up to 5 MP**

+------------------+-------------+-------------+-------------+-------------+
| Model Name       | FSM-IMX464  | FSM-IMX335  | FSM-AR0521  | FSM-IMX675  |
+==================+=============+=============+=============+=============+
| Shutter Type     | CMOS        | CMOS        | CMOS        | CMOS        |
|                  | Rolling     | Rolling     | Rolling     | Rolling     |
|                  | Shutter     | Shutter     | Shutter     | Shutter     |
+------------------+-------------+-------------+-------------+-------------+
| Technology       | Starvis +   | Starvis     | -           | Starvis2    |
|                  | NIR         |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Resolution       | 4.2         | 5           | 5           | 5           |
| [MP]             |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Resolution       | 2712 x      | 2616 x      | 2592 x      | 2592 x      |
| [HxV]            | 1538        | 1964        | 1944        | 1944        |
+------------------+-------------+-------------+-------------+-------------+
| Max. Framerate   | 90 FPS      | 60 FPS      | 69 FPS      | 80 FPS      |
| [FPS]            | (4-Lane)    | (4-Lane)    | (4-Lane)    | (4-Lane)    |
|                  | 30 FPS      | 30 FPS      | 34 FPS      | 60 FPS      |
|                  | (2-Lane)    | (2-Lane)    | (2-Lane)    | (2-Lane)    |
+------------------+-------------+-------------+-------------+-------------+
| Mono / Color     | Color /     | Color /     | Color /     | Color       |
|                  | Mono        | Mono        | Mono        |             |
+------------------+-------------+-------------+-------------+-------------+
| Sensor           | Sony        | Sony        | onsemi      | Sony        |
| Manufacturer     |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Sensor Name      | IMX464LQR-C | IMX335LLN   | AR0521SR2M  | IMX675AAQR  |
|                  | /           | /           | /           |             |
|                  | IMX464LQR   | IMX335LQN   | AR0521SR2C  |             |
+------------------+-------------+-------------+-------------+-------------+
| Application /    | Security    | Security    |             | Security    |
| Grade            |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Optical Format   | 1/1.8       | 1/2.8       | 1/2.5       | 1/2.8       |
| [inch]           |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Pixel Size       | 2.9 x 2.9   | 2 x 2       | 2.2 x 2.2   | 2 x 2       |
| [µm]             |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Pixel Bitdepth   | 10 / 12 bit | 10 / 12 bit | 8 / 10 /    | 10 / 12 bit |
| [bit]            |             |             | 12 bit      |             |
+------------------+-------------+-------------+-------------+-------------+
| Data Interface   | MIPI CSI-2  | MIPI CSI-2  | MIPI CSI-2  | MIPI CSI-2  |
| [Type]           |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Data Interface   | 2 / 4       | 2 / 4       | 2 / 4       | 2 / 4       |
| [# Lanes]        |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Communication    | I²C         | I²C         | I²C         | I²C         |
| Interface        |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+
| Drive Frequency  | 6 to 27 /   | 6 - 27 /    | 10 to 48    | 24 / 27 /   |
| [MHz]            | 37.125 /    | 37.125 /    |             | 37.125 /    |
|                  | 74.25       | 74.25       |             | 72 / 74.25  |
+------------------+-------------+-------------+-------------+-------------+
| Input Voltages   | 1.2V,       | 1.2V,       | 1.2V,       | 1.1V,       |
|                  | 1.8V, 2.9V  | 1.8V, 2.9V  | 1.8V, 2.7V  | 1.8V, 3.3V  |
+------------------+-------------+-------------+-------------+-------------+
| Supported Lens   | M12 or      | M12 or      | M12 or      | M12 or      |
| Mounts           | C/CS-Mount  | C/CS-Mount  | C/CS-Mount  | C/CS-Mount  |
|                  | options     | options     | options     | options     |
+------------------+-------------+-------------+-------------+-------------+
| Board Dimensions | 26.5 x      | 26.5 x      | 26.5 x      | 26.5 x      |
| [mm²]            | 26.5        | 26.5        | 26.5        | 26.5        |
|                  |             |             |             |             |
+------------------+-------------+-------------+-------------+-------------+


**Rolling Shutters (Part 3/4) – 8 MP**

+----------------+------------+------------+------------+------------+------------+------------+
| Model          | FSM-       | FSM-       | FSM-       | FSM-       | FSM-       | FSM-       |
| Name           | IMX334     | IMX485     | IMX585     | IMX678     | IMX415     | IMX715     |
+================+============+============+============+============+============+============+
| Shutter        | CMOS       | CMOS       | CMOS       | CMOS       | CMOS       | CMOS       |
| Type           | Rolling    | Rolling    | Rolling    | Rolling    | Rolling    | Rolling    |
|                | Shutter    | Shutter    | Shutter    | Shutter    | Shutter    | Shutter    |
+----------------+------------+------------+------------+------------+------------+------------+
| Technology     | Starvis    | Starvis    | Starvis    | Starvis    | Starvis    | Starvis    |
|                |            | + NIR      |            |            | + NIR      | + NIR      |
+----------------+------------+------------+------------+------------+------------+------------+
| Resolution     | 8.3        | 8.3        | 8.3        | 8.3        | 8.4        | 8.4        |
| [MP]           |            |            |            |            |            |            |
+----------------+------------+------------+------------+------------+------------+------------+
| Resolution     | 3864 x     | 3864 x     | 3856 x     | 3856 x     | 3864 x     | 3864 x     |
| [HxV]          | 2180       | 2180       | 2180       | 2180       | 2192       | 2192       |
+----------------+------------+------------+------------+------------+------------+------------+
| Max.           | 60 FPS     | 72 FPS     | 90.1       | 72 FPS     | 90 FPS     | 90 FPS     |
| Framerate      | (4-Lane)   | (4-Lane)   | (4-Lane)   | (4-Lane)   | (4-Lane)   | (4-Lane)   |
| [FPS]          |            |            |            |            |            |            |
|                | 38 FPS     | 30 FPS     | 44 FPS     | 30 FPS     | 44 FPS     | 44 FPS     |
|                | (2-Lane)   | (2-Lane)   | (2-Lane)   | (2-Lane)   | (2-Lane)   | (2-Lane)   |
+----------------+------------+------------+------------+------------+------------+------------+
| Mono /         | Color      | Color      | Color      | Color      | Color      | Color      |
| Color          | / Mono     | / Mono     | / Mono     | / Mono     | / Mono     | / Mono     |
+----------------+------------+------------+------------+------------+------------+------------+
| Sensor         | Sony       | Sony       | Sony       | Sony       | Sony       | Sony       |
| Manufacturer   |            |            |            |            |            |            |
+----------------+------------+------------+------------+------------+------------+------------+
| Sensor         | IMX        | IMX        | IMX        | IMX        | IMX        | IMX        |
| Name           | 334LLR     | 485LQJ     | 585A       | 678        | 415        | 715        |
|                | /          |            | AQJ1-C     | AAQR1      | AAQR       | AAQR1      |
|                | IMX        |            |            |            |            |            |
|                | 334LQR     |            |            |            |            |            |
+----------------+------------+------------+------------+------------+------------+------------+
| Application    | Security   | Security   | Security   | Security   | Security   | Security   |
| / Grade        |            |            |            |            |            |            |
+----------------+------------+------------+------------+------------+------------+------------+
| Optical        | 1/1.8      | 1/1.2      | 1/1.2      | 1/1.8      | 1/2.8      | 1/2.8      |
| Format         |            |            |            |            |            |            |
| [inch]         |            |            |            |            |            |            |
+----------------+------------+------------+------------+------------+------------+------------+
| Pixel          | 2 x 2      | 2.9 x      | 2.9 x      | 2 x 2      | 1.45 x     | 1.45 x     |
| Size [µm]      |            | 2.9        | 2.9        |            | 1.45       | 1.45       |
+----------------+------------+------------+------------+------------+------------+------------+
| Pixel          | 10 /       | 10 /       | 10 /       | 10 /       | 10 /       | 10 /       |
| Bitdepth       | 12 bit     | 12 bit     | 12 bit     | 12 bit     | 12 bit     | 12 bit     |
| [bit]          |            |            |            |            |            |            |
+----------------+------------+------------+------------+------------+------------+------------+
| Data           | MIPI       | MIPI       | MIPI       | MIPI       | MIPI       | MIPI       |
| Interface      | CSI-2      | CSI-2      | CSI-2      | CSI-2      | CSI-2      | CSI-2      |
| [Type]         |            |            |            |            |            |            |
+----------------+------------+------------+------------+------------+------------+------------+
| Data           | 4          | 2 / 4      | 2 / 4      | 2 / 4      | 2 / 4      | 2 / 4      |
| Interface      |            |            |            |            |            |            |
| [# Lanes]      |            |            |            |            |            |            |
+----------------+------------+------------+------------+------------+------------+------------+
| Communication  | I²C        | I²C        | I²C        | I²C        | I²C        | I²C        |
| Interface      | (CCI)      | (CCI)      | (CCI)      | (CCI)      | (CCI)      | (CCI)      |
+----------------+------------+------------+------------+------------+------------+------------+
| Drive          | 6 - 27     | 6 to       | 6 to       | 6 - 27     | 24 /       | 24 /       |
| Frequency      | /          | 27 /       | 27 /       | /          | 27 /       | 27 /       |
| [MHz]          | 37.125     | 37.125     | 37.125     | 37.125     | 37.125     | 37.125     |
|                | /          | /          | / 72 /     | /          | / 72 /     | / 72 /     |
|                | 74.25      | 74.25      | 74.25      | 74.25      | 74.25      | 74.25      |
+----------------+------------+------------+------------+------------+------------+------------+
| Input          | 1.2V,      | 1.2V,      | 1.1V,      | 1.1V,      | 1.1V,      | 1.1V,      |
| Voltages       | 1.8V,      | 1.8V,      | 1.8V,      | 1.8V,      | 1.8V,      | 1.8V,      |
|                | 2.9V       | 2.9V       | 3.3V       | 3.3V       | 2.9V       | 2.9V       |
+----------------+------------+------------+------------+------------+------------+------------+
| Supported      | M12 or     | C/CS       | C/CS       | M12 or     | M12 or     | M12 or     |
| Lens           | C/CS       | -Mount     | -Mount     | C/CS       | C/CS       | C/CS       |
| Mounts         | -Mount     | option     | option     | -Mount     | -Mount     | -Mount     |
|                | options    |            |            | options    | options    | options    |
+----------------+------------+------------+------------+------------+------------+------------+
| Board          | 26.5 x     | 26.5 x     | 26.5 x     | 26.5 x     | 26.5 x     | 26.5 x     |
| Dimensions     | 26.5       | 26.5       | 26.5       | 26.5       | 26.5       | 26.5       |
| [mm²]          |            |            |            |            |            |            |
+----------------+------------+------------+------------+------------+------------+------------+


**Rolling Shutters (Part 4/4) – equal or higher than 12 MP**

+----------------+-------------+-------------+-------------+-------------+-------------+
| Model          | FSM-        | FSM-        | FSM-        | FSM-        | FSM-        |
| Name           | IMX412      | IMX577      | IMX477      | AR1335      | IMX283      |
+================+=============+=============+=============+=============+=============+
| Shutter        | CMOS        | CMOS        | CMOS        | CMOS        | CMOS        |
| Type           | Rolling     | Rolling     | Rolling     | Rolling     | Rolling     |
|                | Shutter     | Shutter     | Shutter     | Shutter     | Shutter     |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Technology     | Starvis     | Starvis     | Starvis     | -           | Starvis     |
|                |             |             |             |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Resolution     | 12.3        | 12.3        | 12.3        | 13.1        | 20.2        |
| [MP]           |             |             |             |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Resolution     | 4056 x      | 4056 x      | 4056 x      | 4208 x      | 5496 x      |
| [HxV]          | 3040        | 3040        | 3040        | 3120        | 3694        |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Max.           | 59.9 FPS    | 59.9 FPS    | 59.9 FPS    | 27.2 FPS    | 24.7 FPS    |
| Framerate      | (4-Lane)    | (4-Lane)    | (4-Lane)    | (4-Lane)    | (4-Lane)    |
| [FPS]          | 30 FPS      | 30 FPS      | 30 FPS      | 13 FPS      |             |
|                | (2-Lane)    | (2-Lane)    | (2-Lane)    | (2-Lane)    |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Mono /         | Color       | Color       | Color       | Color       | Color       |
| Color          |             |             |             |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Sensor         | Sony        | Sony        | Sony        | onsemi      | Sony        |
| Manufacturer   |             |             |             |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Sensor         | IMX         | IMX         | IMX         | AR          | I           |
| Name           | 412-AACK    | 477-AAPK    | 577-AACK    | 1335CSSM    | MX283CQJ    |
|                |             |             |             | /           |             |
|                |             |             |             | AR          |             |
|                |             |             |             | 1335CSSC    |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Application    | Security    | Security    | Security    | Industrial  | Audio/Video |
| / Grade        |             |             |             |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Optical        | 1/2.3       | 1/2.3       | 1/2.3       | 1/3.2       | 1           |
| Format         |             |             |             |             |             |
| [inch]         |             |             |             |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Pixel          | 1.55 x      | 1.55 x      | 1.55 x      | 1.1 x       | 2.4 x       |
| Size [µm]      | 1.55        | 1.55        | 1.55        | 1.1         | 2.4         |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Pixel          | 10 / 12 bit | 8 / 10 /    | 8 / 10 /    | 8 / 10 bit  | 10 / 12 bit |
| Bitdepth       |             | 12 bit      | 12 bit      |             |             |
| [bit]          |             |             |             |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Data           | MIPI        | MIPI        | MIPI        | MIPI        | MIPI        |
| Interface      | CSI-2       | CSI-2       | CSI-2       | CSI-2       | CSI-2       |
| [Type]         |             |             |             |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Data           | 2 / 4       | 2 / 4       | 2 / 4       | 2 / 4       | 4           |
| Interface      |             |             |             |             |             |
| [# Lanes]      |             |             |             |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Communication  | I²C         | I²C         | I²C         | I²C         | I²C         |
| Interface      | (CCI)       | (CCI)       | (CCI)       |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Drive          | 6 / 12 /    | 6 to 27     | 6 to 27     | 6 to 48     | 6 to 27     |
| Frequency      | 18 / 27     |             |             |             |             |
| [MHz]          |             |             |             |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Input          | 1.05V,      | 1.05V,      | 1.05V,      | 1.2V,       | 1.2V,       |
| Voltages       | 1.8V,       | 1.8V,       | 1.8V,       | 1.8V,       | 1.8V,       |
|                | 2.75V       | 2.8V        | 2.8V        | 2.7V        | 2.9V        |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Supported      | M12 or      | M12 or      | M12 or      | M12 or      | C/CS-Mount  |
| Lens           | C/CS        | C/CS        | C/CS        | C/CS        | option      |
| Mounts         | -Mount      | -Mount      | -Mount      | -Mount      |             |
|                | options     | options     | options     | options     |             |
+----------------+-------------+-------------+-------------+-------------+-------------+
| Board          | 26.5 x      | 26.5 x      | 26.5 x      | 26.5 x      | 26.5 x      |
| Dimensions     | 26.5        | 26.5        | 26.5        | 26.5        | 26.5        |
| [mm²]          |             |             |             |             |             |
+----------------+-------------+-------------+-------------+-------------+-------------+


Sub-LVDS, SLVS and SLVS-EC Modules
-----------------------------------

+--------------+------------------+----------------+------------------+
| Model Name   | FSM-IMX264       | FSM-IMX304     | FSM-IMX530       |
+==============+==================+================+==================+
| Shutter Type | CMOS Global      | CMOS Global    | CMOS Global      |
|              | Shutter          | Shutter        | Shutter          |
+--------------+------------------+----------------+------------------+
| Technology   | Pregius (Gen2)   | Pregius (Gen2) | Pregius S (Gen4) |
+--------------+------------------+----------------+------------------+
| Resolution   | 5.1              | 12.4           | 24.5             |
| [MP]         |                  |                |                  |
+--------------+------------------+----------------+------------------+
| Resolution   | 2464 x 2056      | 4112 x 3008    | 5328 x 4608      |
| [HxV]        |                  |                |                  |
+--------------+------------------+----------------+------------------+
| Max.         | CSI-2: 35.7 FPS  | CSI-2: 23.4    | SLVS-EC: 106.9   |
| Framerate    | (4-Lane)         | FPS (4-Lane)   | FPS (8-Lane)     |
| [FPS]        |                  |                | CSI-2: 30 FPS    |
|              |                  |                | (4-Lane)         |
+--------------+------------------+----------------+------------------+
| Mono / Color | Color / Mono     | Color / Mono   | Color / Mono     |
+--------------+------------------+----------------+------------------+
| Sensor       | Sony             | Sony           | Sony             |
| Manufacturer |                  |                |                  |
+--------------+------------------+----------------+------------------+
| Sensor Name  | IMX264LLR /      | IMX304LLR /    | IMX530-AAMJ /    |
|              | IMX264LQR        | IMX304LQR      | IMX530-AAQJ      |
+--------------+------------------+----------------+------------------+
| Application  | Industrial       | Industrial     | Industrial       |
| / Grade      |                  |                |                  |
+--------------+------------------+----------------+------------------+
| Optical      | 2/3              | 1.1            | 1.2              |
| Format       |                  |                |                  |
| [inch]       |                  |                |                  |
+--------------+------------------+----------------+------------------+
| Pixel Size   | 3.45 x 3.45      | 3.45 x 3.45    | 2.74 x 2.74      |
| [µm]         |                  |                |                  |
+--------------+------------------+----------------+------------------+
| Pixel        | 12 bit           | 12 bit         | 8 / 10 / 12 bit  |
| Bitdepth     |                  |                |                  |
| [bit]        |                  |                |                  |
+--------------+------------------+----------------+------------------+
| Data         | SubLVDS          | SubLVDS        | SLVS, SLVS-EC    |
| Interface    |                  |                |                  |
| [Type]       |                  |                |                  |
+--------------+------------------+----------------+------------------+
| Data         | 4                | 4 / 8          | 1 / 2 / 4 / 8    |
| Interface [# |                  |                |                  |
| Lanes]       |                  |                |                  |
+--------------+------------------+----------------+------------------+
| Communication| I²C (4-wire      | I²C (4-wire    | I²C (4-wire      |
| Interface    | serial)          | serial)        | serial)          |
+--------------+------------------+----------------+------------------+
| Drive        | 37.125 / 54 /    | 37.125 / 54 /  | 37.125 / 54 /    |
| Frequency    | 74.25            | 74.25          | 74.25            |
| [MHz]        |                  |                |                  |
+--------------+------------------+----------------+------------------+
| Input        | 1.2V, 1.8V, 3.3V | 1.2V, 1.8V,    | 1.1V, 1.8V,      |
| Voltages     |                  | 3.3V           | 2.9V, 3.3V       |
+--------------+------------------+----------------+------------------+
| Supported    | C/CS-Mount       | C/CS-Mount     | C/CS-Mount       |
| Lens Mounts  | option           | option         | option           |
+--------------+------------------+----------------+------------------+
| Board        | 28 x 28          | 28 x 28        | 28 x 28          |
| Dimensions   |                  |                |                  |
| [mm²]        |                  |                |                  |
+--------------+------------------+----------------+------------------+