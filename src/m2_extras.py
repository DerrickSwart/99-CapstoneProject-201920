#These are my extra functions that will run in shared_gui_delegate
import rosebot

class m2_handler(object):
    def __init__(self, robot):
        self.robot = rosebot.RoseBot()

    def m2_fetch_ball(self, speed, speak):
        """

        :param speed:
        :param speak:
        :return:
        """
        print('Got: ', speed, speak)
        self.robot.arm_and_claw.calibrate_arm()
        self.robot.sound_system.speech_maker.speak(speak)
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, 100)
        print('Made it through spin counterclockwise')
        self.m2_pickup_pixy()
        print('made it through pickup pixy')
        self.m2_pickup_ir(speed)
        print('pickup ir')

    def m2_pickup_pixy(self):
        while True:
            blob = self.robot.sensor_system.camera.get_biggest_blob()
            if blob.center.x < (320/2):
                self.robot.drive_system.go(-20, 20)
            if blob.center.x > (320/2):
                self.robot.drive_system.go(20,-20)
            if abs(blob.center.x - (320/2)) < 5:
                self.robot.drive_system.stop()
                break

    def m2_pickup_ir(self, speed):
        self.robot.drive_system.go(speed, speed)
        while True:
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 0.2:
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                break


    def m2_deliver_ball(self, speed):
        """

        :param speed:
        :return:
        """
        print('Got: ', speed)
