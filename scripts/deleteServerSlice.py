# 2015.03.10 - Initial version.

import wlstModule as wlst    
from library.offline.wllib import *  # @UnusedWildImport

print 'starting the script ....'

# for local test use below...
username = 'weblogic'
password = 'weblogic1#'
url = 't3://localhost:7001'

sliceName = 'aServerSlice'

try:
    
    wlst.connect(username, password, url)

    wlst.edit()
    wlst.startEdit()
       
    print 'Sub Deployments...'
    #deleteJMSSubDeployment('JMSModule' + sliceName + '_SystemModule', sliceName + '_SubDeployment')
    print 'Sub Deployments...end.'

    print 'JMS Modules...' 
    deleteJMSModule('JMSModule' + sliceName + '_SystemModule')
    print 'JMS Modules...end.'

    print 'JMS Servers for every managed server...'
    deleteJMSServer('JMSServer' + sliceName)
    print 'JMS Servers for every managed server...end.'

    print 'Filestores...'
    deleteFilestore('FileStore' + sliceName)
    print 'Filestores...end.'

    print 'datasources...'
    deleteDataSource('oraclePool_' + sliceName)
    print 'datasources...end.'
        
    print 'servers...'    
    deleteServer(sliceName)
    print 'servers...end.'
    
    print 'machines...' 
    deleteUnixMachine('localhost')
    print 'machines...end.' 
                    
except Exception, e:
    print e
    print "Error while trying to execute the script"
    wlst.dumpStack()
    raise 

try:
    wlst.save()
    wlst.activate(block="true")
    print "script returns SUCCESS"   
except Exception, e:
    print e 
    print "Error while trying to save and/or activate!!!"
    wlst.dumpStack()
    raise 
    
