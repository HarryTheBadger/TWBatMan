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

    def service_status(self, sname):
        from subprocess import check_output 

        for line in check_output("sc query " + sname, shell=True).decode().split('\n'):
            words = line.split()

            if len(words) > 0 and words[0] == 'STATE':
                if words[3] == 'RUNNING':
                    return(1)
                else:
                    return(0)

    def service_on(sname):
        pass

    def service_off(sname):
        pass