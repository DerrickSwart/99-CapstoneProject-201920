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

    seconds_box_button.grid(row = 2, column = 1)
    time_box_button.grid(row = 5, column = 1)
    distance_box_button.grid(row=8, column = 1)

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


    run_button['command'] = lambda: handle_m1_pick_up_using_prox(mqtt_sender, initial_button_entry.get(), rate_entry.get())
    return frame

def m3_pick_up_prox_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='raised')
    frame.grid()

    frame_label = ttk.Label(frame, text='Find object using proximity sensor')
    frame_label.grid(row=0, column=0)

    run_button = ttk.Button(frame, text="Run Pick up using proximity")
    initial_button_label = ttk.Label(frame, text="enter initial blinking rate")
    initial_button_entry = ttk.Entry(frame, width=10)


    increase_entry = ttk.Entry(frame, width=10)
    increase_label = ttk.Label(frame, text='rate of blinking increase(between 1 and 2)')

    increase_entry.grid(row=4, column=0)
    increase_label.grid(row=3, column=0)

    run_button.grid(row=5, column=0)

    initial_button_entry.grid(row=2, column=0)
    initial_button_label.grid(row=1, column=0)

    run_button['command'] = lambda: handle_m3_pick_up_prox(mqtt_sender, initial_button_entry.get(),
                                                                 increase_entry.get())
    return frame
def ir_control(window, mqtt_sender):
    frame = ttk.Frame(window, padding = 10, borderwidth = 5, relief = 'ridge')
    frame.grid()
    frame_label = ttk.Label(frame, text = 'Robot Control')
    frame_label.grid(row=0, column=1)

    speed_entry = ttk.Entry(frame, width = 8)
    speed_entry_label = ttk.Label(frame, text = 'enter speed here for all functions below')
    speed_entry.grid(row = 1, column = 0)
    speed_entry_label.grid(row = 1, column = 1)

    go_until_color_entry = ttk.Entry(frame, width = 8)
    go_until_color_label = ttk.Label(frame, text = 'color ')
    go_until_color_button = ttk.Button(frame, text = 'go until color')
    go_until_color_not_button = ttk.Button(frame, text = 'stop when color is not')
    go_until_color_not_button['command']= lambda: handle_go_until_color_is_not(mqtt_sender, go_until_color_entry.get(),
                                                                               speed_entry.get())
    go_until_color_not_button.grid(row = 4, column = 2)

    intensity_label = ttk.Label(frame, text = 'enter intensity')
    intensity_entry = ttk.Entry(frame, width = 8)
    intensity_entry.grid(row = 5, column = 0)
    intensity_label.grid(row = 5, column = 1)

    intensity_lower_than_button = ttk.Button(frame,text = 'run go until intensity is lower than')
    intensity_lower_than_button['command'] = lambda : handle_go_until_intensity_less_than(mqtt_sender, intensity_entry.get(),
                                                                                          speed_entry.get())
    intensity_bigger_than_button = ttk.Button(frame, text = 'run go until intensity is greater than')
    intensity_bigger_than_button['command'] = lambda: handle_intensity_bigger_than(mqtt_sender, intensity_entry.get(),
                                                                                   speed_entry.get())
    intensity_lower_than_button.grid(row = 5,  column = 2)
    intensity_bigger_than_button.grid(row = 6, column = 2)


    go_until_color_label.grid(row = 3, column = 1)
    go_until_color_entry.grid(row = 3, column = 0)
    go_until_color_button.grid(row = 3, column = 2)
    go_until_color_button['command']= lambda: handle_go_until_color(mqtt_sender, go_until_color_entry.get(), speed_entry.get())

    return frame

def proximity_control_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')
    frame.grid()
    frame_label = ttk.Label(frame, text='Proximity control')
    frame_label.grid(row=0, column=1)

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry_label = ttk.Label(frame, text='enter speed here for all functions below')
    speed_entry.grid(row=1, column=0)
    speed_entry_label.grid(row=1, column=1)

    inches_entry = ttk.Entry(frame, width = 8)
    inches_entry_label = ttk.Label(frame, text = 'enter inches')
    inches_entry_label.grid(row = 3, column = 1)
    inches_entry.grid(row = 3, column = 0)

    go_until_close_button = ttk.Button(frame, text = 'forward until dist. less than')
    go_until_close_button['command']= lambda: handle_go_until_distance_less_than(mqtt_sender, inches_entry.get(),
                                                                                 speed_entry.get())
    go_until_close_button.grid(row = 2, column = 2)
    go_until_further_than_button = ttk.Button(frame, text = 'backward until dist. is greater than')
    go_until_further_than_button['command']= lambda: handle_backward_until_further_than(mqtt_sender,inches_entry.get()
                                                                                        , speed_entry.get())
    go_until_further_than_button.grid(row = 3, column = 2)

    range_entry = ttk.Entry(frame, width = 8)
    range_label = ttk.Label(frame, text = 'enter range to be within')
    range_entry.grid(row = 4, column = 0)
    range_label.grid(row = 4, column = 1)

    dist_within_button = ttk.Button(frame, text= 'go until dist. within')
    dist_within_button['command']= lambda :handle_go_until_distance_within(mqtt_sender, range_entry.get(),
                                                                           inches_entry.get(),
                                                                           speed_entry.get())
    dist_within_button.grid(row = 5, column = 2)
    return frame


def m1_find_with_pixy_using_color(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='groove')
    frame.grid()
    frame_label = ttk.Label(frame, text= 'm1 find and pickup an object using pixy')
    frame_label.grid(row = 0, column = 0)

    scale = ttk.Scale(frame, from_=10, to=100)
    speed_label = ttk.Label(frame, text = 'speed from 10-100 respectivly')
    speed_label.grid(row = 1, column = 0)
    scale.grid(row = 1, column = 1)

    direction_box = ttk.Entry(frame, width = 8)
    direction_box_label = ttk.Label(frame, text = 'enter direction, CCW or CW')
    direction_box_label.grid(row = 2, column = 0)
    direction_box.grid(row = 2, column = 1)

    initial_button_label = ttk.Label(frame, text="enter initial value")
    initial_button_entry = ttk.Entry(frame, width=8)

    initial_button_entry.grid(row=3, column=1)
    initial_button_label.grid(row=3, column=0)

    rate_entry = ttk.Entry(frame, width=8)
    rate_label = ttk.Label(frame, text='rate of increase')

    rate_entry.grid(row=4, column=1)
    rate_label.grid(row=4, column=0)

    which_to_run_entry = ttk.Entry(frame, width = 8)
    which_to_run_entry_label = ttk.Label(frame, text = 'enter beep, LED, or tone to call that function')

    which_to_run_entry.grid(row = 5, column = 1)
    which_to_run_entry_label.grid(row = 5, column = 0)

    run_button = ttk.Button(frame, text = 'run')
    run_button['command'] = lambda: handle_m1_pick_up_using_pixy(mqtt_sender,scale.get(), direction_box.get(),
                                                                 initial_button_entry.get(), rate_entry.get(),
                                                                 which_to_run_entry.get())
    run_button.grid(row = 7, column = 0)
    return frame

def m3_pick_up_pixy_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='raised')
    frame.grid()
    frame_label = ttk.Label(frame, text='m3 find and pickup an object using PixyCam')
    frame_label.grid(row=0, column=1)

    speed_entry = ttk.Entry(frame, width = 10)
    speed_label = ttk.Label(frame, text='speed from 0-100 respectivly')

    direction_box = ttk.Entry(frame, width=10)
    direction_box_label = ttk.Label(frame, text='enter direction(CCW or CW)')


    initial_button_label = ttk.Label(frame, text="enter initial beeping, blinking, or pitch rate")
    initial_button_entry = ttk.Entry(frame, width=10)

    increase_entry = ttk.Entry(frame, width=10)
    increase_label = ttk.Label(frame, text='rate of increase')

    which_to_run_entry = ttk.Entry(frame, width=10)
    which_to_run_entry_label = ttk.Label(frame, text='enter beep, LED, or tone')


    speed_label.grid(row=1, column=0)
    speed_entry.grid(row=1, column=1)
    direction_box_label.grid(row=2, column=0)
    direction_box.grid(row=2, column=1)
    initial_button_entry.grid(row=1, column=3)
    initial_button_label.grid(row=1, column=2)
    increase_entry.grid(row=2, column=3)
    increase_label.grid(row=2, column=2)
    which_to_run_entry.grid(row=3, column=1)
    which_to_run_entry_label.grid(row=3, column=0)

    start_button = ttk.Button(frame, text='Start')
    start_button['command'] = lambda: handle_m3_pick_up_pixy(mqtt_sender, speed_entry.get(), direction_box.get(),
                                                                 initial_button_entry.get(), increase_entry.get(),
                                                                 which_to_run_entry.get())
    start_button.grid(row=7, column=2)
    return frame

def camara_conrtol_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text='camara control')
    frame_label.grid(row=0, column=0)

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry_label = ttk.Label(frame, text='enter speed, 0-100')
    speed_entry.grid(row=1, column=0)
    speed_entry_label.grid(row=1, column=1)

    area_entry = ttk.Entry(frame, width=8)
    area_entry_label = ttk.Label(frame, text='enter area of color')
    area_entry.grid(row=2, column=0)
    area_entry_label.grid(row=2, column=1)

    clockwise_button = ttk.Button(frame, text='turn clockwise')
    counterclockwise_button = ttk.Button(frame, text=' turn counterclockwise')
    clockwise_button['command'] = lambda: handle_turn_clockwise_using_pixy(mqtt_sender, speed_entry.get(),
                                                                               area_entry.get())
    counterclockwise_button['command'] = lambda: handle_turn_counterclockwise_using_pixy(mqtt_sender,
                                                                                             speed_entry.get(),
                                                                                             area_entry.get())
    clockwise_button.grid(row=1, column=3)
    counterclockwise_button.grid(row=2, column=3)

    return frame

def m2_tone_frame(window, mqtt_sender):
    frame = ttk.Frame(window, relief='groove', borderwidth=5, padding=10)
    frame.grid()
    init_label = ttk.Label(frame, text='Initial Frequency')
    init_label.grid(column=0, row=0)
    init_entry = ttk.Entry(frame, width=8)
    init_entry.grid(column=0, row=1)
    increase_label = ttk.Label(frame, text='Increase Rate')
    increase_label.grid(column=1, row=0)
    increase_entry = ttk.Entry(frame, width=8)
    increase_entry.grid(column=1, row=1)
    submit_button = ttk.Button(frame, text='Go Forward Beeping Faster')
    submit_button.grid(rowspan=2)
    submit_button['command'] = lambda: m2_handle_forward_tone(mqtt_sender, init_entry.get(), increase_entry.get())
    return frame

def m2_pixy_cam(window, mqtt_sender):
    frame = ttk.Frame(window, relief = 'groove', borderwidth = 5, padding =10)
    frame.grid()
    frame_label = ttk.Label(frame, text='M2 USE PIXY TO LOCATE OBJECT')
    frame_label.grid(row=0, column=0)

    scale = ttk.Label(frame, text = "Robot Speed from 0 - 100")
    speed_slider = ttk.Scale(frame, from_=0, to=100)
    speed_slider.grid(column= 1, row = 1)
    scale.grid(row=1, column=0)

    direction_box = ttk.Entry(frame, width=8)
    direction_box_label = ttk.Label(frame, text='enter direction, CCW or CW')
    direction_box_label.grid(row=2, column=0)
    direction_box.grid(row=2, column=1)

    initial_button_label = ttk.Label(frame, text="enter initial value scale 50 - 200")
    initial_button_entry = ttk.Scale(frame, from_=50 , to=200)

    initial_button_entry.grid(row=3, column=1)
    initial_button_label.grid(row=3, column=0)

    rate_entry = ttk.Scale(frame, from_=0 , to=200)
    rate_label = ttk.Label(frame, text='Increase Rate from 0 - 200')

    rate_entry.grid(row=4, column=1)
    rate_label.grid(row=4, column=0)

    which_to_run_entry = ttk.Entry(frame, width=8)
    which_to_run_entry_label = ttk.Label(frame, text='beep, LED, or tone')

    which_to_run_entry.grid(row=5, column=1)
    which_to_run_entry_label.grid(row=5, column=0)

    run_button = ttk.Button(frame, text='Enter Values')
    run_button['command'] = lambda: m2_pixycam_pickup(mqtt_sender, int(speed_slider.get()), direction_box.get(),
                                                           initial_button_entry.get(), rate_entry.get(),
                                                           which_to_run_entry.get())
    run_button.grid(row=7, column=0)
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
def handle_turn_clockwise_using_pixy(mqtt_sender, speed_entry, area_entry):
    print('turn clockwise with speed', speed_entry, 'until area', area_entry)
    mqtt_sender.send_message('turn_clockwise_until_area_is', [speed_entry, area_entry])

def handle_turn_counterclockwise_using_pixy(mqtt_sender, speed_entry, area_entry):
    print('turn counterclockwise with speed', speed_entry, 'until area', area_entry)
    mqtt_sender.send_message('turn_counterclockwise_until_area_is', [speed_entry, area_entry])

def handle_m1_pick_up_using_pixy(mqtt_sender, speed, direction, initial_value, rate_entry,function):
    print(speed, direction, initial_value, rate_entry,function)
    mqtt_sender.send_message('m1_pick_up_using_pixy', [speed, direction, initial_value, rate_entry,function])

def handle_m3_pick_up_pixy(mqtt_sender, speed, direction, initial_value, rate_entry, function):
    print(speed, direction, initial_value, rate_entry, function)
    mqtt_sender.send_message('m3_pick_up_pixy', [speed, direction, initial_value, rate_entry, function])

def handle_go_until_distance_within(mqtt_sender, range_entry, inches_entry, speed_entry):
    print('go until within',range_entry, 'inches of', inches_entry, 'at speed', speed_entry)
    mqtt_sender.send_message('go_until_within_distance', [range_entry, inches_entry, speed_entry])
def handle_backward_until_further_than(mqtt_sender,inches_entry, speed_entry):
    print('go back until distance is bigger than', inches_entry, 'at speed', speed_entry)
    mqtt_sender.send_message('backward_until_further_than', [inches_entry,speed_entry])
def handle_go_until_distance_less_than(mqtt_sender, inches_entry,speed_entry):
    print('go until distance is less than', inches_entry, 'at a speed', speed_entry)
    mqtt_sender.send_message('go_until_distance_less_than', [inches_entry,speed_entry])
def handle_go_until_color_is_not(mqtt_sender, go_until_color_entry, speed_entry):
    print('go until color is not', go_until_color_entry, 'at speed', speed_entry)
    mqtt_sender.send_message('go_until_color_is_not', [go_until_color_entry,speed_entry])
def handle_intensity_bigger_than(mqtt_sender, intensity_entry, speed_entry):
    print('go until intensity greater than', intensity_entry, 'at speed', speed_entry)
    mqtt_sender.send_message('intensity_bigger_than', [intensity_entry, speed_entry])

def handle_go_until_intensity_less_than(mqtt_sender, intensity, speed):
    print('go until intensity is less than', intensity)
    mqtt_sender.send_message('go_straight_until_intensity_is_less_than', [int(intensity), int(speed)])


def handle_go_until_color(mqtt_sender, color, speed):
    print('go until color using the color:  ', color)
    mqtt_sender.send_message('go_until_color', [color,speed])

def handle_m1_pick_up_using_prox(mqtt_sender, initial_button_entry, rate_entry):
    print('m1 pick up using prox', initial_button_entry, rate_entry)
    mqtt_sender.send_message('m1_pick_up_using_prox', [initial_button_entry, rate_entry])
def handle_m3_pick_up_prox(mqtt_sender, initial_button_entry, rate_entry):
    print('m3 pick up object using proximity sensor', initial_button_entry, rate_entry)
    mqtt_sender.send_message('m3_grab_object_LED', [initial_button_entry, rate_entry])

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

##############
#handle tone
###############################################################
def m2_handle_forward_tone(mqtt_sender, frequency, rate):
    print('forward and tone')
    mqtt_sender.send_message("m2_go_forward_tone", [frequency, rate])
def m2_pixycam_pickup(mqtt_sender, speed, direction, initial_value, rate_entry, function):
    print('Got Pixy cam data', speed)
    mqtt_sender.send_message("m2_pick_up_pixy", [speed, direction, initial_value, rate_entry, function])
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
