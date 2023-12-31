from launch import LaunchDescription
import os 
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():

    cartographer_config_dir=os.path.join(get_package_share_directory('cartographer_slam'),'config')
    configuration_basename='cartographer.lua'

    cartographer_node=Node(package='cartographer_ros',
                           executable='cartographer_node',
                           name='cartographer_node',
                           output='screen',
                           parameters=[{'use_sim_time':True}],
                           arguments=['--configuration_directory',cartographer_config_dir,
                                      '--configuration_basename',configuration_basename])

    occupancy_grid_node=Node(package='cartographer_ros',
                           executable='occupancy_grid_node',
                           name='occupancy_grid_node',
                           output='screen',
                           parameters=[{'use_sim_time':True}],
                           arguments=['-resolution','0.05',
                                      '-publish_period_sec','1.0'])

    ld=LaunchDescription()
    ld.add_action(cartographer_node)
    ld.add_action(occupancy_grid_node)

    return ld