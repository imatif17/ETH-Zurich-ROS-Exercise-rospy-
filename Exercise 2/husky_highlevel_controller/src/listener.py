#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

def callback(data):
	rospy.loginfo("Minimum range : {}".format(min(msg.ranges)))

def listener():
	topic = rospy.get_param('~topic_name')
	queue = rospy.get_param('~queue_size')
	rospy.init_node('listener', anonymous = True)
	rospy.Subscriber(topic, LaserScan, callback,queue)
	rospy.spin()

if __name__ == '__main__':
	listener()
