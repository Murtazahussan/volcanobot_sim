#!/usr/bin/env python
import roslib; roslib.load_manifest('laser_assembler')
import rospy; from laser_assembler.srv import *
from sensor_msgs.msg import PointCloud2

rospy.init_node("test_client")
rospy.wait_for_service("assemble_scans2")
try:
    assemble_scans = rospy.ServiceProxy('assemble_scans2', AssembleScans2)
    pub = rospy.Publisher("/laser_pointcloud",PointCloud2,queue_size =1)
    r = rospy.Rate(1)
    while True:

        resp = assemble_scans(rospy.Time(0,0), rospy.get_rostime())
        print "Got cloud with %u points" % len(resp.cloud.data)

    r.sleep()

except rospy.ServiceException, e:
    print "Service call failed: %s"%e
