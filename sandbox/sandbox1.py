# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

# Derrick Swart

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

def camara_conrtol_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text = 'camara control')
    frame_label.grid(row = 0, column = 0)

    speed_entry = ttk.Entry(frame, width = 8)
    speed_entry_label = ttk.Label(frame, text = 'enter speed, 0-100')
    speed_entry.grid(row = 1,column = 0)
    speed_entry_label.grid(row = 1, column = 1)

    area_entry = ttk.Entry(frame, width = 8)
    area_entry_label = ttk.Label(frame, text = 'enter speed, 0-100')
    area_entry.grid(row = 2,column = 0)
    area_entry_label.grid(row = 2, column = 1)

    clockwise_button = ttk.Button(frame, text = 'turn clockwise')
    counterclockwise_button = ttk.Button(frame, text = ' turn counterclockwise')
    clockwise_button['command'] = lambda: handle_turn_clockwise_using_pixy(mqtt_sender, speed_entry.get(),
                                                                           area_entry.get())
    counterclockwise_button['command']= lambda: handle_turn_counterclockwise_using_pixy(mqtt_sender, speed_entry.get(),
                                                                                        area_entry.get())
    clockwise_button.grid(row= 1, column = 3)
    counterclockwise_button.grid(row = 2, column = 3)


def handle_turn_clockwise_using_pixy(mqtt_sender, speed_entry, area_entry):
    print('turn clockwise with speed', speed_entry, 'until area', area_entry)
    mqtt_sender.send_message('turn_clockwise_until_area_is', [speed_entry, area_entry])

def handle_turn_counterclockwise_using_pixy(mqtt_sender, speed_entry, area_entry):
    print('turn counterclockwise with speed', speed_entry, 'until area', area_entry)
    mqtt_sender.send_message('turn_counterclockwise_until_area_is', [speed_entry, area_entry])
