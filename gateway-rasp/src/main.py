#!/usr/bin/python3
import sys
from _thread import start_new_thread

from gui import smart_home
import home
from server_comm.server_inbound import ServerInbound
from things_comm.things_inbound import ThingsInbound
import os
from os.path import join, dirname
from dotenv import load_dotenv

""" SmartHome application entry point
"""


def main():
    env = 'dev'
    for arg in sys.argv[1:]:
        if arg == 'prod':
            env = 'prod'
    dotenv_path = join(dirname(__file__), env + '.env')
    load_dotenv(dotenv_path)

    print("python main function")
    my_home = home.Home()
    my_gui = smart_home.SmartHome(my_home)
    things_comm = ThingsInbound(my_home)
    server_comm = ServerInbound(my_home)

    try:
        start_new_thread(things_comm.start, ())
        start_new_thread(server_comm.start, ())
        # start_new_thread(gui.start, ())
    except Exception as ex:
        print("Error: unable to start thread. ex: {}".format(ex))

    my_gui.run()
    # while my_home.is_ended():
    #    pass


if __name__ == '__main__':
    main()
