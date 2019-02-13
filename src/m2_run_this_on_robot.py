"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Joseph Conrad.
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

    robot = rosebot.RoseBot()
    #delegate = shared_gui_delegate_on_robot.Handler(robot)
    delegate = my_handler(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if delegate.is_time_to_stop:
            break

class my_handler(object):
    def __init__(self, robot):
        self.robot = rosebot.RoseBot()
        self.is_time_to_stop = False
    def go_forward_tone(self, frequency, rate):
        print('got', frequency, rate)
        self.robot.drive_system.go(50,50)
        distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        while True:
            self.robot.sound_system.tone_maker.play_tone(frequency,500)
            frequency = (distance - self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()) * rate
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 0.5:
                self.robot.arm_and_claw.move_arm_to_position(3000)
                break



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()