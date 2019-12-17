#!/usr/bin/python3
from gui import gui
import home

""" SmartHome application entry point
"""

def main():
    print("python main function")
    my_home = home.Home()
    my_gui = gui.GUI(my_home)
    my_gui.start()
    #things_comm = ThingsInbound()
    #server_comm = ServerInbound(home)

    #try:
        #start_new_thread(things_comm.start, ())
        #start_new_thread(server_comm.start, ())
     #   start_new_thread(gui.start, ())
    #except Exception as ex:
     #   print("Error: unable to start thread. ex: {}".format(ex))

    #while home.is_ended():
    #    pass


if __name__ == '__main__':
    main()
