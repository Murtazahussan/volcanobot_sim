# volcanobot_sim
##########################   Simulation Based 3D Mapping Using 2 RP-Lidars in Vertical and Horizontal ########################

INSTALLATION:
 
(.) cd catkin_ws/src
 
(.) https://github.com/Murtazahussan/volcanobot_sim.git
 
(.) cd ..
 
(.) source devel/setup.bash

(.) The given is the simulated model on Rviz with horizontal and vertical lidar. The model can be ssen by given following command with all transformations ok status:
 
(.) roslaunch volcanobot_sim_description display.launch

![image](https://user-images.githubusercontent.com/122727165/212729009-df6c45cd-97aa-4259-862e-cbc2736d5b6b.png)

(.) The given command used for spawn the volcanobot in gezebo based simulation:

(.) roslaunch volcanobot_sim_description gazebo.launch (with both Rp-lidars plugin)

![image](https://user-images.githubusercontent.com/122727165/212729488-35f31702-7a71-46ef-ab36-2d8a1ef62e18.png)

(.)
