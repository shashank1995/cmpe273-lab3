from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Echo(DatagramProtocol):

    def datagramReceived(self, data, (host, port)):
        print("Received %r from %s:%d" % (data, host, port))
        self.transport.write(data, (host, port))

reactor.listenUDP(8000, Echo())
reactor.run()