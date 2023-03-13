#!/usr/bin/python3

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

if __name__ == '__main__':
    rospy.init_node('estrela_imovel_rviz')
    pub = rospy.Publisher('visualization_marker', Marker, queue_size=10)

    marker = Marker()
    marker.header.frame_id = "map"
    marker.type = Marker.SPHERE
    marker.action = Marker.ADD
    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.scale.x = 1.0
    marker.scale.y = 1.0
    marker.scale.z = 1.0
    marker.color.a = 1.0
    marker.color.r = 1.0
    marker.color.g = 0.0
    marker.color.b = 0.0

    while not rospy.is_shutdown():
        pub.publish(marker)
        rospy.sleep(0.1)
