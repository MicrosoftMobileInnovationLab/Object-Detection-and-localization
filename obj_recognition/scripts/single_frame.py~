#!/usr/bin/env python

import cv2
import numpy as np
from sensor_msgs.msg import Image,CameraInfo,CompressedImage,PointCloud2
import sensor_msgs.point_cloud2 as pc2
from cv_bridge import CvBridge,CvBridgeError
import rospy
import time
import math

import sys
sys.path.insert(0, '/home/nuc/py-faster-rcnn/tools')


import matplotlib
#matplotlib.use('Agg')
from matplotlib import pyplot as plt

from demo_kinect_all_pixels import setup,demo

import show

#print("Using" +  matplotlib.get_backend()+ "as backend")


bridge = CvBridge()
counter=0	

def image_callback(ros_image):
	
	try:
		frame = bridge.imgmsg_to_cv2(ros_image, "bgr8")

		#cv2.circle(frame,(200,300), 9, (255,0,0),-1)

		global counter
		counter+=1
		
	
		print(counter)
		cv2.imshow("output", frame)
		
		if(cv2.waitKey(1)&0xFF==ord('k')):			#check the value before execution
			
			print('pressed k')
			net = setup()
			demo(net,frame)
	except KeyboardInterrupt:
			sys.exit(0)

	
	
	
	
	
def listener():
	
	try:
		rospy.init_node('imgDisplay2', anonymous=True)
		returned=rospy.Subscriber("/camera/rgb/image_color", Image,image_callback)
	except KeyboardInterrupt:
		sys.exit(0)
	rospy.spin()



if __name__ == '__main__':
    listener()

