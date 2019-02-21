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
    delegate = shared_gui_delegate_on_robot.Handler(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()



    while True:
        time.sleep(0.04)
        if delegate.is_time_to_stop:
            break
        robot.sensor_system.camera.set_signature('SIG4')
        #print(robot.sensor_system.camera.get_biggest_blob())
        mqtt_receiver.send_message("display_camera", [robot.sensor_system.camera.get_biggest_blob().center.x,
                                    robot.sensor_system.camera.get_biggest_blob().center.y
                                 , robot.sensor_system.camera.get_biggest_blob().height
                                 , robot.sensor_system.camera.get_biggest_blob().width])






# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()