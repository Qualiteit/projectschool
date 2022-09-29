import socket
import threading
import time

from numpy import true_divide
from stats import Stats

class Tello(object):
    def __init__(self):

        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))
        
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()
        
        self.tello_ip = ''
        self.tello_port = 8889
        self.tello_address = (self.tello_ip, self.tello_port)
        self.log = []

        self.MAX_TIME_OUT = 15.0

        def send_command(self, command):
            self.log.append(Stats(command. len(self.log)))
            self.socket.sendto(command.encode'utf-8'), self.tello_address)
            print(f'sending command: {command} to {self.tello_ip}')

            start =  time.time()
            while not self.log[-1].got_response():
                now = time.time()
                diff = now - start 
                if diff > self.MAX_TIME_OUT:
                    print(f'Max timeout exceeded... command {command}')
                    return
                    print(f'Done! sent command: {command} to {self.tello_ip}')


                def _receive_thread(self):

                    while true
                    try:
                        self.response, ip = self.socket.recvfrom(1204)
                        print(f'from{ip} : {self.response}')

                        self.log[-1].add_response(self.reponse)
                        except Exception as exc:
                            print(f'Caught exception socket.error :{exc}')

                        def on_close(self):

                            pass
                        def get_log(self):

                            return self.log
                    



