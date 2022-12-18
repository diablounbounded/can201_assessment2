#/usr/bin/python
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import Host
from mininet.node import OVSKernelSwitch
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.term import makeTerm

def myTopo():
    net = Mininet( topo=None, autoSetMacs=True, build=False, ipBase='10.0.1.0/24')
    
    #add controller

    c1 = net.addController('c0', RemoteController)

    #add hosts

    Client = net.addHost( 'Client', cls=Host, defaultRoute=None)
    Server1 = net.addHost( 'Server1', cls=Host, defaultRoute=None)
    Server2 = net.addHost( 'Server2', cls=Host, defaultRoute=None)

    #add switch
    s1 = net.addSwitch( 's1', cls=OVSKernelSwitch,failMode='secure')

    #add links
    net.addLink(Server1,s1)
    net.addLink(Server2,s1)
    net.addLink(Client,s1)
    
    #net build
    net.build()
    
    #set mac and ip
    Client.setMAC(intf="Client-eth0", mac="00:00:00:00:00:03")
    Server1.setMAC(intf="Server1-eth0", mac="00:00:00:00:00:01")
    Server2.setMAC(intf="Server2-eth0", mac="00:00:00:00:00:02")

    Client.setIP(intf="Client-eth0",ip='10.0.1.5/24')
    Server1.setIP(intf="Server1-eth0",ip='10.0.1.2/24')
    Server2.setIP(intf="Server2-eth0",ip='10.0.1.3/24')

    net.start()
    
    # start xterms
    net.terms += makeTerm(c1)
    net.terms += makeTerm(Server1)
    net.terms += makeTerm(Server2)
    net.terms += makeTerm(Client)
    
    
    #CLI mode running
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myTopo()
