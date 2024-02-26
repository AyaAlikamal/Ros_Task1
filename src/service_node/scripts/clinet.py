#!/usr/bin/env python
from __future__ import print_function  
import sys
import rospy
from service_node.srv import *
def encrypt_data(x):
    rospy.wait_for_service('encrypt_data')
    try:
        add_two_ints = rospy.ServiceProxy('encrypt_data', encrypt_data)
        resp1 = add_two_ints(x)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
def usage():
     return "%s [x]"%sys.argv[0] 
if __name__ == "__main__":
  if len(sys.argv) == 3:
        x = int(sys.argv[1])
  else:
       print(usage())
       sys.exit(1)
print("Requesting %s"%(x))
print("%s = %s"%(x, encrypt_data(x)))