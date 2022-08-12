# MIPS-RAAS-Challenge

Tasks:

1) [Done] perform waypoint navigation with px4 based UAV in gazebo environment; simple square pattern is enough. 
2) [Done] Land UAVs on aruco marker after finishing the square pattern 
3) [Done] add a Husky model into the same environment with a single UAV and make them perform square pattern independently 
4) [Progress] Make UAV land on UGV which has an aruco marker on top of it
5) [TODO] do the same with an extra UAV and UGV (team of two UAV-UGV couple)


### Progress:

To reproduce the package Please make sure to install 
- ROS2 Foxy
- [PX4 Autopilot](https://docs.px4.io/main/en/ros/ros2_comm.html)
- OpenCV

#### Follow instructions carefully given at [PX4 ROS2 Bridge](https://docs.px4.io/main/en/ros/ros2_comm.html)

In your HOME directory, follow below instructions to Build and run this package
```
mkdir px4_ros_com_ros2
mkdir src
cd scr
git clone --recursive https://github.com/sumedhreddy90/MIPS-RAAS-Challenge.git
cd ~/px4_ros_com_ros2/src/px4_ros_com/scripts
bash build_ros2_workspace.bash

```
#### Additionally, Install PX4-Autopilot in your HOME directory

```
git clone https://github.com/PX4/PX4-Autopilot.git
```

#### To launch PX4 Iris using ROS2 

```
ros2 launch px4_husky_aruco px4_aruco_landing.launch.py 
```
![px4](https://user-images.githubusercontent.com/24978535/184264010-cb92ef4c-6f15-4494-b49e-ed87ea7e7304.png)
![px4_1](https://user-images.githubusercontent.com/24978535/184264062-440bfa50-34f5-4ed0-a8a6-90386dbb1c9b.png)



#### To Arm the PX4 and hover the PX4 Iris above the ground level by 4 meters

```
ros2 run px4_husky_aruco px4_offboard
```


https://user-images.githubusercontent.com/24978535/184264097-9270cb74-0355-4590-a32e-51fbaa878d1a.mp4



#### Waypoint Navigation using PX4 Iris - Perform a Square Trajectory 

```
ros2 run  px4_husky_aruco px4_waypoint
```


https://user-images.githubusercontent.com/24978535/184264119-a9ee8b99-f0ee-4adc-8424-f38ffeaa7c30.mp4


https://user-images.githubusercontent.com/24978535/184264126-11eae50c-9a79-4ccc-b51f-084921a89da9.mp4



#### Aruco Marker detection using PX4 Iris

```
ros2 run ros2_markertracker markertracker_node
```

![px4_aruco](https://user-images.githubusercontent.com/24978535/184264255-7d187041-7b45-40c5-9266-8c918cc1343f.png)
![px4_marker_detection](https://user-images.githubusercontent.com/24978535/184264469-66db8a74-119e-4338-89b6-7beb324adcdc.png)

https://user-images.githubusercontent.com/24978535/184264143-3f14bdea-955c-4f61-a9b1-92a8bf49bd12.mp4

https://user-images.githubusercontent.com/24978535/184264147-67aa91bf-966d-4c12-be72-af34f8a6373a.mp4





#### Land PX4 Iris onto Aruco Marker

```
ros2 run ros2_markertracker markertracker_node 
```
```
ros2 run  px4_husky_aruco px4_aruco_landing
```
![px4_aruco_landing](https://user-images.githubusercontent.com/24978535/184264218-8d7e26bf-6c5d-4d68-abe0-bf22e03865a9.png)

![px4_landing_2](https://user-images.githubusercontent.com/24978535/184264208-18fb669c-24d4-45af-848d-69630c28d29e.png)


https://user-images.githubusercontent.com/24978535/184264188-38cdcbb3-ceaa-45a9-82fa-2e3aaf289dac.mp4


#### Spawn Husky onto empty World
```
ros2 launch px4_husky_aruco husky_waypoint.launch.py
```
![husky_spawn](https://user-images.githubusercontent.com/24978535/184264965-8a46b844-c76e-44ec-9b2a-dfdcfacd3d6e.png)


### Spawn Husky algon with PX4 iris
```
```
