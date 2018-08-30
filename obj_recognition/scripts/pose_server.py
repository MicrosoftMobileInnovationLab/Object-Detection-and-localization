#!/usr/bin/env python

from geometry_msgs.msg import Pose2D
import rospy
from obj_recognition.srv import *  #0.0229  .003  .031 .009
import time



pose = Pose2D(0,0,0)

def pose_callback(msg):
	global pose
	pose = msg
	print(pose)



def  handle_pose(req):
	
    

    time.sleep(0.01)
    #print(pose) 
    return Get_poseResponse(pose)	



def listener():
	
	rospy.init_node('pose_server')
	rospy.Subscriber("pose2D", Pose2D,pose_callback)	
	s = rospy.Service('get_pose', Get_pose, handle_pose)
	print "Ready to give pose"


	rospy.spin()









if __name__ == '__main__':
	listener()
