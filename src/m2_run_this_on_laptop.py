"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Joseph Conrad.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
from tkinter import *
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqqt_sender = com.MqttClient()
    mqqt_sender.connect_to_ev3()
    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = Tk()
    root.title("FINAL PROJECT ROBOT")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main = Frame(root, relief='groove', borderwidth=5)
    main.grid()
    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # ------------------------------------------------------------------------
    #teleop_frame, arm_frame, control_frame, make_sounds, ir_control = get_shared_frames(main, mqqt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # : Implement and call get_my_frames(...)

    #grid_frames(teleop_frame, arm_frame, control_frame, make_sounds, ir_control)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    ball_boy = ball_boy_frame(main, mqqt_sender)
    ball_boy.grid(column=0, row=0)
    m2_tone_frame = shared_gui.m2_tone_frame(main, mqqt_sender)
    m2_tone_frame.grid(column=1, row=1)
    m2_pixy_frame = shared_gui.m2_pixy_cam(main, mqqt_sender)
    m2_pixy_frame.grid(column=1, row=2)
    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    go_for_frame = shared_gui.get_drive_for_frame(main_frame, mqtt_sender)
    make_sounds = shared_gui.get_sound_request(main_frame, mqtt_sender)
    ir_control = shared_gui.ir_control(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, make_sounds, ir_control


def grid_frames(teleop_frame, arm_frame, control_frame, make_sounds, ir_control):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(column=0, row=1)
    control_frame.grid(column=0, row=2)
    make_sounds.grid(column=0, row=4)
    ir_control.grid(column=1, row=0)

def ball_boy_frame(root_frame, mqtt_sender):
    """
    Side Effects: Creates a beautiful GUI frame for the user to control the EV3 Robot
    It includes calling methods that make the robot act as fetcher for tennis balls

    :param root_frame: tkinter frame
    :param mqtt_sender: mqtt object
    :return: tkinter frame
    """
    frame = Frame(root_frame, relief = 'groove', borderwidth = 10)
    frame.grid()

    #Set robot speed
    fetch_label = Label(frame, text = 'Set Fetch Speed of Robot:')
    fetch_label.grid(row=0, column=0)

    fetch_speed = Scale(frame, from_ = 5, to=100, orient = HORIZONTAL, length=220)
    fetch_speed.grid(row=0, column =1)

    speak_label = Label(frame, text="Enter a tennis phrase: ")
    speak_label.grid(row=1, column=0)
    speak_entry = Entry(frame, width = 40)
    speak_entry.grid(row=1, column = 1)

    fetch_button = Button(frame, text="Run Fetch Ball", activebackground = 'white')
    fetch_button.grid(rowspan=2 )




    return frame

def handle_fetch_ball(mqtt_sender, speed, speak):
    print('sending: ', speed, speak)
    mqtt_sender.send_message("m2_fetch_ball", [speed, speak])

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()