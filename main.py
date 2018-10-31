'''
 MVP - Zero-Knowledge API
'''

from prover import Prover
from verifier import Verifier
from console import Console
from subprocess import Popen, PIPE, STDOUT

if __name__ == '__main__':

  verifier = Popen(["python", "verifier.py"], stdin=PIPE, stdout=PIPE)
  Console.write(Verifier.getName(), verifier.communicate())
  prover = Popen(["python", "prover.py"], stdin=PIPE, stdout=PIPE)
  Console.write(Prover.getName(), prover.communicate())
