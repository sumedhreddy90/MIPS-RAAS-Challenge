import rclpy
from rclpy.node import Node
import numpy as np
from geometry_msgs.msg import PoseArray
from geometry_msgs.msg import Pose
from px4_msgs.msg import VehicleOdometry
from px4_interfaces.msg import Trajectory
from ros2_markertracker_interfaces.msg import FiducialMarkerArray
from ros2_markertracker_interfaces.msg import FiducialMarker
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import  PoseWithCovariance
from geometry_msgs.msg import  Point
from geometry_msgs.msg import Quaternion

class Px4WayPoint(Node):

    def __init__(self):
        super().__init__('Px4WayPoint')

        
        self.publisher_ = self.create_publisher(Trajectory, 'waypoints', 10)
        self.i = 0
        self.waypoints = [[0, 0, -4, 0], [12, -4, -4, 0]]  ## In NED

        timer_period = 1.  # seconds
        self.timer = self.create_timer(timer_period, self.pub_call)
        
        # Placeholders for local position data
        self.local_x = None # north position in NED (meters)
        self.local_y = None # east position in NED (meters)
        self.local_z = None # down position in NED (meters)
        self.local_vx = None # north velocity in NED (metres/sec)
        self.local_vy = None # east velocity in NED (metres/sec)
        self.local_vz = None # down velocity in NED (metres/sec)
        
        self.marker_msg_id = None
        self.marker_msg_x = None
        self.marker_msg_y = None
        self.marker_msg_z = None
        self.marker_msg_or_x =  None
        self.marker_msg_or_y = None
        self.marker_msg_or_x = None
        self.marker_msg_or_w = None

        self.local_pos_sub_ = self.create_subscription(VehicleOdometry, "fmu/vehicle_odometry/out", self.local_pos_callback, 10)
        #self.aruco_marker_sub_ = self.create_subscription(FiducialMarkerArray, "/fiducial_markers", self.aruco_marker_callback, 10)
        self.next_point = self.waypoints[self.i]
        self.current_point = [0, 0, 4, 0]
        self.new_point = True

        self.get_logger().info(" ----Waiting for Local Position Info")

    def pub_call(self):
        msg = Trajectory()  # NED
        msg.x = 1. * self.next_point[0]	#convert to float
        msg.y = 1. * self.next_point[1]
        msg.z = 1. * self.next_point[2]
        msg.yaw = 1. * self.next_point[3]
        self.publisher_.publish(msg)


    def aruco_marker_callback(self, msg):
        msg = FiducialMarkerArray()
        # self.marker_msg_id = msg.marker[0].id
        # self.marker_msg_x = msg.marker[0].pose_cov_stamped.corners.pose.pose.position.x
        # self.marker_msg_y = msg.marker[0].pose_cov_stamped.corners.pose.pose.position.y
        # self.marker_msg_z = msg.marker[0].pose_cov_stamped.corners.pose.pose.position.z
        # self.marker_msg_or_x =  msg.marker[0].corners.pose.pose.orientation.x
        # self.marker_msg_or_y = msg.marker[0].pose_cov_stamped.corners.pose.pose.orientation.y
        # self.marker_msg_or_x = msg.marker[0].pose_cov_stamped.corners.pose.pose.orientation.z
        # self.marker_msg_or_w = msg.marker[0].pose_cov_stamped.corners.pose.pose.orientation.w
        self.get_logger().info(" ----Marker Coordinates Recieved")

    def local_pos_callback(self, msg):
        self.local_x = msg.x
        self.local_y = msg.y
        self.local_z = msg.z
        self.local_vx = msg.vx
        self.local_vy = msg.vy
        self.local_vz = msg.vz
        self.get_logger().info(" ----Local Position Recieved")
        current_pos = [self.local_x, self.local_y, self.local_z, self.local_vz]
        if self.new_point:
            self.new_point = False
            self.get_logger().info(" ----Aruco marker Detected")
            self.get_logger().info(" ----New Way Point Set after detecting Aruco marker")
        distance_to_target = np.linalg.norm([a - b for a, b in zip(current_pos[0:3], self.next_point[0:3])])
        self.get_logger().info(f" ----Distance from current position to Landing Arcuo marker: {distance_to_target}m")
        if (distance_to_target < 2.0) and (self.i + 1 < len(self.waypoints)):
            self.get_logger().info(" ----POINT REACHED! Ready for safe Landing")
            self.i += 1
            self.current_point = self.next_point
            self.next_point = self.waypoints[self.i]
            self.new_point = True
        
            

def main(args=None):
    rclpy.init(args=args)

    waypoint_publisher = Px4WayPoint()

    rclpy.spin(waypoint_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    waypoint_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

#[TODO] 
### Aruco Spawn 
# Initialize service clients
# self.pause_physics_client = self.create_client(Empty, '/gazebo/pause_physics')
# self.unpause_physics_client = self.create_client(Empty, '/gazebo/unpause_physics')
# self.spawn_request = self.create_client(SpawnEntity, 'spawn_entity')

# if not self.spawn_request.service_is_ready():
#     self.spawn_request.wait_for_service()

# Initialize model names

#self.robot_name = 'drone'
#self.marker_name = self.robot_name + '_marker'

# Compute marker pose based on current robot pose
# self.marker_pose = get_model_pose(robot_name)
# self.marker_pose.position.x -= 0.05
# self.marker_pose.position.z = 0.3
# self.marker_pose.orientation = Quaternion(*quaternion_from_euler(0, 0, pi))

# self.robot_name = 'asphalt_plane'
# self.marker_name = self.robot_name + '_marker'
# self.spawn_request = SpawnEntity.Request()
# self.spawn_request.name = self.marker_name
# self.spawn_request.xml = """
# <sdf version="1.6">
# <world name="default">
#     <include>
#     <uri>model://aruco_marker</uri>
#     </include>
# </world>
# </sdf>"""
# self.marker_pose = Pose
# self.position_ = [2.0, 2.0, 0.0]
# self.marker_pose.position = Point(x=self.position_[0], y=self.position_[1], z=self.position_[2])
# self.quat_tf = [0.0, 1.0, 0.0, 0.0]
# self.marker_pose.orientation = Quaternion(x=self.quat_tf[0], y=self.quat_tf[1], z=self.quat_tf[2], w=self.quat_tf[3])
# self.spawn_request._initial_pose = self.marker_pose

# # Spawn and attach marker to the robot
# #self.pause_physics_client()
# self.future = self.spawn_request.call_async(self.request)
# self.spin_until_future_complete(self.future)
# if self.future.result() is not None:
#     print('response: %r' % self.future.result())
# else:
#     raise RuntimeError('exception while calling service: %r' % self.future.exception())
#self.unpause_physics_client()