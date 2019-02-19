import rosebot
import time


def pick_up_ball(speed, direction):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
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
    robot.drive_system.go(40, 40)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 0.5:
            robot.drive_system.stop()
            break
        if robot.sensor_system.color_sensor.get_color() == 1:
            robot.drive_system.go(100, 100)
            time.sleep(2)
            robot.drive_system.go(40,40)

    robot.arm_and_claw.raise_arm()
def get_ball_to_goal(color):
    robot = rosebot.RoseBot()

    robot.drive_system.go(40,40)
    while color != robot.sensor_system.color_sensor.color_sensor.get_color():
        if robot.sensor_system.color_sensor.get_color() == 1:
            robot.drive_system.go(100, 100)
            time.sleep(2)
            robot.drive_system.go(40,40)
        print(robot.sensor_system.color_sensor.color_sensor.get_color())
    robot.drive_system.stop()

