'''
Created on 18 Jun 2016

@author: holldav
'''
import os, msvcrt

#
# Define all the drawing characters
#
boxed = {'dblbar': '\u2550', 
         'sglbar': '\u2500', 
         'dbltoplft': '\u2554',
         'dbltoprgt': '\u2557',
         'dblbotlft': '\u255A',
         'dblbotrgt': '\u255D',
         'dblteelft': '\u2560',
         'dblteergt': '\u2563',
         'dblvert': '\u2551'}

class MyScreen(object):
    '''
    Handles all the screen drawing features
    '''
    paddr = 0

    def __init__(self):
        '''
        Constructor
        '''
  
  
    def drawheader(self, sname, stype):
        
        self.__cls()
        snamestr = "Server Name: {}".format(sname)
        stypestr = "Server Type: {}".format(stype)
        titlestr = 'TrackWise 8.7 Service Management'
        
        hdrwidth = max(len(snamestr), len(stypestr), len(titlestr)) + 10
        padding = hdrwidth - 2
        self.paddr = padding
        
        print('{}{}{}'.format(boxed['dbltoplft'], boxed['dblbar'] * (hdrwidth - 2), boxed['dbltoprgt']))
        print('{}{:^{hw}}{}'.format(boxed['dblvert'], ' ', boxed['dblvert'], hw = padding))
        print('{}{:^{hw}}{}'.format(boxed['dblvert'], titlestr, boxed['dblvert'], hw = padding))
        print('{}{:^{hw}}{}'.format(boxed['dblvert'], ' ', boxed['dblvert'], hw = padding))
        print('{}{:^{hw}}{}'.format(boxed['dblvert'], snamestr, boxed['dblvert'], hw = padding))
        print('{}{:^{hw}}{}'.format(boxed['dblvert'], stypestr, boxed['dblvert'], hw = padding))
        print('{}{:^{hw}}{}'.format(boxed['dblvert'], ' ', boxed['dblvert'], hw = padding))
        print('{}{}{}'.format(boxed['dblteelft'], boxed['sglbar'] * (hdrwidth - 2), boxed['dblteergt']))
     
    def __cls(self):
        if os.name == 'nt':
            cs = 'cls'
        else: 
            cs =  'clear'
        os.system(cs)
        
    def drawsstate(self, messages):
        ''' Draw a box with the information about how may services are up or down'''
        
        for m in messages:
            print('{} {:<{hw}}{}'.format(boxed['dblvert'], m, boxed['dblvert'], hw=self.paddr - 1 ))
            
        print('{}{}{}'.format(boxed['dblteelft'], boxed['sglbar'] * (self.paddr), boxed['dblteergt']))
    
    def drawoptions(self):
        ''' Draws the menu options on the screen '''
        
        validoptions = [0, 1, 2, 3, 4, 5]
        
        print('{} {:<{hw}}{}'.format(boxed['dblvert'], ' 1. Display Service States', boxed['dblvert'], hw=self.paddr - 1 ))
        print('{} {:<{hw}}{}'.format(boxed['dblvert'], ' 2. Stop All Services', boxed['dblvert'], hw=self.paddr - 1 ))
        print('{} {:<{hw}}{}'.format(boxed['dblvert'], ' 3. Start All Services', boxed['dblvert'], hw=self.paddr - 1 ))
        print('{} {:<{hw}}{}'.format(boxed['dblvert'], ' 4. Stop Load Balancer', boxed['dblvert'], hw=self.paddr - 1 ))
        print('{} {:<{hw}}{}'.format(boxed['dblvert'], ' 5. Start Load Balancer', boxed['dblvert'], hw=self.paddr - 1 ))
        print('{} {:<{hw}}{}'.format(boxed['dblvert'], ' ', boxed['dblvert'], hw=self.paddr - 1 ))
        print('{} {:<{hw}}{}'.format(boxed['dblvert'], ' 0. Exit', boxed['dblvert'], hw=self.paddr - 1 ))
        print('{} {:<{hw}}{}'.format(boxed['dblvert'], ' ', boxed['dblvert'], hw=self.paddr - 1 ))
        print('{} {:<{hw}}{}'.format(boxed['dblvert'], ' Enter Choice: ', boxed['dblvert'], hw=self.paddr - 1 ))
        

        while True:
            try:
                choice = int(msvcrt.getch())
                print ("Chose: {}".format(choice))
                validoptions.index(choice)
                break
            except ValueError:
                pass

        return(choice)
                
            