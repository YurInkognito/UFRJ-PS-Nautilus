#!/usr/bin/python3

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
import math

if __name__ == '__main__':
    rospy.init_node('planeta_rviz')
    pub = rospy.Publisher('visualization_marker', Marker, queue_size=10)

    marker = Marker()
    marker.header.frame_id = "map"
    marker.type = Marker.SPHERE
    marker.action = Marker.ADD
    marker.pose.position.x = rospy.get_param('~raio_orbita') # Leitura do parâmetro raio_orbita
    marker.pose.position.y = 0
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.scale.x = 0.5
    marker.scale.y = 0.5
    marker.scale.z = 0.5
    marker.color.a = 1.0
    marker.color.r = 0.0
    marker.color.g = 0.0
    marker.color.b = 1.0

    t = 0
    while not rospy.is_shutdown():
        # Atualiza a posição do planeta com base no tempo
        marker.pose.position.x = rospy.get_param('~raio_orbita') * math.cos(t)
        marker.pose.position.y = rospy.get_param('~raio_orbita') * math.sin(t)

        pub.publish(marker)
        t += 0.01
        rospy.sleep(0.01)
