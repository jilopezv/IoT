#!/usr/bin/python3
from _thread import start_new_thread

from gui import gui
import home
from server_comm.server_inbound import ServerInbound
from things_comm.things_inbound import ThingsInbound

""" SmartHome application entry point
"""

def main():
    print("python main function")
    my_home = home.Home()
    my_gui = gui.GUI(my_home)
    things_comm = ThingsInbound(my_home)
    #server_comm = ServerInbound(my_home)

    try:
        start_new_thread(things_comm.start, ())
        #start_new_thread(server_comm.start, ())
        #start_new_thread(gui.start, ())
    except Exception as ex:
        print("Error: unable to start thread. ex: {}".format(ex))

    my_gui.start()
    #while my_home.is_ended():
    #    pass


if __name__ == '__main__':
    main()
