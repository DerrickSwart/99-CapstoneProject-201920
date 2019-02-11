"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Joseph Conrad, Derrick Swart, Joshua Giambattista.
  Winter term, 2018-2019.
"""

class Handler(object):
    def __init__(self, robot):
        '''

        :type robot: rosebot.RoseBot
        '''
        self.robot = robot
    def forward(self, left_wheel_speed, right_wheel_speed):
        print("got forward", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed),
                                   int(right_wheel_speed))
    def stop(self):
        print("received stop")
        self.robot.drive_system.stop()
    def backward(self, left_wheel_speed, right_wheel_speed):
        print("received backward", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(-int(left_wheel_speed),
                                   -int(right_wheel_speed))
    def left(self, left_wheel_speed, right_wheel_speed):
        print('recieved left', '-', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(-(int(left_wheel_speed)),
                                   int(right_wheel_speed))
    def right(self, left_wheel_speed, right_wheel_speed):
        print('recieved right', left_wheel_speed, '-', right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), -(int(right_wheel_speed)))
    def raise_arm(self):
        print('recieved raise arm')
        self.robot.arm_and_claw.raise_arm()
    def lower_arm(self):
        print('recieved lower arm')
        self.robot.arm_and_claw.lower_arm()
    def calibrate_arm(self):
        print('recieved calibrate arm')
        self.robot.arm_and_claw.calibrate_arm()
    def move_arm_to_position(self, desired_position):
        print('recieved move arm to position', desired_position)
        self.robot.arm_and_claw.move_arm_to_position(desired_position)
    def go_straight_for_seconds(self, time, speed):
        print('recieved go straight for seconds:   ', time, speed)
        self.robot.drive_system.go_straight_for_seconds(time, speed)
    def go_straight_for_inches_using_time(self, inches, speed):
        print('recieved go straight for seconds using time:   ', inches, speed)
        self.robot.drive_system.go_straight_for_inches_using_time(inches, speed)
    def go_straight_for_inches_using_encoder(self, inches, speed):
        print('recieved go straight for inches using encoder:   ', inches, speed)
        self.robot.drive_system.go_straight_for_inches_using_encoder(inches, speed)
    def beep_times(self,number_of_beeps):
        print('recieved beep. I will beep', number_of_beeps, 'times')
    def toneMaker(self, frequency, duration):
        print('recieved toneMaker. I will make a tone at', frequency, 'frequency for', duration, 'seconds')
    def speak(self, phrase):
        print('recieved speak. I will speak the phrase', phrase)