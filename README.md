# Human-Character-Interaction

Connect Kinect to computer. Set up OpenNI NITE tracker:

`roslaunch openni_launch openni.launch`

`roslaunch openni_tracker openni_tracker`

After the calibration is complete, run the following command to launch:

`roslaunch human_char_mapping myrobot.launch`

The settings of RViz is configured by char-config.rviz

The URDF of the character is written in my_robot.urdf

The main mapping is executed by first.py

The tool functions for calculating joint angles and the filtering are in utility.py





 


