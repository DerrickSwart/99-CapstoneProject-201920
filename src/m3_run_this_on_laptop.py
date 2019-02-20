"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Joshua Giambattista.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
import rosebot

def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """


    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("Joshua")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    frame = ttk.Frame(root, padding = 10, borderwidth=5, relief = "groove")
    frame.grid()
    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, go_for_frame, make_sounds, ir_frame, proximity_control_frame = get_shared_frames(frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    pick_up_prox_frame, pick_up_pixy_frame = get_my_frames(frame, mqtt_sender)
    pick_up_prox_frame.grid(row=2, column = 1)
    pick_up_pixy_frame.grid(row=3,column = 1)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, go_for_frame, make_sounds, ir_frame, proximity_control_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

def mario_kart_frame(frame, mqtt_sender):
    frame = ttk.Frame(frame, padding=10, borderwidth=5, relief='groove')
    frame.grid()
    frame_label = ttk.Label(frame, text='Mario Kart')
    frame_label.grid(row=0, column=0)

    turning_scale = ttk.Scale(frame, from_= 0, to = 100)
    turning_scale.grid(row=1, column = 0)
    turning_scale.set(50)
    options = ['Pick Motor Speed', '50CC', '100CC', '150CC']
    value = tkinter.StringVar()
    value.set(options[0])
    dropdown_menu = ttk.OptionMenu(frame, value, *options)
    dropdown_menu.grid(row=2, column=0)
    #dropdown_label = ttk.Label(frame, text='pick a color goal to stop at')
    #dropdown_label.grid(row=2, column=1)

    return frame

def get_shared_frames(frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(frame, mqtt_sender)
    go_for_frame = shared_gui.get_drive_for_frame(frame, mqtt_sender)
    make_sounds = shared_gui.get_sound_request(frame, mqtt_sender)
    ir_frame = shared_gui.ir_control(frame, mqtt_sender)
    proximity_control_frame = shared_gui.proximity_control_frame(frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, go_for_frame, make_sounds, ir_frame, proximity_control_frame

def grid_frames(teleop_frame, arm_frame, control_frame, go_for_frame, make_sounds, ir_frame, proximity_control_frame):
    teleop_frame.grid(row=0, column = 0)
    arm_frame.grid(row=1, column = 0)
    control_frame.grid(row=2, column = 0)
    go_for_frame.grid(row=3, column=0)
    make_sounds.grid(row = 4, column = 0)
    ir_frame.grid(row=0, column = 1)
    proximity_control_frame.grid(row=1, column = 1)
def get_my_frames(frame, mqtt_sender):
    pick_up_prox_frame= shared_gui.m3_pick_up_prox_frame(frame, mqtt_sender)
    pick_up_pixy_frame = shared_gui.m3_pick_up_pixy_frame(frame, mqtt_sender)
    return pick_up_prox_frame, pick_up_pixy_frame


def final_project():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    root = tkinter.Tk()
    root.title('Joshua Giambattista')

    main_frame = ttk.Frame(root, padding=20, borderwidth=5, relief='groove')
    main_frame.grid()

    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    make_sounds = shared_gui.get_sound_request(main_frame, mqtt_sender)
    mario_kart = mario_kart_frame(main_frame, mqtt_sender)
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    make_sounds.grid(row=3, column = 0)
    mario_kart.grid(row=4, column = 0)


    root.mainloop()

def handler_main_function(mqtt_sender, motor_speed, speed_right, speed_left):
    print(motor_speed, speed_right, speed_left)
    mqtt_sender.send_message('m3_main_function', [motor_speed, speed_right, speed_left])
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
#main()

final_project()