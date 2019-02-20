import rosebot
import time


def pick_up_ball(speed, direction, robot):
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

def get_ball_to_goal(color, speed, robot, robot_sender):


    colornumber = 0
    print('recieved color', color)

    if color == "Green":
        colornumber = 3
    elif color == "Brown":
        colornumber = 7

    elif color == "Red":
        colornumber = 5



    print(colornumber)

    time.sleep(4)

    robot.drive_system.go(50, 50)
    while True:
        if colornumber == 5:
            robot.drive_system.go(50,50)
            if robot.sensor_system.color_sensor.get_color() == 1:
                robot.drive_system.go(int(speed), int(speed))
                time.sleep(3)
                robot.drive_system.go(50, 50)
            if robot.sensor_system.color_sensor.get_color() == 5:
                robot.drive_system.stop()
                break

        elif colornumber == 3:
            robot.drive_system.go(50,50)
            if robot.sensor_system.color_sensor.get_color() == 5:
                turn_right_90()
                robot.drive_system.go(50,50)
            if robot.sensor_system.color_sensor.get_color() == 1:
                robot.drive_system.go(int(speed), int(speed))
                time.sleep(3)
                robot.drive_system.go(50, 50)
            if robot.sensor_system.color_sensor.get_color() == 3:
                robot.drive_system.stop()
                break

        elif colornumber == 7:
            if robot.sensor_system.color_sensor.get_color() == 5:
                turn_right_90()
                robot.drive_system.go(50,50)
            if robot.sensor_system.color_sensor.get_color() == 1:
                robot.drive_system.go(int(speed), int(speed))
                time.sleep(3)
                robot.drive_system.go(50, 50)
            if robot.sensor_system.color_sensor.get_color() == 3:
                turn_left_90()
                robot.drive_system.go(50,50)
            if robot.sensor_system.color_sensor.get_color() == 7:
                robot.drive_system.stop()
                break
        print(robot.sensor_system.color_sensor.get_color())

    if colornumber == 7:
        robot.sound_system.speech_maker.speak('i have scored on the brown goal')
        print('ggggggoooooooaaaaaaalllllll!!!  Congradulations you scored on the brown goal')
        robot_sender.send_message('brown_goal')
    elif colornumber == 3:
        robot.sound_system.speech_maker.speak('i have scored on the green goal')
        print('ggggggoooooooaaaaaaalllllll!!!  Congradulations you scored on the green goal')
        robot_sender.send_message('green_goal')
    elif colornumber == 5:
        robot.sound_system.speech_maker.speak('i have scored on the red goal')
        print('ggggggoooooooaaaaaaalllllll!!!  Congradulations you scored on the red goal')
        robot_sender.send_message('red_goal')




    print('I have scored on the ', color, 'goal')

def turn_left_90():
    robot = rosebot.RoseBot()
    robot.drive_system.stop()
    robot.drive_system.go(-40, 40)
    time.sleep(2.2)
    robot.drive_system.stop()

def turn_right_90():
    robot = rosebot.RoseBot()
    robot.drive_system.stop()
    robot.drive_system.go(40, -40)
    time.sleep(2.2)
    robot.drive_system.stop()



