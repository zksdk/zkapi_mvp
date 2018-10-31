
from utils.console import Console
from utils.connection import Connection
from utils.state import State
from threading import Thread

class Verifier(object):
  def __init__(self):
    self.__name = "Victor"
    self.__connection = Connection()
    self.__verifier = Thread(target = self.verify, args = ())
    self.__state = State()

  def __del__(self):
    pass

  @staticmethod
  def create():
    verifier = Verifier()
    Console.write(verifier.__name, "Initialising ...")
    verifier.__verifier.start()
    verifier.__verifier.join()

  def verify(self):
    while True:
      Console.write(self.__name, "I know (x). I want be convinced that this is true.")
      message = self.__connection.server_socket()
      Console.write(self.__name, "Receiving " + message)
      Console.write(self.__name, "I'm now verifying " + message + ". If this is true I accept, otherwise I reject." )
      return

  @staticmethod
  def getName():
    verifier = Verifier()
    return verifier.__name

if __name__ == '__main__':
  Verifier.create()
