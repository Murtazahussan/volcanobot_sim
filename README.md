# volcanobot_sim
##########################   Simulation Based 3D Mapping Using 2 RP-Lidars in Vertical and Horizontal ########################

# INSTALLATION FOR Simulation Setup:
 
(.) cd catkin_ws/src
 
(.) https://github.com/Murtazahussan/volcanobot_sim.git
 
(.) cd ..
 
(.) source devel/setup.bash

# 3D Simulated model of volcanobot_sim 

The volcanobot was modelled in Fusion360 and converted to URDF using fusion2urdf. Gazebo Pluggins for skid_steering_drive ,Odometry and both horizontal and vertical lidar were added to the urdf and tested in a custom made simulation environment/world in Gazebo.The given is the simulated model on Rviz with horizontal and vertical lidar. The model can be seen by given following command with all transformations ok status:
 
(.) roslaunch volcanobot_sim_description display.launch

![image](https://user-images.githubusercontent.com/122727165/212729009-df6c45cd-97aa-4259-862e-cbc2736d5b6b.png)

The given command used for spawn the volcanobot in gezebo based simulation:

(.) roslaunch volcanobot_sim_description gazebo.launch (with both Rp-lidars plugin)

![image](https://user-images.githubusercontent.com/122727165/212729488-35f31702-7a71-46ef-ab36-2d8a1ef62e18.png)

# volcanobot_sim TF-TREE

The transformation Tf-Tree of volcanobot will be seems as:

![image](https://user-images.githubusercontent.com/122727165/212730593-22bd3912-e2ad-495c-9f2e-75d7d11bb5e6.png)

The topics used for communication are as follows:

![image](https://user-images.githubusercontent.com/122727165/212730224-f23fdc63-563a-4c04-8d52-0335354b69e9.png)

By using popular package of /teleop_twist_keyboard odom will be seems as follows in Rviz:

![image](https://user-images.githubusercontent.com/122727165/212731550-cb354f74-6cc9-4902-9f86-c656820be39c.png)

(.)
