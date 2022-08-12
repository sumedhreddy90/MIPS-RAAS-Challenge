# MIPS-RAAS-Challenge

TODO:

1) perform waypoint navigation with px4 based UAV in gazebo environment; simple square pattern is enough. 
2) Land UAVs on aruco marker after finishing the square pattern 
3) add a Husky model into the same environment with a single UAV and make them perform square pattern independently 
4) Make UAV land on UGV which has an aruco marker on top of it
5) do the same with an extra UAV and UGV (team of two UAV-UGV couple)


### Progress:

1. To launch PX4 Iris using ROS2 

```
ros2 launch px4_husky_aruco px4_aruco_landing.launch.py 
```
![px4](https://user-images.githubusercontent.com/24978535/184264010-cb92ef4c-6f15-4494-b49e-ed87ea7e7304.png)
![px4_1](https://user-images.githubusercontent.com/24978535/184264062-440bfa50-34f5-4ed0-a8a6-90386dbb1c9b.png)



2. To Arm the PX4 and hover the PX4 Iris above the ground level by 4 meters

```
ros2 run px4_husky_aruco px4_offboard
```


https://user-images.githubusercontent.com/24978535/184264097-9270cb74-0355-4590-a32e-51fbaa878d1a.mp4



3. Waypoint Navigation using PX4 Iris - Perform a Square Trajectory 

```
ros2 run  px4_husky_aruco px4_waypoint
```


https://user-images.githubusercontent.com/24978535/184264119-a9ee8b99-f0ee-4adc-8424-f38ffeaa7c30.mp4


https://user-images.githubusercontent.com/24978535/184264126-11eae50c-9a79-4ccc-b51f-084921a89da9.mp4



4. Aruco Marker detection using PX4 Iris

```
ros2 run ros2_markertracker markertracker_node
```

![px4_aruco](https://user-images.githubusercontent.com/24978535/184264255-7d187041-7b45-40c5-9266-8c918cc1343f.png)
![px4_marker_detection](https://user-images.githubusercontent.com/24978535/184264469-66db8a74-119e-4338-89b6-7beb324adcdc.png)



https://user-images.githubusercontent.com/24978535/184264143-3f14bdea-955c-4f61-a9b1-92a8bf49bd12.mp4


https://user-images.githubusercontent.com/24978535/184264147-67aa91bf-966d-4c12-be72-af34f8a6373a.mp4





5. Land PX4 Iris onto Aruco Marker

 ```
ros2 run  px4_husky_aruco px4_aruco_landing
```
![px4_aruco_landing](https://user-images.githubusercontent.com/24978535/184264218-8d7e26bf-6c5d-4d68-abe0-bf22e03865a9.png)

![px4_landing_2](https://user-images.githubusercontent.com/24978535/184264208-18fb669c-24d4-45af-848d-69630c28d29e.png)


https://user-images.githubusercontent.com/24978535/184264188-38cdcbb3-ceaa-45a9-82fa-2e3aaf289dac.mp4


6. Spawn Husky


