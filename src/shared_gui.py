"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Joshua Giambattista, Derrick Swart, Joseph Conrad.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

def get_drive_for_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding =10, borderwidth = 5, relief = "ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text = 'drive for functions')
    frame_label.grid(row = 0, column = 1)


    seconds_box = ttk.Entry(frame, width = 8)
    seconds_box_label = ttk.Label(frame, text = 'Number of Seconds to go forward' )
    seconds_box.grid(row = 2, column = 0)
    second_speed_box = ttk.Entry(frame, width = 8)
    second_speed_box_label = ttk.Label(frame, text = 'at the speed')
    second_speed_box.grid(row = 2, column = 3)

    second_speed_box_label.grid(row = 1, column = 3)
    seconds_box_label.grid(row = 1, column = 0)


    inches_box = ttk.Entry(frame, width = 8)
    inches_box_label = ttk.Label(frame, text = 'Number of Inches using Time' )
    inches_box.grid(row = 5, column = 0)
    inches_speed_box = ttk.Entry(frame, width = 8)
    inches_box_speed_label = ttk.Label(frame, text = 'at the speed')
    inches_speed_box.grid(row = 5, column = 3)

    inches_box_speed_label.grid(row = 4, column = 3)
    inches_box_label.grid(row = 4, column = 0)


    distance_box = ttk.Entry(frame, width = 8)
    distance_box_label = ttk.Label(frame, text = 'Number of Inches using Encoder' )
    distance_box.grid(row = 8, column = 0)
    distance_speed_box = ttk.Entry(frame, width = 8)
    distance_box_speed_label = ttk.Label(frame, text = 'at the speed')
    distance_speed_box.grid(row = 8, column = 3)

    distance_box_speed_label.grid(row = 7, column = 3)
    distance_box_label.grid(row = 7, column = 0)


    seconds_box_button = ttk.Button(frame, text = "Run Go For Seconds")
    time_box_button = ttk.Button(frame, text = "Run Go For Inches Using Time")
    distance_box_button = ttk.Button(frame, text = "Run Go For Inches Using Encoder")

    seconds_box_button.grid(row = 3, column = 1)
    time_box_button.grid(row = 6, column = 1)
    distance_box_button.grid(row=9, column = 1)

    seconds_box_button['command'] = lambda:handle_go_for_seconds(mqtt_sender, seconds_box.get(), second_speed_box.get())
    time_box_button['command'] = lambda: handle_go_for_inches_using_time(mqtt_sender, inches_box.get(), inches_speed_box.get())
    distance_box_button['command'] = lambda: handle_go_for_inches_using_encoder(mqtt_sender, distance_box.get(), distance_speed_box.get())


    return frame

def get_sound_request(window, mqtt_sender):
    frame = ttk.Frame(window, padding = 10, borderwidth = 5, relief = 'ridge')
    frame.grid()
    frame_label = ttk.Label(frame, text = "SoundBoard")
    frame_label.grid(row = 0, column = 0)

    beep_label = ttk.Label(frame, text= 'Enter # of beeps:')
    beep_label.grid(column= 0, row=0)
    beep_number_entry = ttk.Entry(frame, width = 8)
    beep_number_entry.grid(column=1, row=0)
    beep_number_button = ttk.Button(frame, text = 'Execute # of Beeps')
    beep_number_button.grid(column=2, row=0)
    beep_number_button['command'] = lambda: handle_beeps_for_number(mqtt_sender, beep_number_entry.get())

    duration_label = ttk.Label(frame, text = 'Enter duration: ')
    duration_label.grid(column = 0, row = 1)
    duration_entry = ttk.Entry(frame, width = 8)
    duration_entry.grid(column=1,row=1)
    frequency_label = ttk.Label(frame, text='Enter Frequency: ')
    frequency_label.grid(column=2, row=1)
    frequency_entry = ttk.Entry(frame, width=8)
    frequency_entry.grid(column=3, row = 1)
    enter_button = ttk.Button(frame, text='Execute Tone Maker')
    enter_button.grid(column=4, row=1)
    enter_button['command'] = lambda: handle_play_freq_duration(mqtt_sender, frequency_entry.get(), duration_entry.get())

    speak_label = ttk.Label(frame, text = 'Enter speech text: ')
    speak_label.grid(column = 0, row = 2)
    speak_entry = ttk.Entry(frame, width = 8)
    speak_entry.grid(row=2, column=1)
    speak_button = ttk.Button(frame, text='Execute Speak')
    speak_button.grid(column=2, row=2)
    speak_button['command'] = lambda : handle_speak(mqtt_sender, speak_entry.get())

    return frame
def M1_pick_up_objects(window, mqtt_sender):
    frame = ttk.Frame(window, padding = 10, borderwidth = 5, relief = 'ridge')
    frame.grid()

    frame_label = ttk.Label(frame, text = 'Pick Up object Using Proximity')
    frame_label.grid(row = 0, column = 1)

    run_button = ttk.Button(frame, text = "Run Pick up using proximity")
    initial_button_label = ttk.Label(frame, text = "enter initial beeping rate")
    initial_button_entry = ttk.Entry(frame, width = 8)


    initial_button_entry.grid(row =2, column = 0 )
    initial_button_label.grid(row = 1, column = 0)

    rate_entry = ttk.Entry(frame, width = 8)
    rate_label = ttk.Label(frame, text = 'rate of increase')

    rate_entry.grid(row = 2, column = 2)
    rate_label.grid(row = 1, column = 2)

    run_button.grid(row = 3, column = 1)

    pixy_cam_pickup_button = ttk.Button(frame, text = 'pick up using pixycam')
    pixy_cam_pickup_button.grid(row = 6, column = 1)

    pixy_cam_direction_entry = ttk.Entry(frame, width = 8)
    pixy_cam_entry_label = ttk.Label(frame, text = 'enter direction of turning and the two rates above')
    pixy_cam_direction_entry.grid(row = 5, column = 1)
    pixy_cam_entry_label.grid(row = 4, column = 1)
    run_button['command'] = lambda: handle_m1_pick_up_using_prox(mqtt_sender, initial_button_entry.get(), rate_entry.get())
    pixy_cam_pickup_button['command'] = lambda: handle_m1_pick_up_using_pixy(mqtt_sender, initial_button_entry.get(), rate_entry.get(), pixy_cam_direction_entry.get() )
    return frame

def ir_control(window, mqtt_sender):
    frame = ttk.Frame(window, padding = 10, borderwidth = 5, relief = 'ridge')
    frame.grid()
    frame_label = ttk.Label(frame, text = 'IR Robot Control')
    frame_label.grid(row=0, column=1)

    speed_entry = ttk.Entry(frame, width = 8)
    speed_entry_label = ttk.Label(frame, text = 'enter speed here for all functions below')
    speed_entry.grid(row = 1, column = 0)
    speed_entry_label.grid(row = 1, column = 1)

    go_until_color_entry = ttk.Entry(frame, width = 8)
    go_until_color_label = ttk.Label(frame, text = 'color to stop at')
    go_until_color_button = ttk.Button(frame, text = 'go until color')

    intensity_label = ttk.Label(frame, text = 'enter intensity')
    intensity_entry = ttk.Entry(frame, width = 8)
    intensity_entry.grid(row = 4, column = 0)
    intensity_label.grid(row = 4, column = 1)

    


    go_until_color_label.grid(row = 3, column = 1)
    go_until_color_entry.grid(row = 3, column = 0)
    go_until_color_button.grid(row = 3, column = 2)
    go_until_color_button['command']= lambda: handle_go_until_color(mqtt_sender, go_until_color_entry.get())

    return frame


###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_go_until_color(mqtt_sender, color):
    print('go until color using the color:  ', color)
    mqtt_sender.send_message('go_until_color', [color])
def handle_m1_pick_up_using_pixy(mqtt_sender, initial_button_entry, rate_entry, direction):
    print('pick up using pixycam', initial_button_entry, rate_entry)
    mqtt_sender.send_message('m1_pick_up_using_pixy', [initial_button_entry, rate_entry, direction])

def handle_m1_pick_up_using_prox(mqtt_sender, initial_button_entry, rate_entry):
    print('m1 pick up using prox', initial_button_entry, rate_entry)
    mqtt_sender.send_message('m1_pick_up_using_prox', [initial_button_entry, rate_entry])

def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("forward:  ", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("forward", [left_entry_box.get(),
                                         right_entry_box.get()])

def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("backward:  ", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("backward", [(left_entry_box.get()),
                                         (right_entry_box.get())])
def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print ('left', '-',left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('left', [left_entry_box.get(),
                                      right_entry_box.get()])

def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('right', left_entry_box.get(), '-', right_entry_box.get())
    mqtt_sender.send_message('right', [left_entry_box.get(), right_entry_box.get()])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print("stop:  ")
    mqtt_sender.send_message("stop")

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('raise arm')
    mqtt_sender.send_message('raise_arm')


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('lower arm')
    mqtt_sender.send_message('lower_arm')


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('calibrate arm')
    mqtt_sender.send_message('calibrate_arm')



def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('move arm to position', arm_position_entry)
    mqtt_sender.send_message('move_arm_to_position', [int(arm_position_entry.get())])

def handle_go_for_seconds(mqtt_sender, number_of_inches, speed):
    print('go for',number_of_inches, ' inches at the speed', speed)
    mqtt_sender.send_message('go_straight_for_seconds', [int(number_of_inches), int(speed)])

def handle_go_for_inches_using_time(mqtt_sender, inches_box, inches_speed_box):
    print('go for', inches_box, 'inches at speed', inches_speed_box,'using time')
    mqtt_sender.send_message('go_straight_for_inches_using_time', [int(inches_box), int(inches_speed_box)])

def handle_go_for_inches_using_encoder(mqtt_sender, distance_box, distance_speed_box):
    print('go for', distance_box, 'inches at speed', distance_speed_box, 'using the encoder')
    mqtt_sender.send_message('go_straight_for_inches_using_encoder', [int(distance_box), int(distance_speed_box)])


###################################################
#Handlers for beeps and speak and tone
###################################################

def handle_beeps_for_number(mqtt_sender, beeps_entry):
    print("beep for", beeps_entry)
    mqtt_sender.send_message('beep_times', [int(beeps_entry)])

def handle_play_freq_duration(mqtt_sender, frequency, duration):
    print('frequency', frequency, ' duration: ', duration)
    mqtt_sender.send_message('tone', [int(frequency), int(duration)])

def handle_speak(mqtt_sender, speak_string):
    print('speak: ', speak_string)
    mqtt_sender.send_message("speak", [speak_string])

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message("quit")


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print("exit")
    handle_quit(mqtt_sender)
    exit()