import unittest

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






if __name__ == '__main__':
    unittest.main()
