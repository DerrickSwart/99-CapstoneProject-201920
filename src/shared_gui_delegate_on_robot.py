"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Joseph Conrad, Derrick Swart, Joshua Giambattista.
  Winter term, 2018-2019.
"""
import time
class Handler(object):
    def __init__(self, robot):
        '''

        :type robot: rosebot.RoseBot
        '''
        self.robot = robot
        self.is_time_to_stop = False
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
        for k in range(number_of_beeps):
            self.robot.sound_system.beeper.beep().wait()
    def tone(self, frequency, duration):
        print('recieved toneMaker. I will make a tone at', frequency, 'frequency for', duration, 'Milliseconds')
        self.robot.sound_system.tone_maker.play_tone(frequency, duration).wait()
    def speak(self, phrase):
        print('recieved speak. I will speak the phrase', phrase )
        self.robot.sound_system.speech_maker.speak(phrase)
    def quit(self):
        print("got quit")
        self.is_time_to_stop = True
    def exit(self):
        print("got exit")
    def m1_pick_up_using_prox(self, initial_time, rate_increase):
        print('recieved m1 pick up using prox with initial speed', initial_time, 'and rate increase of ', str(rate_increase) )
        wait_time = int(initial_time)
        self.robot.arm_and_claw.calibrate_arm()
        self.robot.drive_system.go(20, 20)
        while True:
            self.robot.sound_system.beeper.beep().wait()
            time.sleep(wait_time)

            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 0.5:
                print(self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
                self.robot.drive_system.stop()
                break
            wait_time = wait_time - ((float(rate_increase)/100) * self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
            if wait_time <=0:
                wait_time = 0
        self.robot.arm_and_claw.raise_arm()
    def m1_pick_up_using_pixy(self, speed, direction, initial_value, rate_entry,function):
        if direction == 'CCW':
            self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 250)
        if direction == 'CW':
            self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), 250)

        while True:
            blob = self.robot.sensor_system.camera.get_biggest_blob()
            if blob.center.x < (320/2):
                self.robot.drive_system.go(20,-20)
                if blob.center.x > (320/2):
                    self.stop()
                    break
            if blob.center.x > (320/2):
                self.robot.drive_system.go(-20,20)
                if blob.center.x > (320/2):
                    self.stop()
                    break
        if function == 'beep':
            self.m1_pick_up_using_prox(float(initial_value), float(rate_entry))
        if function == 'LED':
            self.m3_grab_object_LED(int(initial_value), float(rate_entry))
        if function == 'tone':
            self.m2_go_forward_tone(float(initial_value), float(rate_entry))


    def go_until_color(self, color, speed):
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

        self.robot.drive_system.go_straight_until_color_is(colornumber, int(speed))

    def go_straight_until_intensity_is_less_than(self, intensity, speed):
        print('recieved go_straight_until_intensity_is_less_than', intensity)
        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity), int(speed))
    def intensity_bigger_than(self, intensity, speed):
        print('recieved go until intensity is bigger than', intensity, 'at speed', speed)
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(intensity,int(speed))
    def go_until_color_is_not(self,color, speed):
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
        self.robot.drive_system.go_straight_until_color_is_not(colornumber,int(speed))
    def go_until_distance_less_than(self,inches,speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(inches), int(speed))
    def backward_until_further_than(self,inches, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches),int(speed))
    def go_until_within_distance(self,delta, inches, speed):
        self.robot.drive_system.go_until_distance_is_within(int(delta),int(inches),int(speed))

    def m3_grab_object_LED(self, start_time, increase):

        self.robot.arm_and_claw.calibrate_arm()
        self.robot.drive_system.go(20, 20)
        led = 1
        wait_time = int(start_time)
        while self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 0.25:
            if led == 1:
                self.robot.led_system.left_led.turn_on()
                time.sleep(wait_time)
            if led == 2:
                self.robot.led_system.left_led.turn_off()
                self.robot.led_system.right_led.turn_on()
                time.sleep(wait_time)
            if led == 3:
                self.robot.led_system.left_led.turn_on()
                time.sleep(wait_time)
            if led == 4:
                self.robot.led_system.right_led.turn_off()
                self.robot.led_system.left_led.turn_off()
                time.sleep(wait_time)
            if led == 4:
                led = 0
            led = led + 1
            wait_time = wait_time - (
                        float(increase) / (self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() + 5))
            if wait_time <= 0:
                wait_time = 0

        self.robot.drive_system.stop()
        self.robot.arm_and_claw.raise_arm()

    def m3_pick_up_pixy(self, speed, direction, initial_value, rate_entry, function):
        if direction == 'CCW':
            self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 250)
        if direction == 'CW':
            self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), 250)

        while True:
            blob = self.robot.sensor_system.camera.get_biggest_blob()
            if blob.center.x < (320/2):
                self.robot.drive_system.go(20,-20)
                if blob.center.x > (320/2):
                    self.stop()
                    break
            if blob.center.x > (320/2):
                self.robot.drive_system.go(-20,20)
                if blob.center.x > (320/2):
                    self.stop()
                    break
        if function == 'beep':
            self.m1_pick_up_using_prox(float(initial_value), float(rate_entry))
        if function == 'LED':
            self.m3_grab_object_LED(int(initial_value), float(rate_entry))
        if function == 'tone':
            self.m2_go_forward_tone(float(initial_value), float(rate_entry))

    def turn_counterclockwise_until_area_is(self,speed, area):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), int(area))
    def turn_clockwise_until_area_is(self,speed, area):
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed),int(area))
    def m2_go_forward_tone(self, frequency, rate):
        print('got', frequency, rate)
        self.robot.arm_and_claw.calibrate_arm()
        self.robot.drive_system.go(50,50)
        distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        while True:
            self.robot.sound_system.tone_maker.play_tone(frequency,500)
            frequency = (distance - self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()) * int(rate)
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1:
                self.stop()
                self.robot.arm_and_claw.move_arm_to_position(5000)
                break