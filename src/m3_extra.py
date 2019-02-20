import rosebot
import time
#import m3_run_this_on_laptop as m3
import random

def main_function(motor_speed, turning_value):
    robot = rosebot.RoseBot()
    if motor_speed == '50CC':
        highest_value = 30
    elif motor_speed == '100CC':
        highest_value = 60
    elif motor_speed == '150CC':
        highest_value = 90
    print(highest_value)
    turn(turning_value, highest_value)

def main_function2(motor_speed):
    robot = rosebot.RoseBot()
    if motor_speed == '50CC':
        robot.drive_system.go(30, 30)
        highest_value = 30
    elif motor_speed == '100CC':
        highest_value = 60
    elif motor_speed == '150CC':
        highest_value = 90
    print(highest_value)
    robot.drive_system.go(highest_value, highest_value)
    running_code(highest_value)

def stop():
    robot = rosebot.RoseBot()
    robot.drive_system.stop()

def running_code(highest_value):
    robot = rosebot.RoseBot()
    while True:
        banana(highest_value,robot)
        pick_up_item(highest_value)
        finish = finish_line()
        #turn(turning_value, highest_value)
        if finish == 1:
            robot.drive_system.stop()
            break

def turn(turning_value, highest_value):
   print(turning_value)
   robot = rosebot.RoseBot()
   if int(turning_value) > 0:
       robot.drive_system.go(highest_value, highest_value-turning_value)
       #running_code(highest_value, turning_value)
   elif int(turning_value) < 0:
       robot.drive_system.go(highest_value+turning_value, highest_value)
       #running_code(highest_value, turning_value)
   else:
       robot.drive_system.go(highest_value,highest_value)

def banana(highest_value,robot):

    if robot.sensor_system.color_sensor.get_color() == 4:
        robot.drive_system.stop()
        robot.drive_system.go(100,-100)
        robot.sound_system.speech_maker.speak("aaaaaaaaaaaaaaaa")
        time.sleep(2)
        robot.drive_system.go(highest_value, highest_value)


def pick_up_item(highest_value):
    robot = rosebot.RoseBot()
    if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 0.5:
        robot.drive_system.stop()
        robot.arm_and_claw.raise_arm()
        num = random.randrange(1,3)
        if num == 1:
            print("Placing a banana")
            robot.drive_system.go(30,-30)
            time.sleep(1.5)
            robot.drive_system.stop()
            robot.arm_and_claw.lower_arm()
            robot.drive_system.go(-20,-20)
            time.sleep(.5)
            robot.drive_system.go(-30,30)
            time.sleep(1.5)
            robot.drive_system.go(highest_value, highest_value)
        if num == 2:
            print("Placing a green shell")
            robot.drive_system.go(20, -20)
            time.sleep(1.5)
            robot.drive_system.stop()
            robot.arm_and_claw.lower_arm()
            robot.drive_system.go(-20, -20)
            time.sleep(.5)
            robot.drive_system.go(-20, 20)
            time.sleep(1.5)
            robot.drive_system.go(highest_value, highest_value)

def finish_line():
    robot = rosebot.RoseBot()
    if robot.sensor_system.color_sensor.get_color() == 2:
        robot.drive_system.stop()
        print("I have finished the race")
        return 1


