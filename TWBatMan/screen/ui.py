from tkinter import Tk, Text, BOTH, RIGHT, TOP, X, N, LEFT, RAISED, Listbox, StringVar, END, Menu, W, Message
from tkinter.ttk import Frame, Button, Style, Label, Entry 

class Ui(Frame):
    """The user interface class"""

    def __init__(self, parent, server):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI(server)

    def initUI(self, server):
      
        self.parent.title("TrackWise Service Manager")
        self.pack(fill=BOTH, expand = True)
        # self.centerWindow()

        menubar = Menu(self.parent)
        self.parent.config(menu = menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label = "Exit", command = self.onExit)
        menubar.add_cascade(label = "File", menu = fileMenu)

        svcsMenu = Menu(menubar)
        svcsMenu.add_command(label = "List Service Status", command = self.onStatus)
        svcsMenu.add_command(label = "Stop Services", command = self.onStop)
        svcsMenu.add_command(label = "Start Services", command = self.onStart)
        menubar.add_cascade(label = "Services", menu = svcsMenu)

        # svcs = ['TrackWise Tomcat', 'Web Services Tomcat', 'QMD Tomcat', 'Keystone Intake', 'ID Intake', 'TWC']
        svcs = server.getservices()

        frame1 = Frame(self, borderwidth = 1)
        frame1.pack(fill = X, anchor = W)

        l = StringVar()
        label1 = Message(frame1, textvariable = l , anchor = W)
        
        svcscount = 0

        lstr = "Service Status\n\n"

        for i in svcs:
            svcscount += 1 
            lstr += '{} - '.format(i) + ('UP\n' if svcscount % 2 else 'DOWN\n')
      
            
        l.set(lstr)
        label1.pack(side=TOP, padx = 5, pady = 5)   

        frame4 = Frame(self, relief=RAISED, borderwidth = 1)
        frame4.pack(fill = X)
        closeButton = Button(frame4, text="Close", command = self.quit)
        closeButton.pack(side = RIGHT, padx = 5, pady = 5)
        okButton = Button(frame4, text = "OK")
        okButton.pack(side = RIGHT) 

    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)      

    def onExit(self):
        self.quit()

    def onStatus(self):
        pass

    def onStop(self):
        pass

    def onStart(self):
        pass



