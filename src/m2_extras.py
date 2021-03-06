# These are my extra functions that will run in shared_gui_delegate
import rosebot
import time


class m2_handler(object):
    def __init__(self, robot):
        self.robot = rosebot.RoseBot()

    def m2_fetch_ball(self, speed, speak):
        """
        Side Effects: Locates the ball with the Pixy, then uses the IR to pick the ball up.
        :param speed:
        :param speak:
        :return:
        """
        print('Got: ', speed, speak)
        self.robot.sound_system.speech_maker.speak(speak)
        self.robot.arm_and_claw.calibrate_arm()
        self.robot.sensor_system.camera.set_signature("SIG4")
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, 100)
        print('Made it through spin counterclockwise')
        self.m2_pickup_pixy('SIG4')
        print('made it through pickup pixy')
        self.m2_pickup_ir(speed)
        print('pickup ir')

    def m2_pickup_pixy(self, sig):
        """
        Side Effects: turns to the angle of the tennis ball with the pixycam
        :return:
        """
        while True:
            self.robot.sensor_system.camera.set_signature(sig)
            blob = self.robot.sensor_system.camera.get_biggest_blob()
            if blob.center.x < (320 / 2):
                self.robot.drive_system.go(-30, 30)
            if blob.center.x > (320 / 2):
                self.robot.drive_system.go(30, -30)
            if abs(blob.center.x - (320 / 2)) < 3:
                self.robot.drive_system.stop()
                break

    def m2_pickup_ir(self, speed):
        """
        Side Effects: Drives forward until the IR sensor is less than 0.2 inches
        :param speed: int
        :return: None
        """
        self.robot.drive_system.go(speed, speed)
        while True:
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 0.2:
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                break

    def m2_deliver_ball(self, speed):
        """
        Side Effects: Drives until the robots reaches the edge of the court and drops off the ball
        :param speed: int
        :return:None
        """
        print('Got: ', speed)
        self.robot.drive_system.go(speed, speed)
        while True:
            if self.robot.sensor_system.color_sensor.get_color() != 6:
                break
        self.robot.drive_system.stop()
        self.robot.arm_and_claw.lower_arm()
        self.return_to_start(speed)

    def return_to_start(self, speed):
        """
        Side Effects: Finds the starting block with the camera and drives to it, then turns to get ready for next ball
        :param speed: int
        :return: None
        """
        self.robot.sensor_system.camera.set_signature("SIG3")
        print('returning at speed: ', speed)
        self.robot.drive_system.go(-1 * speed, -1 * speed)
        time.sleep(0.5)
        self.robot.drive_system.stop()
        self.robot.drive_system.spin_clockwise_until_sees_object(speed, 80)
        self.m2_pickup_pixy('SIG3')
        self.robot.drive_system.go_forward_until_distance_is_less_than(1, speed)
        self.robot.drive_system.go(-50,50)
        time.sleep(1)
        self.robot.drive_system.stop()

    def m2_speak(self, value):
        if value==1:
            self.robot.sound_system.speech_maker.speak("in")
        elif value == 2:
            self.robot.sound_system.speech_maker.speak('out')

