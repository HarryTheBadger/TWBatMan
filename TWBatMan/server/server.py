from subprocess import CalledProcessError
class Server(object):
    """Handles retreiving all the information about a server and its services"""

    

    def __init__(self):
        '''
        Constructor
        '''
        import xml.etree.ElementTree as ET
        from socket import gethostname
        
        
        services = ET.parse("twbatman.xml")
        root = services.getroot()
        self.hostname = gethostname()
        self.servertype, self.services = self._get_services(root, self.hostname)

    def gethostname(self):
        return self.hostname

    def gettype(self):
        return self.servertype

    def getservices(self):
        return self.services

    def _get_services(self, root, hostname):
        ''' Gets all the server and services information frmo the XML file for this host name '''

        servicelist = []
        for s in root.iter('server'):
            if s.attrib['name'] == hostname:
                servertype = s.attrib['type']
                for t in s:
                    # print(t.tag, t.attrib)
                    if t.tag == 'service':
                        # print("sc query " + t.attrib['name'])
                        servicelist.append(t.attrib['name'])
                    
        return(servertype, servicelist)

    def onStatus(self, sname):
        from subprocess import check_output 

        try:
            for line in check_output("sc query " + sname, shell=True).decode().split('\n'):
                words = line.split()
    
                if len(words) > 0 and words[0] == 'STATE':
                    return(words[3])
                
        except CalledProcessError:
            return("Service Not Found")        

    def startService(self, sname):
        from subprocess import check_output 
        try:
            for line in check_output("sc start " + sname, shell=True).decode().split('\n'):
                words = line.split()
                if len(words) > 0 and words[0] == 'STATE':
                    return(words[3])
                
        except CalledProcessError:
            return("Service Not Found")

    def stopService(self, sname):
        from subprocess import check_output 
        import time as t
        
        try:
            check_output("sc stop " + sname, shell=True).decode().split('\n')
            tcount = 0
            while 'PENDING' in self.onStatus(sname) and tcount < 5:
                t.sleep(5) 
                tcount += 1
            
            #
            # If the tcount == 5 then the service hasn't stopped and must need killing
            #
            if tcount == 5:
                self._killService(sname)
                
            return  (self.onStatus(sname))      

        except CalledProcessError:
            return("Service Not Found")
        
    def _killService(self, sname):
        from subprocess import check_output
        
        pid = self._getPID(self, sname)
        
        for line in check_output("taskkill /f /pid " + pid, shell=True).decode().split('\n'):
            words = line.split()
            if words[0] == 'SUCCESS:':
                return(1)
            else:
                return(0)
     
    def _getPID(self, sname): 
        from subprocess import check_output
        
        try:
            for line in check_output("sc queryex " + sname, shell=True).decode().split('\n'):
                words = line.split()
    
                if len(words) > 0 and words[0] == 'PID':
                    return(words[2])
                
        except CalledProcessError:
            return("Service Not Found")
        
               
            