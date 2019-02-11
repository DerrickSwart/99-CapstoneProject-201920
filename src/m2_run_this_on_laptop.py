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
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, go_for_frame = get_shared_frames(main, mqqt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # : Implement and call get_my_frames(...)
    grid_frames(teleop_frame, arm_frame, control_frame, go_for_frame)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    go_for_frame = shared_gui.get_drive_for_frame(main_frame, mqtt_sender)
    #make_sounds = shared_gui.///(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, go_for_frame


def grid_frames(teleop_frame, arm_frame, control_frame, go_for_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(column=0, row=1)
    control_frame.grid(column=0, row=2)
    go_for_frame.grid(row=3, column=0)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()