#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

Author: Jan Bodnar
Last modified: November 2015
Website: www.zetcode.com
"""

from tkinter import Tk, Text, BOTH, RIGHT, TOP, X, N, LEFT, RAISED, Listbox, StringVar, END, Menu, W, Message
from tkinter.ttk import Frame, Button, Style, Label, Entry 

class TWB(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    
    def initUI(self):
      
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

        svcs = ['TrackWise Tomcat', 'Web Services Tomcat', 'QMD Tomcat', 'Keystone Intake', 'ID Intake', 'TWC']
        #lb = Listbox(self)
        #for i in svcs:
        #    lb.insert(END, i)

        #lb.bind("<<ListboxSelect>>", self.onSelect)
        #lb.pack(pady = 15)

        #self.var = StringVar()
        #self.label = Label(self, text = 0, textvariable = self.var)
        #self.label.pack()
        
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

        #entry1 = Entry(frame1)
        #entry1.pack(fill=X, padx = 5, expand = True)

        #frame2 = Frame(self)
        #frame2.pack(fill = X)

        #label2 = Label(frame2, text = "Author", width = 6)
        #label2.pack(side=LEFT, padx = 5, pady = 5)

        #entry2 = Entry(frame2)
        #entry2.pack(fill=X, padx = 5, expand = True)

        #frame3 = Frame(self)
        #frame3.pack(fill = X)

        #label3 = Label(frame3, text = "Review", width = 6)
        #label3.pack(side=LEFT, anchor = N, padx = 5, pady = 5)

        #txt = Text(frame3)
        #txt.pack(fill=X, padx = 5, expand = True)

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
    
    def centerWindow(self):

        w = 768
        h = 480

        swidth = self.parent.winfo_screenwidth()
        sheight = self.parent.winfo_screenheight()

        x = int((swidth - w) / 2)
        y = int((sheight - h) / 2)
        self.parent.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        

def main():
  
    root = Tk()
    # root.geometry("450x150+300+300")
    app = TWB(root)
    root.mainloop()  


if __name__ == '__main__':
    main()