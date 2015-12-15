# Name:     pc_led_control.py
# Author:   Steven Liu (steven261715@gmail.com)
# Date:     12/14/2015

from tkinter import *
import serial
import time

serialBT = serial.Serial(3, 9600, timeout=10)   # open com4 for BT communication

def send_to_BT(cmd):
    # serialBT = serial.Serial(3, 9600, timeout=10)
    cmd = cmd + "\n"
    cmd_bytes = cmd.encode('utf-8')
    print(cmd_bytes)
    serialBT.write(cmd_bytes)
    # time.sleep(1)
    # serialBT.close()

main_window = Tk()

# button for turn on red led
red_led_on_button = Button(main_window, text="RED_ON", command=lambda: send_to_BT("R00"))
red_led_on_button.grid(row=0, column=0)
red_led_on_button.config(height = 1, width = 10)

# button for turn off red led
red_led_off_button = Button(main_window, text="RED_OFF", command=lambda: send_to_BT("R10"))
red_led_off_button.grid(row=1, column=0)
red_led_off_button.config(height = 1, width = 10)

# text entry for red led blink time interval
red_led_blink_entry = Entry(main_window)
red_led_blink_entry.grid(row=2, column=1)
red_led_blink_entry.config(width = 5)
red_led_blink_entry.delete(0, END)
red_led_blink_entry.insert(0, "1")

# button for red led blink
red_led_blink_button = Button(main_window, text="RED_BLINK", command=lambda: send_to_BT("R0" + red_led_blink_entry.get()))
red_led_blink_button.grid(row=2, column=0)
red_led_blink_button.config(height = 1, width = 10)

# button for turn on green led
green_led_on_button = Button(main_window, text="GREEN_ON", command=lambda: send_to_BT("G00"))
green_led_on_button.grid(row=3, column=0)
green_led_on_button.config(height = 1, width = 10)

# button for turn off green led
green_led_off_button = Button(main_window, text="GREEN_OFF", command=lambda: send_to_BT("G10"))
green_led_off_button.grid(row=4, column=0)
green_led_off_button.config(height = 1, width = 10)

# text entry for green led blink time interval
green_led_blink_entry = Entry(main_window)
green_led_blink_entry.grid(row=5, column=1)
green_led_blink_entry.config(width = 5)
green_led_blink_entry.delete(0, END)
green_led_blink_entry.insert(0, "1")

# button for green led blink
green_led_blink_button = Button(main_window, text="GREEN_BLINK", command=lambda: send_to_BT("G0" + green_led_blink_entry.get()))
green_led_blink_button.grid(row=5, column=0)
green_led_blink_button.config(height = 1, width = 10)

# button for turn on blue led
blue_led_on_button = Button(main_window, text="BLUE_ON", command=lambda: send_to_BT("B00"))
blue_led_on_button.grid(row=6, column=0)
blue_led_on_button.config(height = 1, width = 10)

# button for turn off blue led
blue_led_off_button = Button(main_window, text="BLUE_OFF", command=lambda: send_to_BT("B10"))
blue_led_off_button.grid(row=7, column=0)
blue_led_off_button.config(height = 1, width = 10)

# text entry for blue led blink time interval
blue_led_blink_entry = Entry(main_window)
blue_led_blink_entry.grid(row=8, column=1)
blue_led_blink_entry.config(width = 5)
blue_led_blink_entry.delete(0, END)
blue_led_blink_entry.insert(0, "1")

# button for blue led blink
blue_led_blink_button = Button(main_window, text="BLUE_BLINK", command=lambda: send_to_BT("B0" + blue_led_blink_entry.get()))
blue_led_blink_button.grid(row=8, column=0)
blue_led_blink_button.config(height = 1, width = 10)

# serialBT.close()
