'''
Created on 14 Jun 2016

@author: HOLLDAV

TrackWise Services Management Utility
'''
# from urllib.request import urlopen
import sys
from server.server import Server
from tkinter import Tk, StringVar, Menu, W
from tkinter.ttk import Label, LabelFrame, Button

#
# Initialize the presentation routines
#
win = Tk()

#
# Global textvariables
#  
snv = StringVar()
stv = StringVar()
lbv = StringVar()

#
# Routines to do the screen handling
#
def serverpanel(server):
    ''' Draws the top panel with the server information '''
    serverpanel = LabelFrame(win, text = "Server Details")
    serverpanel.grid(column = 0, row = 0, padx = 5, pady = 5)
    snamelbl = Label(serverpanel, text = "Server Name: ").grid(column = 0, row = 0, sticky = W)
    stypelbl = Label(serverpanel, text = "Server Type: ").grid(column = 0, row = 1, sticky = W)
    loadballbl = Label(serverpanel, text = "Load Balancer Status: ").grid(column = 0, row = 2, sticky = W)
    sname = Label(serverpanel, textvariable = snv).grid(column = 1, row = 0, sticky = W)
    stype = Label(serverpanel, textvariable = stv ).grid(column = 1, row = 1, sticky = W)
    loadbal = Label(serverpanel, textvariable = lbv).grid(column = 1, row = 2, sticky = W)
    serverstatus(server)

def serverstatus(server):
    ''' Sets the  server status text variables ''' 
    snv.set(server.gethostname())
    stv.set(server.gettype())
    lbv.set("Future Release")
    

def servicepanel():
    ''' Draws the panel with the service information '''
    servicepanel = LabelFrame(win, text = "Service Details")
    servicepanel.grid(column = 0, row = 1, padx = 5, pady = 5)

def buttonpanel():
    ''' Draws the panel with the buttons at the bottom '''
    pass

def menubar():
    ''' Draws the menu bar '''

def main():

    #
    # Initialize the server object
    #
    server = Server()
    
    menubar()
    serverpanel(server)
    servicepanel()
    buttonpanel()
   
    win.mainloop()

    sys.exit(0)
    

if __name__ == '__main__':
    main()
