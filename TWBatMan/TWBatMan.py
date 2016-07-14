'''
Created on 14 Jun 2016

@author: HOLLDAV

TrackWise Services Management Utility
'''
# from urllib.request import urlopen
import sys
from server.server import Server
from tkinter import Tk, StringVar, Menu, W, E
from tkinter.ttk import Label, LabelFrame, Button
# import logging
# import time as t
# logger = logging.getLogger('TWBatMan')
# logger.setLevel(logging.DEBUG)
# logfh = logging.FileHandler('TWBatMan.log')
# logfh.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logfh.setFormatter(formatter)
# logger.addHandler(logfh)

#
# Initialize the server object
#
server = Server()

#
# Initialize the presentation routines
#
win = Tk()

#
# Global variables
#  
snv = StringVar()
stv = StringVar()
lbv = StringVar()
servv = {}
servlbl = {}
status = StringVar()
spanel = ""

#
# Routines to do the screen handling
#
def serverpanel(server):
    ''' Draws the top panel with the server information '''
    serverpanel = LabelFrame(win, text = "Server Details")
    serverpanel.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = W+E)
    Label(serverpanel, text = "Server Name: ").grid(column = 0, row = 0, sticky = W)
    Label(serverpanel, text = "Server Type: ").grid(column = 0, row = 1, sticky = W)
    Label(serverpanel, text = "Load Balancer Status: ").grid(column = 0, row = 2, sticky = W)
    Label(serverpanel, textvariable = snv).grid(column = 1, row = 0, sticky = W)
    Label(serverpanel, textvariable = stv ).grid(column = 1, row = 1, sticky = W)
    Label(serverpanel, textvariable = lbv).grid(column = 1, row = 2, sticky = W)
    serverstatus(server)

def serverstatus(server):
    ''' Sets the  server status text variables ''' 
    snv.set(server.gethostname())
    stv.set(server.gettype())
    lbv.set(server.lbstatus())
    

def servicepanel(server):
    ''' Draws the panel with the service information '''
    global servv, spanel
    servicepanel = LabelFrame(win, text = "Service Details")
    servicepanel.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = W+E)
    
    services = server.getservices()
    scount = 0
    for service in services:
        servv[service] = StringVar()
        Label(servicepanel, text = service + ": ").grid(column = 0, row = scount, sticky = W)

        Label(servicepanel, textvariable = servv[service]).grid(column = 1, row = scount, sticky = W)
        servicestatus(server, service)
        scount += 1
        
    spanel = Label(servicepanel, textvariable = status).grid(column = 0, row = scount + 1, columnspan = 2, sticky = W)
    status.set("")
        
def servicestatus(server, service):
    ''' Refreshes the status of a service and updates the relevant text variable '''
    global servv
    servv[service].set(server.onStatus(service))
        
def onStop():
    status.set("Stopping Services...")
    win.update_idletasks()
    for sname in server.getservices():
        server.stopService(sname)
        servicestatus(server, sname)
    status.set("")
    win.update_idletasks()
        
def onStart():
    status.set("Starting Services...")
    win.update_idletasks()
    for sname in server.getservices():
        server.startService(sname)
        servicestatus(server, sname)
    status.set("")
    win.update_idletasks()
    
def onStatus():
    for sname in server.getservices():
        servv[sname].set(server.onStatus(sname))
    win.update_idletasks()    
    

def buttonpanel():
    ''' Draws the panel with the buttons at the bottom '''
    butpanel = LabelFrame(win, text = "")
    butpanel.grid(column = 0, row = 2, padx = 5, pady = 5, sticky = W+E)
    Button(butpanel, text = "Stop Services", command = onStop).grid(column = 0, row = 0)
    Button(butpanel, text = "Start Services", command = onStart).grid(column = 1, row = 0)
    Button(butpanel, text = "Refresh List", command = onStatus).grid(column = 2, row = 0)
    
    if server.lbalanced.upper() == "YES":
        # lbutpanel = LabelFrame(win, text = "")
        # lbutpanel.grid(column = 0, row = 3, padx = 5, pady = 5, sticky = W+E)
        Button(butpanel, text = "Stop Load Balancer", command = lbStop).grid(column = 0, row = 1)
        Button(butpanel, text = "Start Load Balancer", command = lbStart).grid(column = 1, row = 1)
        

def menubar(server):
    ''' Draws the menu bar '''
    menubar = Menu(win)
    fileMenu = Menu(menubar)
    fileMenu.add_command(label = "Exit", command = win.quit)
    menubar.add_cascade(label = "File", menu = fileMenu)

    svcsMenu = Menu(menubar)
    svcsMenu.add_command(label = "List Service Status", command = onStatus)
    svcsMenu.add_command(label = "Stop Services", command = onStop)
    svcsMenu.add_command(label = "Start Services", command = onStart)
    menubar.add_cascade(label = "Services", menu = svcsMenu)
    
    if server.lbalanced.upper() == "YES":
        lbMenu = Menu(menubar)
        menubar.add_cascade(label = "Load Balancer", menu = lbMenu)
        lbMenu.add_command(label = "Stop Load Balancer", command = lbStop)
        lbMenu.add_command(label = "Start Load Balancer", command = lbStart)
    
    win.config(menu = menubar)

def lbStop():
    ''' Stop the load balancer '''
    server.lbStop()
    lbv.set(server.lbstatus())

def lbStart():
    ''' Start the load balancer '''
    server.lbStart()
    lbv.set(server.lbstatus())    

def main():

    serverpanel(server)
    servicepanel(server)
    buttonpanel()
    menubar(server)
   
    win.mainloop()

    sys.exit(0)
    

if __name__ == '__main__':
    main()
