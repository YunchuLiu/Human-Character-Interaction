import rosbag

'''
bag=rosbag.Bag('cropped.bag')
for topic, msg, t in bag.read_messages(topics=['transform_a','transform_b']):
    print topic,msg,t
bag.close()

'''
num_msgs=50

with rosbag.Bag('cropped.bag','w') as outbag:
    for topic, msg,t in rosbag.Bag('tfdata.bag').read_messages():
        if num_msgs<1:
            break
        num_msgs -=1
        outbag.write(topic,msg,t)
