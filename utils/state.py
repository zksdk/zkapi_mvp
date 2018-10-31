
class State(object):

  def __init__(self):
    self.__x = []     #instance
    self.__w = []     #witness
    self.__setup = [] #setup
  
  def __del__(self):
    pass

  def update(self, x, w):
    self.__x = x
    self.__w = w
    return
