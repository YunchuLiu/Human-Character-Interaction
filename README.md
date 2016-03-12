# homework-2-YunchuLiu
homework-2-YunchuLiu created by Classroom for GitHub

** Functioniality of the package**

There is one author-defined package called **twolink_robot** that simulates a visuably two-link robot arm in rviz. Three coordinate frames are visible at the root, joint of two links and the end effector. The end effector is following a trajectory, which is a circle of diameter 1 that is symmetric across the x axis of the root frame and 1.25 unit shifted in the positive direction. Markers in rviz are used to draw the trace of the end effector.

** Relevant published/subscribed topics and key nodes**

I have created two nodes in separate python scripts. The node **twolink_planar_robot** in *twolink_robot.py* is publishing data to topic `joint_states` to set the real-time postition of the joint. At the same time, **tf broadcaster** is publishing the translational and rotational transformation between every two link coordiname frames. The node **twolink_planar_listener** in *twolink_robot_listener.py* is publishing data to topic `/use_rviz/visualization_marker_array` to provide infomation on MarkerArray in rviz. Meanwhile, **tf listener** is receiving current transforms. 

Two Ros-defined nodes **joint_state_publisher** and **robot_state_publisher** are also launched. **joint_state_publisher** publishes **_sensor_msgs/JointState_** messages with all defined joints. In this applicatioin, the source of the data either comes from the input of GUI or data published by running the node **twolink_planar_robot**. **robot_state_publisher** is used in conjunction with the **robot_state_publisher** node to also publish transforms for all joint states.   

** Important parameters and args**

When launching node **twolink_planar_robot**, the private parameter _T_ can be adjusted to change the periods of the traced circle while _Fre_ sets the rate of publishing the messages. 

On the `roslaunch` command line,  setting the arg _use_rvis_ as `use_rvis:=1`will start rviz. Setting the arg _sys_joint_publisher_ as `sys_joint_publisher:=0` will change the data source of the **_sensor_msgs/JointState_** messages from GUI to the data published when running the node **twolink_planar_robot**.
