from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    side_length_arg = DeclareLaunchArgument('side_length', default_value='0.8')
    side_length = LaunchConfiguration('side_length')

    turn_away_node = Node(
        package='my_robot_nodes',
        executable='turn_away',
        name='turn_away_node',
        parameters=[{'forward_speed': 0.2, 'turn_speed': 0.5}]
    )

    return LaunchDescription([
        side_length_arg,
        turn_away_node
    ])