from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    planner_yaml=os.path.join(get_package_share_directory('path_planner_server'),\
                              'config','planner_server.yaml')

    controller_yaml=os.path.join(get_package_share_directory('path_planner_server'),
                                'config','controller.yaml')

    bt_navigator_yaml=os.path.join(get_package_share_directory('path_planner_server'),
                                'config','bt_navigator.yaml')
    recovery_yaml=os.path.join(get_package_share_directory('path_planner_server'),
                                'config','recovery.yaml')

    localization_launch=IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
        PathJoinSubstitution([FindPackageShare('localization_server'),
                              'launch',
                              'localization.launch.py'])
        )
    )

    planner_server_node=Node(package='nav2_planner',
                             executable='planner_server',
                             name='planner_server',
                             output='screen',
                             parameters=[planner_yaml])
    
    controller_node=Node(package='nav2_controller',
                             executable='controller_server',
                             name='controller_server',
                             output='screen',
                             parameters=[controller_yaml])

    bt_navigator_node=Node(package='nav2_bt_navigator',
                             executable='bt_navigator',
                             name='bt_navigator',
                             output='screen',
                             parameters=[bt_navigator_yaml])

    recoveries_server_node=Node(package='nav2_recoveries',
                             executable='recoveries_server',
                             name='recoveries_server',
                             output='screen',
                             parameters=[recovery_yaml])
    
    lifceycle_node=Node(package='nav2_lifecycle_manager',
                        executable='lifecycle_manager',
                        name='lifecycle_manager_pathplanner',
                        output='screen',
                        parameters=[{'autostart':True},
                                    {'node_names':['planner_server',
                                                   'controller_server',
                                                   'recoveries_server',
                                                   'bt_navigator']}])    

    ld=LaunchDescription()
    ld.add_action(localization_launch)
    ld.add_action(planner_server_node)
    ld.add_action(controller_node)
    ld.add_action(recoveries_server_node)
    ld.add_action(bt_navigator_node)
    ld.add_action(lifceycle_node)

    return ld