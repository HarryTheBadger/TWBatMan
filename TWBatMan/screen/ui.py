from tkinter import Tk, Text, BOTH, RIGHT, TOP, X, N, LEFT, RAISED, Listbox, StringVar, END, Menu, W, Message
from tkinter.ttk import Frame, Button, Style, Label, Entry, Labelframe

class Ui(Frame):
    """The user interface class"""

    def __init__(self, parent, server):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI(server)

    def initUI(self, server):
      
        self.parent.title("TrackWise Service Manager")
        self.pack(fill=BOTH, expand = True, padx = 300)
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
        hostname = server.gethostname().strip()
        servertype = server.gettype().strip()

        frame0 = Labelframe(self, text = "Server Details",  borderwidth = 1)
        frame0.grid(column = 0, row = 0, sticky = W)
        
        so = StringVar()
        svroverview = Message(frame0, textvariable = so, anchor = W, width = 300)
        svroverview.grid(column = 0, row = 0)
        sstr = "Server: {}\n".format(hostname)
        sstr += "Server Type: {}".format(servertype)
        so.set(sstr)
        
        
        frame1 = Labelframe(self, text = "Service Status", borderwidth = 1)
        frame1.grid(column = 0, row = 1, sticky = W)


        l = StringVar()
        label1 = Message(frame1, textvariable = l , anchor = W)
        
        svcscount = 0

        lstr = ""

        for i in svcs:
            svcscount += 1 
            lstr += '{} - '.format(i) + ('UP\n' if svcscount % 2 else 'DOWN\n')
      
            
        l.set(lstr)
        label1.pack(side=TOP, padx = 5, pady = 5)   

        frame4 = Frame(self, relief=RAISED, borderwidth = 1)
        frame4.grid(column = 0, row = 2, sticky = W)
        closeButton = Button(frame4, text="Close", command = self.quit)
        closeButton.grid(column = 0, row = 0)
        okButton = Button(frame4, text = "OK")
        okButton.grid(column = 1, row = 0)

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



