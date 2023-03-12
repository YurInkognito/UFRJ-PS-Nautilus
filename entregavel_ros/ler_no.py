#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32MultiArray

def callback(data):
    rospy.loginfo("Resultado recebido: %s", data.data[0])
    

def listener():
    rospy.init_node('listener')
    sub = rospy.Subscriber('resultados', Float32MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
