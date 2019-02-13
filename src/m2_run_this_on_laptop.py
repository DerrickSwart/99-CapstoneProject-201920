"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Joseph Conrad.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
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
    root = tkinter.Tk()
    root.title("FINAL PROJECT ROBOT")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main = ttk.Frame(root, relief='groove', borderwidth=5, padding =10)
    main.grid()
    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # ------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, go_for_frame, make_sounds, ir_control = get_shared_frames(main, mqqt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # : Implement and call get_my_frames(...)
    grid_frames(teleop_frame, arm_frame, control_frame, go_for_frame, make_sounds, ir_control)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    frame = ttk.Frame(main, relief = 'groove', borderwidth = 5, padding = 10)
    frame.grid(column=1, row = 1)
    init_label = ttk.Label(frame, text='Initial Frequency')
    init_label.grid(column=0, row=0)
    init_entry = ttk.Entry(frame, width = 8)
    init_entry.grid(column=0, row=1)
    increase_label = ttk.Label(frame, text='Increase Rate')
    increase_label.grid(column=1, row=0)
    increase_entry = ttk.Entry(frame, width = 8)
    increase_entry.grid(column=1, row=1)
    submit_button = ttk.Button(frame, text='Go Forward Beeping Faster')
    submit_button.grid(rowspan=2)
    submit_button['command'] = lambda: go_forward_beeping_faster(mqqt_sender, init_entry.get(), increase_entry.get())
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
    return teleop_frame, arm_frame, control_frame, go_for_frame, make_sounds, ir_control


def grid_frames(teleop_frame, arm_frame, control_frame, go_for_frame, make_sounds, ir_control):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(column=0, row=1)
    control_frame.grid(column=0, row=2)
    go_for_frame.grid(row=3, column=0)
    make_sounds.grid(column=0, row=4)
    ir_control.grid(column=1, row=0)

def go_forward_beeping_faster(mqqt_sender, initial_freq, increase_rate):
    mqqt_sender.send_message('go_forward_tone' , [int(initial_freq), int(increase_rate)])
    print('sent message', initial_freq, increase_rate)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()