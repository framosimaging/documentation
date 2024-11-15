FSM Ecosystem
~~~~~~~~~~~~~~~

Key Terms
^^^^^^^^^^^
This section lists the key terms used in the FSM Ecosystem, providing their full forms to help you quickly understand the components and terminology essential for integrating advanced imaging solutions.

+--------+-------------------------------------------+
|Acronym | Full Form                                 |
+========+===========================================+
| FSM    | FRAMOS Sensor Module                      |
+--------+-------------------------------------------+
| FSA    | FRAMOS Sensor Adapter                     |
+--------+-------------------------------------------+
| FSM:GO | FRAMOS Sensor Module:GO                   |
+--------+-------------------------------------------+
| FMA    | FRAMOS Module Accessories                 |
+--------+-------------------------------------------+
| FFA    | FRAMOS Functional Adapter                 |
+--------+-------------------------------------------+
| FPA    | FRAMOS Processor Adapter                  |
+--------+-------------------------------------------+

FSM+FSA vs FSM:GO
^^^^^^^^^^^^^^^^^^^^^^^
The FSM Ecosystem offers two paths:

1. FSM+FSA emphasizes Flexibility with over 30 sensor types for custom solutions, ideal for projects needing unique configurations.

2. FSM:GO focuses on Time to Market, offering compact, cost-effective modules ready in weeks. It's perfect for high-volume production, providing up to 50% cost savings with pre-assembled, "Ready-to-Mount" components.

FSM+FSA
^^^^^^^^^^^^^

The FRAMOS Sensor Modules (FSM) encompass a broad range of high-performance
imaging solutions including the FSM+FSA and the for volume optimized FSM:GO series.
These modules are engineered to facilitate seamless integration of advanced image sensors 
into a variety of embedded vision systems. By offering standardized connectivity 
features such as connector types, pinouts, mechanical formats, and compatible 
accessories, the FSM Ecosystem delivers unparalleled versatility and ease of use. 
Whether for initial evaluation, proof-of-concept phases, or scaling up to mass production, 
FSM provides a flexible and reliable foundation for your imaging requirements. This section 
delves into the overarching characteristics of the FSM Ecosystem and explores the specifics 
of each module, complemented by detailed datasheets for individual models.

The FSM Ecosystem consists of FRAMOS Sensor Modules, Adapters, Software and Sources, and provides 
one coherent solution supporting the whole process of integrating image sensors into 
embedded vision products. 

During the evaluation and proof-of-concept phase, off-the-shelf sensor modules with a 
versatile adapter framework allow the connection of latest image sensor technology to 
open processing platforms, like the NVIDIA Jetson Family or the 96boards.org standard. 
Reference drivers and sample applications deliver images immediately after installation, 
supporting V4L2 and an optional derivate API providing comfortable integration. 
Within the development phase, electrical design references and driver sources guide with a 
solid and proven baseline to quickly port into individual system designs and extend scope, 
while decreasing risk and efforts. 


FSM:GO – the Optical Sensor Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The introduction of the FSM:GO series further enhances the FSM Ecosystem by offering an optimized, 
ready-to-use solution for volume production. The FSM:GO series comprises compact, 
integrated single-board sensor modules that deliver superior image quality and are meticulously 
engineered for high-volume deployment. These modules are designed to meet the industry's growing 
demand for efficient, high-performance imaging systems that can be easily integrated into a wide 
range of applications.


Off-the-Shelf Hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^

- FRAMOS Sensor Modules (FSM) from stock, ready for evaluation and prototyping
- Versatile adapter framework, allowing flexible testing of different modules on different processing boards.
- FRAMOS Sensor Adapter (FSA):
  Everything needed for specific sensor operation.
- FRAMOS Optical Sensor Modules (FSM:GO):
  Offers integrated single-board design, tailored for volume production, removing the need for FSA, and streamlined for easy evaluation, prototyping, and sensor integration and deployment in embedded vision applications.
- FRAMOS Processor Adapter (FPA):
  Connect up to four FSM + FSA or FSM:GO to a specific processor board.
- From lenses, mechanics, and cables, all necessary imaging accessories are available from a single source.

Kickstart Software Package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Drivers with basic sensor integration.
- V4L2 drivers for specific image sensors.
- Platform-specific device tree overlays.
- Streamlined V4L2 library (LibSV) with comfortable and generic C/C++ API.
- Example applications demonstrating initialization, configuration, and image acquisition.

Project-Based Ecosystem Support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Further to the off-the-shelf hardware and software, the Ecosystem supports you on a project basis with:

- Driver sources, allowing the focus on application-specific scope and sensor features.
- Electrical references for FSA and FPA, supporting quick and optimized embedding of FSMs.
- Engineering services via FRAMOS and its partners, allowing you to focus on your product’s unique value.
