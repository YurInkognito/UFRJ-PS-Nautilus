#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Vector3

def calcular_modulo_vetor(vetor):
    modulo = (vetor.x**2 + vetor.y**2 + vetor.z**2)**0.5

    vetor.x = 3.0
    vetor.y = 5.0
    vetor.z = 5.8

    return modulo


def callback(data):
    modulo = calcular_modulo_vetor(data)
    pub = rospy.Publisher('/modulo', Float32, queue_size=10)
    pub.publish(modulo)

def meu_no():
    rospy.init_node('meu_no', anonymous=True)
    rospy.Subscriber('/vetor', Vector3, callback)
    rospy.spin()

if __name__ == '__main__':
    meu_no()