#!/usr/bin/python3
from _thread import start_new_thread
from InternalComm import ThingsComm
from ExternalComm import ExternalComm
from Home import Home
from GUI import GUI

""" SmartHome application entry point
"""

home = Home()
thingServer = ThingsComm()
remoteComm = ExternalComm(home)
gui = GUI(home)

try:
    start_new_thread(thingServer.start, ())
    start_new_thread(remoteComm.start, ())
    start_new_thread(gui.start, ())
except Exception as ex:
    print("Error: unable to start thread. ex: {}".format(ex))

while home.is_ended():
    pass
