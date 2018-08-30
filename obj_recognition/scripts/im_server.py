#!/usr/bin/env python

from sensor_msgs.msg import Image
import rospy
from obj_recognition.srv import *
import time
import cv2


im = cv2.imread('1.jpeg'.encode('utf-8'))

def image_callback(msg):
	global im
	im = msg



def  handle_im(req):
	
    
    #rospy.Subscriber("/camera/rgb/image_color", Image,image_callback)
    time.sleep(0.01)
    return Get_imResponse(im)	



def listener():
	
	rospy.init_node('im_server')
	rospy.Subscriber("/camera/rgb/image_color", Image,image_callback)
	
	s = rospy.Service('get_image', Get_im, handle_im)
	print "Ready to give image"


	rospy.spin()









if __name__ == '__main__':
	listener()
