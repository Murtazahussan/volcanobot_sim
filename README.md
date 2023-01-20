# Volcanobot_Sim
#########>>>>> Simulation Based Real-Time 3D Mapping Using 2 RP-Lidars in Vertical and Horizontal <<<<<#########

### Prerequisites

Ubuntu version : 18.04

ROS version : Melodic

Editor used : Vscode

Compiler : catkin

### Dedication

Specially this project is dedicated to my parants S.Mujahid hussain (My Father) and Kaneez Fatima Rizvi (My Mother), Institute of Industrial Electronics Engineering: IIEE and to the students of IIEE.

# Installation For Simulation Setup
 
(.) cd catkin_ws/src
 
(.) https://github.com/Murtazahussan/volcanobot_sim.git
 
(.) cd ..
 
(.) source devel/setup.bash

# 3D Simulated model of volcanobot

The volcanobot was modelled in Fusion360 and converted to URDF using fusion2urdf. Gazebo Pluggins for skid_steering_drive ,Odometry and both horizontal and vertical lidar were added to the urdf and tested in a custom made simulation environment/world in Gazebo. The given is the simulated model on Rviz with horizontal and vertical lidar. The model can be seen by given following command with all transformations ok status:
 
(.) roslaunch volcanobot_sim_description display.launch

![image](https://user-images.githubusercontent.com/122727165/212729009-df6c45cd-97aa-4259-862e-cbc2736d5b6b.png)

The given command used for spawn the volcanobot in gezebo based simulation:

(.) roslaunch volcanobot_sim_description gazebo.launch (with both Rp-lidars plugin)

![image](https://user-images.githubusercontent.com/122727165/212729488-35f31702-7a71-46ef-ab36-2d8a1ef62e18.png)

# Volcanobot Tf-tree

The transformation Tf-Tree of volcanobot will be seems as:

![image](https://user-images.githubusercontent.com/122727165/212730593-22bd3912-e2ad-495c-9f2e-75d7d11bb5e6.png)

# Volcanobot_sim Topics

The topics used for communication are as follows:

![image](https://user-images.githubusercontent.com/122727165/212730224-f23fdc63-563a-4c04-8d52-0335354b69e9.png)

# Volcanobot Odometry in Rviz

By using popular package of /teleop_twist_keyboard odom will be seems as follows in Rviz:

(.) roslaunch volcanobot_sim_description gazebo.launch

(.) rosrun teleop_twist_keyboard teleop_twist_keyboard.py

(.) rosrun rviz rviz

![image](https://user-images.githubusercontent.com/122727165/212731550-cb354f74-6cc9-4902-9f86-c656820be39c.png)

# Volcanobot Mapping

## G-Mapping

(.) roslaunch volcanobot_sim_description gazebo.launch

(.) roslaunch gmapping mapping.launch

(.) rosrun teleop_twist_keyboard teleop_twist_keyboard.py

(.) rviz

(.) rosrun map_server map_saver -f newmap

## Volcanobot G-Mapping Output

Open a new terminal window and run the following commands:

![image](https://user-images.githubusercontent.com/122727165/212752411-6a9ebf7d-e0eb-4451-b703-8403850d3170.png)
![image](https://user-images.githubusercontent.com/122727165/212752470-b057725f-a061-4442-b85c-2f20fad74c8c.png)

NOTE: Green line shows the odometry of the volcanobot and the 2nd image is the png of map

The map is already saved in /volcanobot_sim_description/maps directory if using the preset map.

# Volcanobot Real-Time 3D Point-Cloud Generation

(.) roslaunch volcanobot_sim_description gazebo.launch

clone follow package into your workspace

(.) https://github.com/Murtazahussan/ira_laser_tools.git

(.) roslaunch ira_laser_tools laserscan_multi_merger.launch

NOTE: Above command produce merged node of point-cloud whose name is merged_cloud for 3D point-cloud

(.) roslaunch gmapping mapping.launch

(.) rosrun teleop_twist_keyboard teleop_twist_keyboard.py

(.) rviz

NOTE: Add merged_cloud topic on point_cloud2 in rviz and give decay of 1000.

(.) rosrun map_server map_saver -f newmap

## Volcanobot Real-Time 3D Point-Cloud Generation Output

![image](https://user-images.githubusercontent.com/122727165/212757150-7f678a20-67ba-4b81-bade-ff63bd130d8d.png)

![image](https://user-images.githubusercontent.com/122727165/212757323-a9a6a9f5-bd8a-48d4-bbdf-52f2c8f36de6.png)
![image](https://user-images.githubusercontent.com/122727165/212757351-b0088934-5215-430d-bce2-8923408dc6c5.png)


# Volcanobot Navigation

(.) roslaunch volcanobot_sim_description gazebo.launch

(.) roslaunch volcanobot_sim_navigation move_base.launch

(.) rviz

After opening Rviz open the configuration file from the Rviz folder.

Type rqt in terminal and open dynamic reconfigure pluggin, load the final_reconf_param_sim.yaml from the reconf_params folder and you are all set to give navigation goals.

# Volcanobot Navigation Output

![image](https://user-images.githubusercontent.com/122727165/212764310-159eeb38-c37a-44ac-a60b-805f20f9a8f3.png)

# FINAL WORKING VIDEO OF REAL-TIME 3D Point Cloud Generation

https://user-images.githubusercontent.com/122727165/212772238-026c7a1c-f808-40a8-8d3a-adc09b5568e2.mp4

#####################>>>>>>>> Best Of Luck IIEEIANS <<<<<<<<#####################


