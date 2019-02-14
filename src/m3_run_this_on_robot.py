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
    #go_straight_encoder()
    #go_straight_time()
    real_thing()
    #run_test_calibrate()
    #run_test_arm()
    #move_arm_to_position()
    #lower_arm()
    #go_straight_until_dark()
    #go_straight_color_is()
    #proximity()
    #beacon()
    #camera()
    #LED()
    #m3_grab_object_LED(1, 1)
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
        if delegate.is_time_to_stop:
            break
def go_straight_encoder():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_encoder(50, 50)

def go_straight_time():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_time(50, 50)
def go_straight_until_dark():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_greater_than(30, 50)
def go_straight_color_is():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_color_is_not(1, 50)

def proximity():
    robot = rosebot.RoseBot()
    robot.drive_system.go_until_distance_is_within(1, 15, 50)

def beacon():
    robot= rosebot.RoseBot()
    robot.drive_system.go_straight_to_the_beacon(8, 50)

def camera():
    robot = rosebot.RoseBot()
    robot.drive_system.spin_counterclockwise_until_sees_object(50, 400)
def LED():
    robot = rosebot.RoseBot()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    time.sleep(5)
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()
    time.sleep(5)
    robot.led_system.left_led.turn_on()
    time.sleep(2)
    robot.led_system.left_led.turn_off()

def m3_grab_object_LED(start_time, increase):
   robot = rosebot.RoseBot()
   robot.arm_and_claw.calibrate_arm()
   robot.drive_system.go(20, 20)
   led = 1
   wait_time = int(start_time)
   while robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 0.25:
        if led == 1:
            robot.led_system.left_led.turn_on()
            time.sleep(wait_time)
        if led == 2:
            robot.led_system.left_led.turn_off()
            robot.led_system.right_led.turn_on()
            time.sleep(wait_time)
        if led == 3:
            robot.led_system.left_led.turn_on()
            time.sleep(wait_time)
        if led == 4:
            robot.led_system.right_led.turn_off()
            robot.led_system.left_led.turn_off()
            time.sleep(wait_time)
        if led == 4:
            led = 0
        led = led + 1
        wait_time = wait_time - (float(increase)/ (robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()+5))
        if wait_time <= 0:
            wait_time = 0
   robot.drive_system.stop()
   robot.arm_and_claw.raise_arm()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()