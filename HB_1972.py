#!/usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		    HolA Bot (HB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script should be used to implement Task 0 of HolA Bot (KB) Theme (eYRC 2022-23).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[1972]
# Author List:		[ Pradeep Pawar, Kedar Solapure, Nitin Patil, Aniket Patil]
# Filename:			task_0.py
# Functions:
# 					[ Comma separated list of functions in this file ]
# Nodes:		    Add your publishing and subscribing node


####################### IMPORT MODULES #######################
import rospy
from geometry_msgs.msg import Twist
import time
##############################################################


def move_circle():

    # Create a publisher which can "talk" to Turtlesim and tell it to move
    rospy.init_node('arm_to_pos', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
     
    # Create a Twist message and add linear x and angular z values
    move_cmd = Twist()
    move_cmd.linear.x = 1.0
    move_cmd.angular.z = 1.0

    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(10)

    # For the next 6 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(3.4):
    	rospy.loginfo("Turtle moving in circle.")
    	pub.publish(move_cmd)
    	rate.sleep()
    

    	
def rotate():
	
	rospy.init_node('arm_to_pos', anonymous=True)
	pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
	
	now = rospy.Time.now()
	rate = rospy.Rate(10)
    
	move_cmd = Twist()
	move_cmd.linear.x = 0.0
	move_cmd.angular.z = 1.0
	now = rospy.Time.now()
	while rospy.Time.now() < now + rospy.Duration.from_sec(1.6):
		rospy.loginfo("Turtle rotating.")
		pub.publish(move_cmd)
		rate.sleep()



def move_straight():
	rospy.init_node('arm_to_pos', anonymous=True)
	pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
	
	now1 = rospy.Time.now()
	rate = rospy.Rate(10)
	
	move_cmd = Twist()
	move_cmd.linear.x = 1.0
	move_cmd.angular.z = 0.0
	now = rospy.Time.now()
	while rospy.Time.now() < now1 + rospy.Duration.from_sec(1.1):
		rospy.loginfo("Turtle moving in straight line.")
		pub.publish(move_cmd)
		rate.sleep()



if __name__ == '__main__':
    try:
        move_circle()
        rotate()
        move_straight()
        
        
    except rospy.ROSInterruptException:
        pass
