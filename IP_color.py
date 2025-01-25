#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import socket
import requests
from urllib.request import urlopen
from urllib.error import URLError
import re
from tkinter import *
from tkinter import ttk

#Get IP address
def get_IP():
    try:
        print("-------------")
        print("Checking if Internet is up...")
        d = str(urlopen('http://checkip.dyndns.com/').read())
        return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
    except URLError:
        print("Uh-oh. Are you disconnected?")
        return("0.0.0.0")

def get_globale_color():
    glob_ip_address = get_IP()
    glob_ip_address_array = glob_ip_address.split('.')[1:]
    glob_ip_address_color = ''
    for n in glob_ip_address_array:
        hex_val = hex(int(n))[2:]
        if len(hex_val)==1:
            hex_val = "0"+hex_val
        glob_ip_address_color += hex_val
    glob_ip_address_color = '#'+''.join(glob_ip_address_color)
    print(glob_ip_address)
    return [glob_ip_address, glob_ip_address_color]

def get_locale_color():
    loc_ip_address = socket.gethostbyname(socket.gethostname())
    loc_ip_address_array = loc_ip_address.split('.')[1:]
    loc_ip_address_color = ''
    for n in loc_ip_address_array:
        hex_val = hex(int(n))[2:]
        if len(hex_val)==1:
            hex_val = "0"+hex_val
        loc_ip_address_color += hex_val
    loc_ip_address_color = '#'+''.join(loc_ip_address_color)
    print(loc_ip_address)
    return [loc_ip_address, loc_ip_address_color]

def update():
    global_ip = get_globale_color()
    locale_ip = get_locale_color()
    loc_label['text'] = f"Addresse Locale: {locale_ip[0]}"
    glob_label['text'] = f"Addresse Global: {global_ip[0]}"
    glob_canvas['bg'] = global_ip[1]
    loc_canvas['bg'] = locale_ip[1]
    root.after(2000, update)

#Create and manage window
root = Tk()
root.title("IP Colored ☻")
root.config(bg="skyblue")
root.resizable(False, False)

global_ip = ["checking internet", "#f0f0f0"]
locale_ip = ["checking internet", "#f0f0f0"]

loc_canvas = Canvas(root, width=180, height=200, bg=locale_ip[1])
loc_canvas.grid(column=0, row=0, padx=10, pady=10)
loc_label = Label(root, text=f"Addresse Locale: {locale_ip[0]}")
loc_label.grid(column=0, row=1)

glob_canvas = Canvas(root, width=180, height=200, bg=global_ip[1])
glob_canvas.grid(column=1, row=0, padx=10, pady=10)
glob_label = Label(root, text=f"Addresse Global: {global_ip[0]}")
glob_label.grid(column=1, row=1)


update()
root.mainloop()
