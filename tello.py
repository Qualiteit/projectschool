import socket
import threading
import time
from stats import Stats

class Tello(object):
    def __init__(self):

        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))
        