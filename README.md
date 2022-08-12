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

2. To Arm the PX4 and hover the PX4 Iris above the ground level by 4 meters

```
ros2 run px4_husky_aruco px4_offboard
```

3. Waypoint Navigation using PX4 Iris - Perform a Square Trajectory 

```
ros2 run  px4_husky_aruco px4_waypoint
```

4. Aruco Marker detection using PX4 Iris

```
ros2 run ros2_markertracker markertracker_node
```

5. Land PX4 Iris onto Aruco Marker

 ```
ros2 run  px4_husky_aruco px4_aruco_landing
```