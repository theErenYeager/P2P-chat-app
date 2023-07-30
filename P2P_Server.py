from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import random as r
import encrypt as e


class Server(DatagramProtocol):
    def __init__(s):
        s.clients = set()

    def datagramReceived(s, datagram, addr):
        datagram = datagram.decode('utf-8')
        if datagram == "ready":
            print(s.clients)
            addresses = "\n".join([str(x) for x in s.clients])
            s.transport.write(addresses.encode('utf-8'), addr)
            s.clients.add(addr)


if __name__ == "__main__":
    reactor.listenUDP(9999, Server())
    reactor.run()
