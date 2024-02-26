import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Float32

def callback(data):
    i = data.data 
    a = (i - 10) ** 0.5 
    rospy.loginfo("Recieved number = %d , After Decryption = %d ", i, a)
    pub.publish(a)

if __name__ == '__main__':
    rospy.init_node("subscriber", anonymous = True)
    rospy.loginfo("Data is Recieved")
    pub = rospy.Publisher('Second_topic', Float32, queue_size=10)
    sub = rospy.Subscriber('First_topic', Int16, callback=callback)
    rospy.spin()