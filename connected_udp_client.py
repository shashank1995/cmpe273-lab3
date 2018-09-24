from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 8000

        self.transport.connect(host, port)
        print("Now we can only send to host %s port %d" % (host, port))
        self.transport.write("Hello World") # no need for address

    def datagramReceived(self, datagram, address):
        print("Received %s from %s" % (repr(datagram), repr(address)))

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")

# 0 means any port, we don't care in this case
reactor.listenUDP(0, Helloer())
reactor.run()
