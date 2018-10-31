## Zero-Knowledge API MVP
This is a mvp of our zero-knowledge api.

## Zero-Knowledge Proofs
A zero-knowledge proof involves two parties: a prover, Pat, and a verifier, Victor. Pat wants to prove to Victor that he knows something (i.e. a statement) without revealing the statement. 

A zero-knowledge proofs comes with three properties:
  * _completeness_: a honest prover is able to convince a honest verifier about the truth of a statement
  * _soundness_: a malicious prover is not able to convince a honest verifier about the falseness of a statement
  * _zero-knowledge_: while convincing the honest verifier, a prover does not reveal anything about the statement other than the truth of the statement

More information please visit <a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">here</a>.

## How to use/run the MVP

The MVP is written in python. To run the MVP you need to open two command lines:

'''
python verifier.py
'''

'''
python prover.py
'''

## API / SDK
We are compliant with the standardisation effords of zero-knowledge proofs. See <a href="https://zkproof.org/">here</a> for more details.

## License
This is open-source software. CC-NC
