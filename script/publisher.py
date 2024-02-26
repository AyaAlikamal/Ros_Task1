#!/user/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Float32
import random

Transmetion = 1
sent_number = None
def call_back(data):
    global Transmetion
    global sent_number
    data_sent = data.data
    rospy.loginfo("Received Decrypted Number: %d", data_sent)
    if data_sent == sent_number:
       rospy.loginfo("Transmission is successfully Done.")
       Transmetion = 1
    else:                #  for validation if the data is not true but it is a dead end code
       rospy.logwarn("Data Received is Wrong.")
       Transmetion = 0

if __name__ == '__main__':
    rospy.init_node("subscriber_node", anonymous=True)
    pub = rospy.Publisher("First_topic", Int16 ,queue_size = 10)
    sub = rospy.Subscriber("Second_topic", Float32, call_back)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
          if Transmetion == 1:
            i = random.randint(0, 10)  
            a = (i ** 2) + 10  
            sent_number = i
            rospy.loginfo("Sending Encrypted Number : %d, befor Encryption: %d ", a, i)
            pub.publish(a)
            Transmetion = 0
          else:
            rospy.logwarn("No Message Recived, Please send it again.")
            a = (i ** 2) + 10
            pub.publish(a)    
          rate.sleep()   