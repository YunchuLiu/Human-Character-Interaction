import rosbag
from geometry_msgs.msg import Transform
import utility 

'''
bag=rosbag.Bag('cropped.bag')

topics=bag.get_type_and_topic_info()[1].keys()
types=[]
for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
    types.append(bag.get_type_and_topic_info()[1].values()[i][0])

print types 
'''

bag=rosbag.Bag('tfdata.bag')
trans_a_list=[]
trans_b_list=[]
theta_list=[]

for topic, msg, t in bag.read_messages(topics=['transform_a']):
    trans_a_list.append([msg.translation.x,msg.translation.y,msg.translation.z])
    
for topic, msg, t in bag.read_messages(topics=['transform_b']):
    trans_b_list.append([msg.translation.x,msg.translation.y,msg.translation.z])

    
for i in range(0,len(trans_a_list)):
    theta=utility.get_theta(trans_a_list[i],trans_b_list[i])
    theta_list.append(theta)

   



 
        
    

