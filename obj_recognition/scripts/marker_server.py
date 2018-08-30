#!/usr/bin/env python

import rospy
from obj_recognition.srv import *
import time
import basic





counter = 0




def  handle_marker(req):

		

	global counter
	counter+=1
	basic.pub_marker('/map', ('first'+str(counter)), counter, req.x, req.y, 0, 0, 1.0,str(req.label))
	print("map")
	time.sleep(0.01)
	return 1 	



def listener():
	
	rospy.init_node('marker_server')
	
	s = rospy.Service('get_marker', Get_ma, handle_marker)
	print "Ready to publish marker"


	rospy.spin()









if __name__ == '__main__':
	listener()
