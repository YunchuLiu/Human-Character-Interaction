#!/usr/bin/python

import math
import rospy
import roslib
#roslib.load_manifest('two_link')
import tf 
from sensor_msgs.msg import JointState
from std_msgs.msg import String

def two_link():
    pub = rospy.Publisher("joint_states", JointState, queue_size = 10)
    
    rospy.set_param('~Fre',50)
    rate=rospy.Rate(rospy.get_param('~Fre'))
   
    rospy.set_param('~T', 5)
    T=rospy.get_param('~T')

    l1 = l2 = 1
    
    
    
    #br = tf.TransformBroadcaster()
    
    while not rospy.is_shutdown():
        
        t = (rospy.Time.now() - base_time).to_sec()
        x = 0.5 * math.cos((2* math.pi *t)/T) + 1.25
        y = 0.5 * math.sin((2* math.pi *t)/T)
        r = math.sqrt(x*x+y*y)
        apha = math.acos((l1*l1+l2*l2-r*r)/(2*l1*l2))
        beta = math.acos((r*r+l1*l1-l2*l2)/(2*l1*r))
        theta1 = math.atan(y/x)-beta
        theta2 = math.pi - apha
        
        
        js = JointState(name=['joint1', 'joint2'],position=[theta1,theta2])
        js.header.stamp = rospy.Time.now()
        
        
        
        
        #br.sendTransform((0, 0, 0), tf.transformations.quaternion_from_euler(0, 0, theta1), rospy.Time.now(),'link1','base_link')
        #br.sendTransform((1, 0, 0), tf.transformations.quaternion_from_euler(0, 0, theta2), rospy.Time.now(),'link2','link1')
        #br.sendTransform((1, 0, 0), tf.transformations.quaternion_from_euler(0, 0, 0), rospy.Time.now(),'link3','link2')
        
        pub.publish(js)  
        
        #rate.sleep()
if __name__ == '__main__':
    try:
        rospy.init_node('two_link', anonymous = True)
        base_time = rospy.Time.now()
        two_link()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
