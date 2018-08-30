#!/usr/bin/env python

import cv2
import numpy as np
from sensor_msgs.msg import Image,CameraInfo,CompressedImage,PointCloud2
import sensor_msgs.point_cloud2 as pc2
from cv_bridge import CvBridge,CvBridgeError
import rospy
import time
import math
from PIL import Image

import sys
sys.path.insert(0, '/home/nuc/py-faster-rcnn/tools')

#print(sys.path)

from obj_recognition.srv import *

import matplotlib
#matplotlib.use('Agg')
from matplotlib import pyplot as plt

from demo_kinect_all_pixels import setup,demo

#import show

#print("Using" +  matplotlib.get_backend()+ "as backend")


bridge = CvBridge()
counter=0	

	
def listener():
	try:	
		#print("im_here")

		frame = client()


		frame = bridge.imgmsg_to_cv2(frame, "bgr8")

		#cv2.circle(frame,(200,300), 9, (255,0,0),-1)

		global counter
		counter+=1
	
		print(counter)
		cv2.imshow("output", frame)
		if(cv2.waitKey(1)&0xFF==ord('k')):			#check the value before execution
		
			print('pressed k')
			net = setup()
			demo(net,frame)
	except:
		pass

	


def client():

	rospy.wait_for_service('get_image')
	image_client = rospy.ServiceProxy('get_image', Get_im)	
	resp1 = image_client()
	return resp1.im



if __name__ == '__main__':
	while True:
		listener()

