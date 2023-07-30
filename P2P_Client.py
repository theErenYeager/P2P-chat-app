from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint
import encrypt as e
#import security as e
import tkinter as tk
from tkinter.simpledialog import askstring
import tkinter.scrolledtext


from threading import *


class Client(DatagramProtocol):
    def __init__(s, host, port):
        if host == "localhost":
            host = '127.0.0.1'

        s.id = host, port
        s.address = None
        s.server = '192.168.39.166', 9999
        #print("Working on id:", s.id)

        s.msg = tk.Tk()
        s.msg.withdraw()
        s.host = tk.simpledialog.askstring(
            "Write HOST", f"Working on id : {s.id}\nEnter HOST address :", parent=s.msg)
        s.port = tk.simpledialog.askstring(
            "Write PORT", f"Working on id : {s.id}\nEnter PORT :", parent=s.msg)

        thread1 = Thread(target=s.Gui, args=())

        thread1.start()

    def Gui(s):
        s.tab = tk.Tk()
        # s.tab.geometry('500x500')
        s.tab.configure(bg="lightgray")

        tk.Label(s.tab, text=f"Working on id : {s.id}\nP2P Chat:", bg="lightgray").pack(
            padx=20, pady=5)

        s.text_area = tk.scrolledtext.ScrolledText(s.tab, state="disabled")
        s.text_area.pack(padx=20, pady=5)

        tk.Label(s.tab, text='Message', bg="lightgray").pack(padx=20, pady=5)

        s.input_area = tk.Text(s.tab, height=3)
        s.input_area.pack(padx=20, pady=5)

        s.btn = tk.Button(s.tab, text="SEND",
                          command=s.send_message)
        s.btn.pack()

        s.tab.mainloop()

    def startProtocol(s):
        s.transport.write("ready".encode('utf-8'), s.server)

    def datagramReceived(s, datagram, addr):
        print(type(datagram))
        datagram = e.decrypt(datagram)

        if addr == s.server:
            print("Choose a client from these\n",
                  e.encrypt(datagram).decode('utf-8'))

            # GUI -- HOST - PORT I/P

            #s.address = input("write Host :"), int(input("write port :"))
            s.address = s.host, int(s.port)
            # reactor.callInThread(s.send_message)
        else:
            print(addr, ":", datagram)
            s.text_area.config(state="normal")
            s.text_area.insert('end', datagram)
            s.text_area.yview('end')
            s.text_area.config(state="disabled")

    def send_message(s):
        # while True:
        s.transport.write(
            e.encrypt(s.input_area.get('1.0', 'end')), s.address)
        s.input_area.delete('1.0', 'end')


if __name__ == '__main__':

    # Gui

    port = randint(1000, 5000)
    reactor.listenUDP(port, Client('192.168.39.166', port))  # 192.168.227.166
    reactor.run()
