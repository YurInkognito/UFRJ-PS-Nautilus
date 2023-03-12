#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Vector3


class calcular_modulo_vetor:

    def __init__(self, x=4.0, y=6.0, z=3.0):
        self.x = x
        self.y = y
        self.z = z

    def calcular_modulo(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5


def callback(data):
    x = data.x
    y = data.y
    z = data.z
    modulo = calcular_modulo_vetor(x, y, z).calcular_modulo()
    pub = rospy.Publisher('/modulo', Float32MultiArray, queue_size=10)
    rate = rospy.Rate(10)
    pub.publish(Float32MultiArray(data=[modulo]))
    rate.sleep()

def meu_no():
    rospy.init_node('meu_no', anonymous=True)
    rospy.Subscriber('/vetor', Vector3, callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        meu_no()
    except rospy.ROSInterruptException:
        pass
