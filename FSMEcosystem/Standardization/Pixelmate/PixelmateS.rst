PixelMate™ (S)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Sub-LVDS, SLVS and SLVS-EC Pinout (8-Lane)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This pinout scheme applies to all sensors that natively output image
data using signals according to Sub-LVDS, SLVS or SLVS-EC specification.
This layout provides eight data lanes on the connector. Devices with
SLVS and SLVS-EC share the same sensor package pins therefore share the
same connector pins.

**Note:** Lane number assignment is applied according to SLVS numbering,
which differs in most cases from the SLVS-EC lane numbering. Please
refer to image sensor datasheet for correct SLVS-EC numbering.

Legend:

- ⚡ Common Voltages (from FPA to FSA)
- 🔋 Sensor Specific Voltages (from FSA to FSM)
- 📶 Sensor Signals
- ⏰ Driving Clocks
- 🔗 Data Lines
- 🚫 Reserved / Secondary Signals

+------------+-------------------+----------------+-------------------+
| Pin#       | Signal            | Pin#           | Signal            |
+============+===================+================+===================+
| 1          | ⚡ 3V8            | 2              | ⚡ 1V8            |
+------------+-------------------+----------------+-------------------+
| 3          | ⚡ 3V8            | 4              | ⚡ 1V8            |
+------------+-------------------+----------------+-------------------+
| 5          | 🔋 V_ANA          | 6              | 🔋 V_DIG          |
+------------+-------------------+----------------+-------------------+
| 7          | 🔋 V_ANA          | 8              | 🔋 V_DIG          |
+------------+-------------------+----------------+-------------------+
| 9          | 📶 V_IF           | 10             | 📶 V_AUX          |
+------------+-------------------+----------------+-------------------+
| 11         | 🚫 GND            | 12             | 🚫 GND            |
+------------+-------------------+----------------+-------------------+
| 13         | 🚫 GND            | 14             | 🚫 GND            |
+------------+-------------------+----------------+-------------------+
| 15         | 📶 SDA            | 16             | 📶 SCL            |
+------------+-------------------+----------------+-------------------+
| 17         | 📶 SDO            | 18             | 📶 XCE            |
+------------+-------------------+----------------+-------------------+
| 19         | 📶 TOUT0          | 20             | 📶 SLAMODE        |
+------------+-------------------+----------------+-------------------+
| 21         | 📶 TOUT1          | 22             | 📶 XMASTER        |
+------------+-------------------+----------------+-------------------+
| 23         | 📶 TOUT2          | 24             | 🚫 NC             |
+------------+-------------------+----------------+-------------------+
| 25         | 🚫 NC             | 26             | 📶 XTRIG          |
+------------+-------------------+----------------+-------------------+
| 27         | 🚫 NC             | 28             | 📶 XHS            |
+------------+-------------------+----------------+-------------------+
| 29         | 🚫 NC             | 30             | 📶 XVS            |
+------------+-------------------+----------------+-------------------+
| 31         | 🚫 GND            | 32             | 🚫 GND            |
+------------+-------------------+----------------+-------------------+
| 33         | 📶 RST            | 34             | 🔗 D_DATA_7_P     |
+------------+-------------------+----------------+-------------------+
| 35         | ⏰ MCLK           | 36             | 🔗 D_DATA_7_N     |
+------------+-------------------+----------------+-------------------+
| 37         | 🚫 GND            | 38             | 🚫 GND            |
+------------+-------------------+----------------+-------------------+
| 39         | 🔗 D_DATA_6_P     | 40             | 🔗 D_DATA_5_P     |
+------------+-------------------+----------------+-------------------+
| 41         | 🔗 D_DATA_6_N     | 42             | 🔗 D_DATA_5_N     |
+------------+-------------------+----------------+-------------------+
| 43         | 🚫 GND            | 44             | 🚫 GND            |
+------------+-------------------+----------------+-------------------+
| 45         | 🔗 D_DATA_4_P     | 46             | 🔗 D_DATA_3_P     |
+------------+-------------------+----------------+-------------------+
| 47         | 🔗 D_DATA_4_N     | 48             | 🔗 D_DATA_3_N     |
+------------+-------------------+----------------+-------------------+
| 49         | 🚫 GND            | 50             | 🚫 GND            |
+------------+-------------------+----------------+-------------------+
| 51         | 🔗 D_DATA_2_P     | 52             | 🔗 D_DATA_1_P     |
+------------+-------------------+----------------+-------------------+
| 53         | 🔗 D_DATA_2_N     | 54             | 🔗 D_DATA_1_N     |
+------------+-------------------+----------------+-------------------+
| 55         | 🚫 GND            | 56             | 🚫 GND            |
+------------+-------------------+----------------+-------------------+
| 57         | 🔗 D_DATA_0_P     | 58             | ⏰ D_CLK_0_P      |
+------------+-------------------+----------------+-------------------+
| 59         | 🔗 D_DATA_0_N     | 60             | ⏰ D_CLK_0_N      |
+------------+-------------------+----------------+-------------------+

**Table 1**: Standard Pinout of LVDS (8-Lane) interface

The table above shows the position of each signal on the 60-pin
connector in case the image sensor provides it. For further details,
please refer to the image sensor Datasheet.

**Note:** The table shows the general signal assignment that applies to
all connections using PixelMate™ (S). The signals that are eventually
available depend on image sensor and adapter configuration. Please use
the *FSM Connector Pinout* from the individual FSM datasheet as
reference for the available signals.