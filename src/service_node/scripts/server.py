#!/usr/bin/env python 
from __future__ import print_function
from service_node.srv import AddTwoInts,AddTwoIntsResponse
import rospy 
def encrypt_data(req):
  print("Returning [%s]"%((req.a- 10)** 2))
  return AddTwoIntsResponse(req.a)
   
def send_data_to_server():
   rospy.init_node('server')
   s = rospy.Service('encrypt_data', AddTwoInts, encrypt_data)
   print("Ready to receive")
   rospy.spin() 
if __name__ == "__main__":
     send_data_to_server()