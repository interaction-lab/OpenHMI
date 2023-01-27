# OpenHMI
Official GitHub repository for OpenHMI: A Co-Design Workshop Toward Developing an Open-Source, Affordable, and Modular Platform for Enabling Scalable and Accessible Research and Outreach in Human-Machine Interaction. 


<img src="https://firebasestorage.googleapis.com/v0/b/uscinteractionlab.appspot.com/o/projects%2Fopenhmi%2Fblossom_natalie.jpg?alt=media&token=cb101f6c-fcd5-4605-bc7d-e66655d63212" alt="drawing" width="500"/>

# What to prepare:

Here is the to-do list to get ready before the OpenHMI workshop:

1) 3D-printing components: This is a list [(link)](https://docs.google.com/spreadsheets/d/1t7z_LR9PL6xjs64DBJckwSwQi114tPqmKAhL10Ktr_M/edit?usp=sharing) of all 3D-printed components needed for building the robot. You can find the name of the components, number of copies needed, and recommended 3D-printing material in this list. In addition, all of the 3D-printing STL files are located in OpenHMI/Hardware/3D Printing Files. If a 3d-printer is not available to you, we recommend out-source the printing to external service like [Xometry](https://www.xometry.com). The cost is only slightly higher and the quality and shipping time is more than satisfactory.


2) Purchasing needed materials: This is a purchase list [(link)](https://docs.google.com/spreadsheets/d/160ENST97K0b6GmP2vGoKJ554m8fZKPFYfByFBAFuFu0/edit?usp=sharing) of all the required materials needed for building the robot. The list includes the item, a purchase link and quantity needed for building 1 OpenHMI robot.

3) Robot Skin: The *Skin* directory contains instructions to create fabric and crocheted skins for the robot. 

4) Host computer: To run the robot code, either Ubuntu or Windows machines work well. [OpenSense](https://github.com/intelligent-human-perception-laboratory/OpenSense)'s standalone application is used for human perceptions for this project. However, because Opensense is based on [Microsoft Platform for Situated Intelligence](https://github.com/microsoft/psi), some of its components rely on Windows environment, a Windows machine will be needed to run the full robot + human perception demo. A webcam is needed for head detection for the workshop demo. GPU is not required, CPU will be used for those computations.


# How to Build:

To build the robot, you will need to assemble 1) robot skeleton; 2) wiring between motors.

1) You can follow this [build guide](https://docs.google.com/presentation/d/1tSICkZTfJj_O5U8Cg3pJ7uGAolSJe6wW/edit?usp=sharing&ouid=105532696586971028354&rtpof=true&sd=true) to work on building the robot skeleton.

2) You can follow this [build guide](https://docs.google.com/presentation/d/1g5RqoF_3xt6z6RvbIo_sDCCCWvMbcokz0HMdGt5Rlj0/edit?usp=sharing) to work on setting up the wiring between motors, and between motors and computer.

# How to Calibrate the Motors:

To calibrate the motors, you can click on "Robot Control Codebase @ 24fb527" folder in the repo, and it will bring you to the robot contol codebase located in the hrc2/blossom-public repo from cornell. The motor calibration script is located in hrc2/blossom-public/motor_calib.py.

# How to Control:

To control the robot, you can click on "Robot Control Codebase @ 24fb527" folder in the repo, and it will bring you to the robot contol codebase located in the hrc2/blossom-public repo from cornell. More documentations and guide can be found in the README of the hrc2/blossom-public repo. 


# How to Cite

This repository is developed and updated based on the [Blossom robot repository](https://github.com/hrc2/blossom-public) from the Human-Robot Collaboration & Companionship (HRC2) Lab at Cornell. If you use this repository or any of its content, please cite it as follows:

## Citation for the original Blossom robot

Suguitan, Michael, and Guy Hoffman. "Blossom: A handcrafted open-source robot." ACM Transactions on Human-Robot Interaction (THRI) 8.1 (2019): 1-27.

Bibtex:
```
@article{suguitan2019blossom,
author = {Suguitan, Michael and Hoffman, Guy},
title = {Blossom: A Handcrafted Open-Source Robot},
year = {2019},
issue_date = {March 2019},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {8},
number = {1},
doi = {10.1145/3310356},
journal = {J. Hum.-Robot Interact.},
month = {mar},
articleno = {2},
numpages = {27},
keywords = {craft, social robotics, toolkit, handcrafted, robot toolkit, craft robotics, 
            research platform, open-source, Robot design, soft robotics}
}
```

## Citation for the OpenSense system

Stefanov, Kalin, et al. "OpenSense: A Platform for Multimodal Data Acquisition and Behavior Perception." Proceedings of the 2020 International Conference on Multimodal Interaction. 2020.

Bibtex:
```
@inproceedings{stefanov2020opensense,
  title={OpenSense: A Platform for Multimodal Data Acquisition and Behavior Perception},
  author={Stefanov, Kalin and Huang, Baiyu and Li, Zongjian and Soleymani, Mohammad},
  booktitle={Proceedings of the 2020 International Conference on Multimodal Interaction},
  pages={660--664},
  year={2020}
}
```

----
