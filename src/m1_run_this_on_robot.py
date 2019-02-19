"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Derrick Swart.
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
    actual_code()


def actual_code():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Handler(robot)
    mqtt_reciever = com.MqttClient(delegate)
    mqtt_reciever.connect_to_pc()
    while True:
        time.sleep(0.01)
        if delegate.is_time_to_stop:
            break


def pick_up_ball(speed, direction, initial_value, rate_entry,function):
    robot = rosebot.RoseBot()
    if direction == 'CCW':
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 250)
    elif direction == 'CW':
        robot.drive_system.spin_clockwise_until_sees_object(int(speed), 250)
    while True:
        blob = robot.sensor_system.camera.get_biggest_blob()
        if blob.center.x < (320 / 2):
            robot.drive_system.go(-20, 20)
        if blob.center.x > (320 / 2):
            robot.drive_system.go(20, -20)
        if abs(blob.center.x - (320 / 2)) < 4:
            robot.drive_system.stop()
            break

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()