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
    