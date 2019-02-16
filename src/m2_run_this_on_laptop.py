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


class laptop_delegate(object):
    def __init__(self, frame):
        self.frame = frame
    def display_camera(self, blob):
        """
        Side Effects: Displays a circle on a canvas of where the tennis ball will be
        :param blob: Blob
        :return:Nothing
        """
        x0 = blob.center.x - (blob.width/2)
        y0 = blob.center.y - (blob.height/2)
        x1 = blob.center.x + (blob.width/2)
        y1 = blob.center.y + (blob.height/2)

        frame2 = Frame(self.frame, borderwidth = 5 , relief = 'groove')
        canvas = Canvas(frame2, width = 319, height=199)
        canvas.grid(row=0, sticky = E)
        canvas.create_oval(x0, y0, x1, y1)

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
    root.title("Tennis Ball Boy Controller")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main = Frame(root, relief='groove', borderwidth=5)
    main.grid()

    mqtt_receiver = com.MqttClient(laptop_delegate(main))
    mqtt_receiver.connect_to_ev3()
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
    fetch_ball = fetch_ball_frame(main, mqqt_sender)
    fetch_ball.grid(row=0, sticky = W)

    deliver = deliver_ball(main, mqqt_sender)
    deliver.grid(sticky=W, row=1)

    #m2_tone_frame = shared_gui.m2_tone_frame(main, mqqt_sender)
    #m2_tone_frame.grid(column=1, row=1)
    #m2_pixy_frame = shared_gui.m2_pixy_cam(main, mqqt_sender)
    #m2_pixy_frame.grid(column=1, row=2)
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

def fetch_ball_frame(root_frame, mqtt_sender):
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
    speak_label.grid(row=1, sticky=W)

    speak_entry = Entry(frame, width = 40)
    speak_entry.grid(row=1, column = 1)

    fetch_button = Button(frame, text="Run Fetch Ball", activebackground = 'white', borderwidth=5, command = lambda: handle_fetch_ball(mqtt_sender, fetch_speed.get(), speak_entry))
    fetch_button.grid(rowspan=2 , sticky=W)

    return frame

def deliver_ball(root, mqtt_sender):
    """
    Side Effects: Creates a beautiful GUI frame for the user to control the EV3 Robot
    It includes calling methods that make the robot act as fetcher for tennis balls

    :param root: tkinter frame
    :param mqtt_sender:  mqtt object
    :return: tkinter frame
    """
    frame = Frame(root, relief = 'groove', borderwidth = 10)
    frame.grid()

    deliver_label = Label(frame, text = "Deliver the ball, then go back to original position")
    deliver_label.grid(row=0, column=0)

    slider_label = Label(frame, text="Delivery & return speed: ")
    slider_label.grid(sticky=W, row=1)

    speed_slider = Scale(frame, from_=5, to=100, orient = HORIZONTAL, length =220)
    speed_slider.grid(column=1, row=1)

    deliver_button = Button(frame, text = "Deliver and Return",borderwidth = 5, command = lambda: handle_deliver_return(mqtt_sender, speed_slider.get()))
    deliver_button.grid(row = 2, sticky=W)

    return frame




def handle_fetch_ball(mqtt_sender, speed, speak):
    """
    Side Effects: Sends an mqtt message to the robot with the passed in data
    :param mqtt_sender: mqtt object
    :param speed: string
    :param speak: tkinter Entry object
    :return: Nothing
    """
    print('sending: ', speed, speak.get())
    mqtt_sender.send_message("m2_fetch_ball", [speed, speak.get()])
    speak.delete(0, len(speak.get()))

def handle_deliver_return(mqtt_sender, speed):
    """
    Side Effects: Sends an mqtt message to the robot with the passed in data
    :param mqtt_sender: mqtt object
    :param speed: string
    :return: Nothing
    """
    print('handling deliver and return', speed)
    mqtt_sender.send_message("m2_deliver_ball", [speed])



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()