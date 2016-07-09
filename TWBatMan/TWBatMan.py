'''
Created on 14 Jun 2016

@author: HOLLDAV

TrackWise Services Management Utility
'''
# from urllib.request import urlopen
import sys
from server.server import Server
from screen import ui
from tkinter import Tk

#
# Initialize the presentation routines
#
root = Tk()
# uscreen = ui.Ui(root)

#===============================================================================
# def menu(server):
#     ''' Handle the menu and processing '''
#     
#     mymess = []
#     countup, countdown = 0, 0
#     # screen.drawheader(server.gethostname(), server.gettype())
#         
#     # print ("{} Services defined".format(len(services)))
#     services = server.getservices()
#     mymess.append("Services Defined: {}".format(len(services)))
#     
#     for sname in services:
#         if server.service_status(sname) == 1:
#             status = "RUNNING"
#             countup += 1
#         else:
#             status = "STOPPED"
#             countdown += 1
#             
#         # print("Service {} is {}".format(sname, status))
#         
#     su = 'service is' if countup == 1 else 'services are'
#     sd = 'service is' if countdown == 1 else 'services are'
#     # print ("{0} {2} up - {1} {3} down".format(countup, countdown, su, sd))
#     # mymess.append("{0} {2} up - {1} {3} down".format(countup, countdown, su, sd))
#     mymess.append("Services Up: {}".format(countup))
#     mymess.append("Services Down: {}".format(countdown))
#     mymess.append("Load Balancer Status: ")
#     #screen.drawsstate(mymess)
#     #choice = screen.drawoptions()
#     
#     return(choice)
#===============================================================================

def main():
    
    #
    # Parse the XML service details and get the services for this hostname
    #
    #services = ET.parse("twbatman.xml")
    #root = services.getroot()
    #hostname = gethostname()
    #servertype, services = get_services(root, hostname)

    server = Server()
    uscreen = ui.Ui(root, server)
    #===========================================================================
    # hostname = server.gethostname()
    # servertype = server.gettype()
    # servicelist = server.getservices()
    #===========================================================================

    root.mainloop()
    
    #while menu(server):
    #    pass
    
    sys.exit(0)
    

if __name__ == '__main__':
    main()
