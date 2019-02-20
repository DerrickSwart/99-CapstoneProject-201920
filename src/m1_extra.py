import rosebot
import time


def pick_up_ball(speed, direction):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    if direction == 'CCW':
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 50)
    elif direction == 'CW':
        robot.drive_system.spin_clockwise_until_sees_object(int(speed), 50)
    robot.drive_system.stop()
    while True:
        blob = robot.sensor_system.camera.get_biggest_blob()
        if blob.center.x < (320 / 2):
            robot.drive_system.go(-20, 20)
        if blob.center.x > (320 / 2):
            robot.drive_system.go(20, -20)
        if abs(blob.center.x - (320 / 2)) < 4:
            robot.drive_system.stop()
            break

    time.sleep(0.4)
    robot.drive_system.go(20, 20)

    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 0.5:
            robot.drive_system.stop()
            break
        if robot.sensor_system.color_sensor.get_color() == 1:
            robot.drive_system.go(100, 100)
            time.sleep(1)
            robot.drive_system.go(20,20)

    robot.arm_and_claw.raise_arm()
    robot.sound_system.speech_maker.speak('i got the ball').wait()
    robot.sound_system.tone_maker.play_tone(400,1000).wait()
    time.sleep(1.5)
    robot.sound_system.tone_maker.play_tone(400, 1000).wait()
    time.sleep(1.5)
    robot.sound_system.tone_maker.play_tone(600, 1000).wait()
    print('i have picked up the ball')

def get_ball_to_goal(color, speed):
    robot = rosebot.RoseBot()

    colornumber = 0
    print('recieved color', color)
    if color == "Black" or "black":
        colornumber = 1
    if color == "Blue" or "blue":
        colornumber = 2
    if color == "Green" or "green":
        colornumber = 3
    if color == "Yellow" or "yellow":
        colornumber = 4
    if color == "Red" or "red":
        colornumber = 5
    if color == "White" or "white":
        colornumber = 6
    if color == "Brown" or "brown":
        colornumber = 7

    robot.drive_system.go(20,20)
    while True:
        """
        if robot.sensor_system.color_sensor.get_color() == 1:
            robot.drive_system.go(int(speed), int(speed))
            time.sleep(1)
            robot.drive_system.go(20,20)
        """
        if robot.sensor_system.color_sensor.get_color() == colornumber:
            robot.drive_system.stop()
            break
        print(robot.sensor_system.color_sensor.get_color())

    robot.arm_and_claw.lower_arm()
    robot.sound_system.speech_maker.speak('I have scored')
