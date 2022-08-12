import rclpy
from rclpy.node import Node
import numpy as np
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import TwistWithCovariance


class HuskyWayPoint(Node):

    def __init__(self):
        super().__init__('HuskyWayPoint')
        self.publisher_ = self.create_publisher(PoseWithCovarianceStamped, '/set_pose', 10)
        self.i = 0
        self.waypoints = [[0, 0, 0, 0], [5, 0, 0, 90], [5, 5, 0, 90], [0, 5, 0, 90], [0, 0, 0, 0]]  ## In NED

        timer_period = 1.  # seconds
        self.timer = self.create_timer(timer_period, self.pub_call)
        
        # Placeholders for local position data
        self.local_x = None 
        self.local_y = None 
        self.local_z = None 
        self.local_vx = None 
        self.local_vy = None
        self.local_vz = None 
        
        self.local_pos_sub_ = self.create_subscription(Odometry, "/odom", self.local_pos_callback, 10)

        self.next_point = self.waypoints[self.i]
        self.current_point = [0, 0, 0, 0]
        self.new_point = True

        self.get_logger().info(" ----Waiting for Local Position Info")

    def pub_call(self):
        msg = PoseWithCovarianceStamped() 
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "base_footprint"
        msg.pose.pose.position.x = 1. * self.next_point[0]	#convert to float
        msg.pose.pose.position.y = 1. * self.next_point[1]
        msg.pose.pose.position.z = 1. * self.next_point[2]
        msg.pose.pose.orientation.z = 1. * self.next_point[3]
        self.publisher_.publish(msg)

    def local_pos_callback(self, msg):
        self.local_x = msg.pose.pose.position.x
        self.local_y = msg.pose.pose.position.y
        self.local_z = msg.pose.pose.position.z
        self.local_vx = msg.pose.pose.orientation.x
        self.local_vy = msg.pose.pose.orientation.y
        self.local_vz = msg.pose.pose.orientation.z

        self.get_logger().info(" ----Local Position Recieved")
        current_pos = [self.local_x, self.local_y, self.local_z, self.local_vz]
        if self.new_point:
            self.new_point = False
            self.get_logger().info(" ----New Way Point Set")
        distance_to_target = np.linalg.norm([a - b for a, b in zip(current_pos[0:3], self.next_point[0:3])])
        self.get_logger().info(f" ----Distance from current position to target: {distance_to_target}m")
        if (distance_to_target < 1.0) and (self.i + 1 < len(self.waypoints)):
            self.get_logger().info(" ----POINT REACHED!")
            self.i += 1
            self.current_point = self.next_point
            self.next_point = self.waypoints[self.i]
            self.new_point = True
            

def main(args=None):
    rclpy.init(args=args)

    waypoint_publisher = HuskyWayPoint()

    rclpy.spin(waypoint_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    waypoint_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
