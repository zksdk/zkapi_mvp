
from utils.console import Console
from utils.connection import Connection
from utils.state import State
from threading import Thread

class Prover(object):
  def __init__(self):
    self.__name = "Pat"
    self.__connection = Connection()
    self.__prover = Thread(target = self.prove, args = ())
    self.__state = State()
  
  def __del__(self):
    pass
  
  @staticmethod
  def create():
    prover = Prover()
    Console.write(prover.__name, "Initialising ...")
    prover.__prover.start()
    prover.__prover.join()

  def prove(self):
    while True:
      Console.write(self.__name, "I know (x, w). I want to prove this knowledge.")
      Console.write(self.__name, "Transforming (x, w) -> \pi")
      
      ''' todo: transform (x,w) -> \pi '''
      
      Console.write(self.__name, "Sending \pi")
      self.__connection.client_socket("\pi")
      return

  @staticmethod
  def getName():
    prover = Prover()
    return prover.__name

if __name__ == '__main__':
  Prover.create()
