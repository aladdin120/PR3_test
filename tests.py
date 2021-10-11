import unittest
from main import ChatServer
from GUI import GUI
from tkinter import Tk
import socket



class SocketTCPTest(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(("", 2000))
        self.serv.listen(1)

    def tearDown(self):
        self.serv.close()
        self.serv = None


class SocketUDPTest(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(("", 2000))

    def tearDown(self):
        self.serv.close()
        self.serv = None


class MySocketTest(unittest.TestCase):
    def setUp(self):
        self.serv = ChatServer()

    def tearDown(self):
        self.serv.close()
        self.serv = None


class MyGuiTest(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.gui = GUI(self.root)

    def TestTitle(self):
        self.assertEqual(self.gui.root.title, "Socket Chat")

    def tearDown(self):
        self.gui.client_socket.close()
        self.gui.client_socket = None


if __name__ == '__main__':
    unittest.main()
