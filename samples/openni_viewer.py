#!/usr/bin/env python

"""
This sample shows how to use the ecto_openni capture and cloud viewer.
"""

import ecto, ecto_pcl, ecto_openni
import ecto_ros.ecto_sensor_msgs as ecto_sensor_msgs
import ecto_pcl_ros, ecto_ros, sys

plasm = ecto.Plasm()

#device = ecto_openni.Capture('device')
#cloud_generator = ecto_pcl.NiConverter('cloud_generator')

cloud_sub = ecto_sensor_msgs.Subscriber_PointCloud2("cloud_sub", topic_name='/camera/depth/color/points')
msg2cloud = ecto_pcl_ros.Message2PointCloud("msg2cloud", format=ecto_pcl.XYZRGB)

viewer = ecto_pcl.CloudViewer("viewer", window_name="Clouds!")

#plasm.connect(device[:] >> cloud_generator[:],
#              cloud_generator[:] >> viewer[:])
plasm.connect(cloud_sub[:] >> msg2cloud[:],
    msg2cloud[:] >> viewer[:])

if __name__ == "__main__":
    from ecto.opts import doit
    ecto_ros.init(sys.argv, "ecto_pcl")
    doit(plasm, description='View the current point cloud.')
