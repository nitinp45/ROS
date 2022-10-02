#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import sys
 
 
def turtle_circle(radius):
	rospy.init_node('turtlesim', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
	rate = rospy.Rate(30)
	vel = Twist()

	t0 = rospy.Time.now().to_sec()

	dist = 0
	fin_d = 3.142
	print(rate)

	while dist <= fin_d:
		vel.linear.x = radius
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 1
		rospy.loginfo("Radius = %f",radius)
		pub.publish(vel)
		rate.sleep()

		t1 = rospy.Time.now().to_sec();

		dist = 0.93 * (t1 - t0)

	rot = 0
	while rot <= 22.55:
		vel.linear.x = 0
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 1
		
		pub.publish(vel)
		rate.sleep()
		
		rot += 0.5

	dist = 0
	while dist <= fin_d:
		vel.linear.x = radius
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
		rospy.loginfo("Radius = %f",radius)
		pub.publish(vel)
		rate.sleep()

		t1 = rospy.Time.now().to_sec();

		dist = 0.51 * (t1 - t0)
 
if __name__ == '__main__':
    try:
        turtle_circle(1)
    except rospy.ROSInterruptException:
        pass
