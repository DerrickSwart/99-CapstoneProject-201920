import rosebot


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