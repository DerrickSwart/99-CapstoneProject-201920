"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Derrick Swart.
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
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title('Derrick Swart: CSSE 120 Capstone Project')



    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding = 20, borderwidth = 5, relief = 'groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, go_for_frame, ir_frame, prox_control_frame, sound_control, pixy_control = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    m1_pick_up_objects, m1_find_with_pixy_using_color = get_my_frames(main_frame, mqtt_sender)
    m1_pick_up_objects.grid(row = 1, column = 1)
    m1_find_with_pixy_using_color.grid(row = 3, column = 1)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, go_for_frame, ir_frame, prox_control_frame, sound_control, pixy_control)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------


    root.mainloop()


"""
creates a new GUI for my specific part of the 
"""
def my_main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title('Derrick Swart: CSSE 120 Capstone Project Sprint 3')

    main_frame = ttk.Frame(root, padding=20, borderwidth=5, relief='groove')
    main_frame.grid()

    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    my_ball_frame = get_ball_frame(main_frame, mqtt_sender)







    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    my_ball_frame.grid(row = 0, column = 1)

    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    go_for_frame = shared_gui.get_drive_for_frame(main_frame, mqtt_sender)
    ir_frame = shared_gui.ir_control(main_frame, mqtt_sender)
    proximity_control_frame = shared_gui.proximity_control_frame(main_frame,mqtt_sender)
    sound_control = shared_gui.get_sound_request(main_frame, mqtt_sender)
    pixy_control = shared_gui.camara_conrtol_frame(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, go_for_frame, ir_frame, proximity_control_frame, sound_control, pixy_control



def grid_frames(teleop_frame, arm_frame, control_frame, go_for_frame, ir_frame, prox_control_frame, sound_control, pixy_control):
    teleop_frame.grid(row = 0, column = 0)
    arm_frame.grid(row = 1, column = 0)
    control_frame.grid(row = 2, column = 0)
    go_for_frame.grid(row = 3, column = 0)
    ir_frame.grid(row = 4, column = 0)
    prox_control_frame.grid(row = 0, column =1)
    sound_control.grid(row = 2, column = 1)
    pixy_control.grid(row=4, column = 1)


def get_my_frames(main_frame, mqtt_sender):
    m1_pick_up_objects = shared_gui.M1_pick_up_objects(main_frame, mqtt_sender)
    m1_find_with_pixy_using_color = shared_gui.m1_find_with_pixy_using_color(main_frame, mqtt_sender)
    return  m1_pick_up_objects, m1_find_with_pixy_using_color


def get_ball_frame(main_frame, mqtt_sender):
    frame = ttk.Frame(main_frame, padding=10, borderwidth=5, relief='groove')
    frame.grid()
    frame_label = ttk.Label(frame, text='m1 find and pickup an object using pixy')
    frame_label.grid(row=0, column=0)

    scale = ttk.Scale(frame, from_=10, to=100)
    speed_label = ttk.Label(frame, text='speed from 10-100 respectivly')
    speed_label.grid(row=1, column=0)
    scale.grid(row=1, column=1)

    direction_box = ttk.Entry(frame, width=8)
    direction_box_label = ttk.Label(frame, text='enter direction, CCW or CW')
    direction_box_label.grid(row=2, column=0)
    direction_box.grid(row=2, column=1)

    initial_button_label = ttk.Label(frame, text="enter initial value")
    initial_button_entry = ttk.Entry(frame, width=8)

    initial_button_entry.grid(row=3, column=1)
    initial_button_label.grid(row=3, column=0)

    rate_entry = ttk.Entry(frame, width=8)
    rate_label = ttk.Label(frame, text='rate of increase')

    rate_entry.grid(row=4, column=1)
    rate_label.grid(row=4, column=0)

    which_to_run_entry = ttk.Entry(frame, width=8)
    which_to_run_entry_label = ttk.Label(frame, text='enter beep, LED, or tone to call that function')

    which_to_run_entry.grid(row=5, column=1)
    which_to_run_entry_label.grid(row=5, column=0)

    run_button = ttk.Button(frame, text='run')
    run_button.grid(row=7, column=0)
    run_button['command'] = lambda: handler_find_ball(mqtt_sender,scale.get(), direction_box.get(),
                                                                 initial_button_entry.get(), rate_entry.get(),
                                                                 which_to_run_entry.get())
    return frame


"""
Handlers for the final sprints frame
"""
def handler_find_ball(mqtt_sender, speed, direction, initial_value, rate_entry):
    print(speed, direction, initial_value, rate_entry)
    mqtt_sender.send_message('m1_pick_up_using_pixy', [speed, direction, initial_value, rate_entry,])
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
#main()
my_main()