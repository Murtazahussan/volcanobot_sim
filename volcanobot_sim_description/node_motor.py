#!/usr/bin/env python
import rospy
from simple_pid import PID

from std_msgs.msg import Int64
from std_msgs.msg import Float64
from std_msgs.msg import Int16


cmd_vel = 0
PPR = 41
gearRatio = 60
decodeNumber = 4
pi = 3.14
r = 0.0325

right_ticks = 0
started = False
started1 = False
desired_Position = 0.0

current_wheel_distance = (right_ticks * 2 * pi *r) / (PPR * gearRatio * decodeNumber)
current_angle = right_ticks*((PPR * gearRatio * decodeNumber)/360)

pub = rospy.Publisher('/cmd_vel',Int16,queue_size=100)
pub1 = rospy.Publisher('/Current_angle',Int16,queue_size=100)
def sub_encoderValue():
    rospy.init_node('node_motor', anonymous=True)
    rospy.Subscriber('right_ticks',Int64,callback)
    rospy.Subscriber('desiredPosition',Float64,callback1)
    timer = rospy.Timer(rospy.Duration(0.01),timer_callback)
    rospy.spin()
    timer.shutdown()

def callback(data):
    global started,right_ticks
    print "right_ticks Received",right_ticks
    right_ticks = data.data
    if (not started):
        started = True

def callback1(data):
    global started1,desired_Position
    #print "Desired Received",desired_Position
    desired_Position = data.data
    if (not started1):
        started1 = True



def timer_callback(event):
    global started,started1,pub,right_ticks,cmd_vel,desired_Position,current_wheel_distance,current_angle
    
    if(started1):
        if (started):

            previouswheeldistance = current_wheel_distance
            pid = PID(100,0.5,1, setpoint=desired_Position,auto_mode=True)
            pid.output_limits = (-255, 255)
            pid.sample_time = 0.001
           cmd_vel = pid(previouswheeldistance)
            current_wheel_distance = (right_ticks * 2 * pi *r) / (PPR * gearRatio * decodeNumber) 

            #previous_angle=current_angle
            #pid = PID(0.022,0.01,2,setpoint=desired_Position)
            #pid.output_limits = (-255, 255)
            #pid.sample_time = 0.001
            #cmd_vel = pid(previous_angle)

            #if( 0 < cmd_vel <= 13):
            #    cmd_vel= cmd_vel + 11.5
            #elif (-13 <= cmd_vel < 0):
            #   cmd_vel = cmd_vel - 11.5
            #
            #current_angle = right_ticks/24
            
            pub.publish(cmd_vel)
            
            print "Publishing cmd_vel",cmd_vel
            print "Current Wheel distance",current_wheel_distance
            #print "Current angle",current_angle
            #print "Desired Position",desired_Position

if _name_ == '_main_':
    print "Running"
    sub_right_ticks()