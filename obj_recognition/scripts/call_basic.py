#!/usr/bin/env python


import basic
import rospy

rospy.init_node('basic_shapes')
basic.pub_marker('/my_frame', 'first', 01, 1, 1, 0, 0, 1.0)
basic.pub_marker('/my_frame', 'first1', 02, 2, 2, 0, 0, 1.0)
basic.pub_marker('/my_frame', 'first2', 03, 3, 3, 0, 0, 1.0)
basic.pub_marker('/my_frame', 'first3', 04, 4, 4, 0, 0, 1.0)
basic.pub_marker('/my_frame', 'first4', 05, 5, 5, 0, 0, 1.0)

