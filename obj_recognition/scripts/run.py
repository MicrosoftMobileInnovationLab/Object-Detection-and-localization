import os
os.system("gnome-terminal -x rosrun obj_recognition get_yaw")
os.system("gnome-terminal -x rosrun obj_recognition marker_server.py")
os.system("gnome-terminal -x rosrun obj_recognition depth_xy.py")
os.system("gnome-terminal -x rosrun obj_recognition im_server.py")
os.system("gnome-terminal -x rosrun obj_recognition pose_server.py")
