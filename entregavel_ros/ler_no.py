#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Resultado recebido: %s", data.data)
    print(data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('resultados', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()