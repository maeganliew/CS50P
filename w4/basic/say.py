import sys

#library written in sayings.py
from sayings import hello, goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])