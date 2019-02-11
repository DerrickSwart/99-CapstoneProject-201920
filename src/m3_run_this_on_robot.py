"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Joshua Giambattista.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    go_straight_encoder()
    #real_thing()
    #run_test_calibrate()
    #run_test_arm()
    #move_arm_to_position()
    #lower_arm()

def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()

def run_test_calibrate():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()

def move_arm_to_position():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(2000)
    time.sleep(1)
def lower_arm():
    robot=rosebot.RoseBot()
    robot.arm_and_claw.lower_arm()

def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Handler(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
def go_straight_encoder():
    robot = rosebot.RoseBot()
    robot.DriveSystem.go_straight_for_seconds_using_encoder(2000)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()