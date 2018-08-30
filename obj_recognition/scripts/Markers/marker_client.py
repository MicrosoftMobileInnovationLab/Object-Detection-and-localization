#!/usr/bin/env python
import rospy
from obj_recognition.srv import *
from std_msgs.msg import String
x=4
y=4




def ma_client(x,y, label):

	rospy.wait_for_service('get_marker')
	marker_client = rospy.ServiceProxy('get_marker', Get_ma)	
	marker_client(x,y, label)
	
st = String("person")
print(type(st))
ma_client(x,y,st)
