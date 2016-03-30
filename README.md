## Human-Character-Interaction

### Overview 

This repository is documented for the quarter-long project Human-Character-Interaction. Please refer to this [link](http://yunchuliu.github.io/Portfolio/projects/project-5/) for more desription. 

### Files in Package

* __my_robot.launch__

Launches nodes: [robot_state_publisher](http://wiki.ros.org/robot_state_publisher), which subscribes to the `joint_states` topic and publishes the state of a robot to [tf](http://wiki.ros.org/tf), [joint_state_publisher](http://wiki.ros.org/joint_state_publisher), __map_to_char__ and __rviz__

It also defines several parameters such as `gui`,`self_joint_publisher` and `use_rviz`. By remapping the parameter to 1 (true) or 0 (false), we can choose whether to use gui, start mapping and startup RViz. 

* __char-config.rviz__

Set the configurations when loading RViz

* __my_robot.urdf__

The URDF for the character: the music stand 

* __first.py__

The main script in the package. It initializes the node __map_to_char__, looks up the transforms, calculates the joint angles for each joint and publishes [JointState message](http://docs.ros.org/api/sensor_msgs/html/msg/JointState.html) to `joint_states` topic. 

* __utility.py__

This script includes the functions we utilize. **get_trans()** looks up the transforms published by tf and returns the filtered vectors relating two frames. **double_expo_smooth()** implements the Adaptive Double Exponential Smoothing Filter specified on [Skeleton Joint Smoothing White Paper](https://msdn.microsoft.com/en-us/library/jj131429.aspx). **reset_filter()** initialize the parameters of the filter. **get_theta()** calculates revolute joint angles. **get_euler_from_spherical()** converts the rotation in Quaternion to Euler angles. 
 







 


