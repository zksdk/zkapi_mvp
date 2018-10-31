
import sys

class Console(object):

  def __init__(self):
    self.__color = '\033[94m'
    self.__end_color = '\033[0m'
  
  def __del__(self):
    pass

  @staticmethod
  def write(name, message):
    console = Console()
  
    sys.stdout.write(console.__color)
    print("[" + name + "] " + message)
    sys.stdout.write(console.__end_color)
