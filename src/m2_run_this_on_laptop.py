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
import time

class laptop_delegate(object):
    def __init__(self, frame):
        self.frame = frame
    def display_camera(self, center_x, center_y, width, height):
        """
        Side Effects: Displays a circle on a canvas of where the tennis ball will be
        :param center: Point
        :param width: int
        :param height: int
        :return:Nothing
        """
        x0 = center_x - (width/2)
        y0 = center_y - (height/2)
        x1 = center_x + (width/2)
        y1 = center_y + (height/2)
        frame2 = Frame(self.frame, borderwidth = 5 , relief = 'groove')
        if x0 == 0  and x1 == 0 and y1 == 0 and y0 == 0 :
            Label(frame2, text = "Object NOT in RANGE" ).grid(row=2, column=0)

        print(x0, y0, x1, y1)

        frame2.grid(row=2, column=0)
        canvas = Canvas(frame2, width = 319, height=199)
        canvas.grid(row=0, sticky = E)
        canvas.create_oval(x0, y0, x1, y1)
        time.sleep(0.2)
def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """

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

    ############
    #MQTT Client
    ############
    mqtt_sender = com.MqttClient(laptop_delegate(main))
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # ------------------------------------------------------------------------
    teleop_frame, control_frame = get_shared_frames(main, mqtt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # : Implement and call get_my_frames(...)

    grid_frames(teleop_frame, control_frame)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    fetch_ball = fetch_ball_frame(main, mqtt_sender)
    fetch_ball.grid(row=0, sticky = N+S+E+W)


    deliver = deliver_ball(main, mqtt_sender)
    deliver.grid(sticky=N+S+E+W, row=1)

    temp_canvas = canvas_place_holder(main)
    temp_canvas.grid(sticky=N+S+E+W, row=2)
    # ------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    control = shared_gui.get_control_frame(main_frame, mqtt_sender)
    return teleop_frame, control


def grid_frames(teleop_frame, control):
    teleop_frame.grid(row=0,column=2)
    control.grid(column=2, row=1)


#################################################
#Sprint 3 frames
################################################
def fetch_ball_frame(root_frame, mqtt_sender):
    """
    Side Effects: Creates a beautiful GUI frame for the user to control the EV3 Robot
    It includes calling methods that make the robot act as fetcher for tennis balls

    :param root_frame: tkinter frame
    :param mqtt_sender: mqtt object
    :return: tkinter frame
    """
    frame = Frame(root_frame, relief = 'groove', borderwidth = 10)
    frame.grid(column=0, row=0, sticky=N+S+E+W)
    Grid.columnconfigure(frame, 0, weight=1)
    Grid.rowconfigure(frame, 0, weight=1)
    #Set robot speed

    title_label = Label(frame, text="Tennis Ball Boy Robot Program", font= ("Arial", 16))
    title_label.grid(row=0,column=0, sticky=N+E+S+W)

    fetch_label = Label(frame, text = 'Set Fetch Speed of Robot:', font=("Arial", 12))
    fetch_label.grid(row=1, column=0, sticky=W)

    fetch_speed = Scale(frame, from_ = 5, to=100, orient = HORIZONTAL, length=220, bg="yellow", fg="black")
    fetch_speed.grid(row=1, column =1)

    speak_label = Label(frame, text="Enter a tennis phrase: ", font=("arial", 12))
    speak_label.grid(row=2, sticky=W)

    speak_entry = Entry(frame, width = 40)
    speak_entry.grid(row=2, column = 1)
    speak_entry.insert(0, 'Lets play tennis')

    fetch_button = Button(frame, text="Run Fetch Ball",font=("Arial", 12), activebackground = 'yellow', borderwidth=5, command = lambda: handle_fetch_ball(mqtt_sender, fetch_speed.get(), speak_entry))
    fetch_button.grid(rowspan=3 , sticky=W)

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
    frame.grid(column=0, row=1, sticky=N+S+E+W)
    Grid.rowconfigure(frame, 0, weight=1)
    Grid.columnconfigure(frame, 1, weight=1)

    deliver_label = Label(frame, text = "Deliver the ball, then go back to original position", font=("Arial", 16))
    deliver_label.grid(row=0, column=0)

    slider_label = Label(frame, text="Delivery & return speed: ", font=("Arial", 12))
    slider_label.grid(sticky=W, row=1)

    speed_slider = Scale(frame, from_=5, to=100, orient = HORIZONTAL, length =220, bg="yellow")
    speed_slider.grid(column=1, row=1)

    deliver_button = Button(frame,font=("arial", 12), text = "Deliver and Return", activebackground= 'yellow', borderwidth = 5, command = lambda: handle_deliver_return(mqtt_sender, speed_slider.get()))
    deliver_button.grid(row = 2, sticky=W)

    return frame

def canvas_place_holder(root):
    """
    Side Effects: creates a empty canvas until data is received from the robot
    :param root: tkinter.Frame
    :return: tkinter.Frame
    """
    frame2 = Frame(root, borderwidth=5, relief='groove')
    frame2.grid(row=2, column=0)
    canvas = Canvas(frame2, width=319, height=199)
    canvas.grid(row=0, sticky=E)
    Label(frame2, text="No data received from robot!! \n Connect to display Camera data", font=('arial', 20)).grid(row=2, column=0)
    return frame2



########################################################
#HANLDERS
########################################################
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