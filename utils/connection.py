
import socket
from console import Console
from threading import Thread

class Connection(object):

  def __init__(self):
    self.__host = '127.0.0.1'  # Standard loopback interface address (localhost)
    self.__port = 5000        # Port to listen on (non-privileged ports are > 1023)
  
  def __del__(self):
    pass
  
  def server_socket(self):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((self.__host, self.__port))
    s.listen(1)
    
    message = [None] * 1
    server = Thread(target = self.listen, args = (s, message))
    server.start()
    server.join()
    Console.write("[Connection2]", "Message " + message[0])
    return message[0]
    
  def listen(self, s, message):
    while True:
      conn, addr = s.accept()
      Console.write("[Connection]", "Connected by " + str(addr))
      message[0] = conn.recv(1024)
      if not message[0]:
        break
      Console.write("[Connection]", "Message " + message[0])
      return
    
  def client_socket(self, message):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((self.__host, self.__port))
      s.sendall(message)

