#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2026 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2026-04-28
################################################################

import os
from hex_flow_core import LaunchConfig
from hex_flow_node_mujoco import default_mujoco_e3_desktop_node
from hex_flow_node_teleop import default_teleop_keyboard_node
from hex_flow_node_data import default_data_record_node
from hex_flow_comp_e3_desktop import default_comp_e3_desktop_node

config = LaunchConfig(
    local_only=True,
    enable_tui=True,
    log_to_file=True,
    save_path="/tmp/sim_comp.yml",
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RECORD_PATH = f"{SCRIPT_DIR}/record_data"

nodes = {
    "mujoco_e3_desktop":
    default_mujoco_e3_desktop_node(
        name="mujoco_e3_desktop",
        state_rate=500,
        cam_rate=30,
        headless=False,
        state_buffer_size=200,
        cam_buffer_size=8,
        sens_ts=False,
        head_cam_type="realsense",
        left_cam_type="usb",
        right_cam_type="usb",
        rate_hz=500,
        required=True,
        hidden=True,
        remap_dict={
            "left_arm_state": "mujoco_e3_desktop/left_arm_state",
            "right_arm_state": "mujoco_e3_desktop/right_arm_state",
            "left_grip_state": "mujoco_e3_desktop/left_grip_state",
            "right_grip_state": "mujoco_e3_desktop/right_grip_state",
            "left_arm_ctrl": "mujoco_e3_desktop/left_arm_ctrl",
            "right_arm_ctrl": "mujoco_e3_desktop/right_arm_ctrl",
            "left_grip_ctrl": "mujoco_e3_desktop/left_grip_ctrl",
            "right_grip_ctrl": "mujoco_e3_desktop/right_grip_ctrl",
        },
    ),
    "teleop_keyboard":
    default_teleop_keyboard_node(
        name="teleop_keyboard",
        device_path="",
        rate_hz=100.0,
        required=True,
        hidden=True,
        remap_dict={"teleop_keyboard": "teleop_keyboard/teleop_keyboard"},
    ),
    "comp_e3_desktop":
    default_comp_e3_desktop_node(
        name="comp_e3_desktop",
        rate_hz=500.0,
        arm_stable_pos="0.0,-1.5,3.0,0.07,0.0,0.0",
        grip_stable_pos="0.5",
        arrive_threshold=0.06,
        arm_err_threshold=0.02,
        grip_err_threshold=0.02,
        extra_mass=0.1,
        required=True,
        hidden=False,
        remap_dict={
            "left_arm_state": "mujoco_e3_desktop/left_arm_state",
            "right_arm_state": "mujoco_e3_desktop/right_arm_state",
            "left_grip_state": "mujoco_e3_desktop/left_grip_state",
            "right_grip_state": "mujoco_e3_desktop/right_grip_state",
            "left_arm_ctrl": "mujoco_e3_desktop/left_arm_ctrl",
            "right_arm_ctrl": "mujoco_e3_desktop/right_arm_ctrl",
            "left_grip_ctrl": "mujoco_e3_desktop/left_grip_ctrl",
            "right_grip_ctrl": "mujoco_e3_desktop/right_grip_ctrl",
            "keys": "teleop_keyboard/teleop_keyboard",
            "record": "comp_e3_desktop/record",
        },
    ),
    "data_record":
    default_data_record_node(
        name="data_record",
        record_path=RECORD_PATH,
        foxglove_host="127.0.0.1",
        foxglove_port=8765,
        start_cnt=0,
        required=False,
        remap_dict={
            "left_arm_state": "mujoco_e3_desktop/left_arm_state",
            "right_arm_state": "mujoco_e3_desktop/right_arm_state",
            "left_grip_state": "mujoco_e3_desktop/left_grip_state",
            "right_grip_state": "mujoco_e3_desktop/right_grip_state",
            "left_arm_ctrl": "mujoco_e3_desktop/left_arm_ctrl",
            "right_arm_ctrl": "mujoco_e3_desktop/right_arm_ctrl",
            "left_grip_ctrl": "mujoco_e3_desktop/left_grip_ctrl",
            "right_grip_ctrl": "mujoco_e3_desktop/right_grip_ctrl",
            "record": "comp_e3_desktop/record",
        },
    ),
}

config.set_nodes(nodes)
print(config.export())
