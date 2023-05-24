import cowsay    #after running command in pip.py, the package is installed
import sys

if len(sys.argv) != 2:
    sys.exit("Invalid arguments")
cowsay.trex("hello," + sys.argv[1])



#name of this file cannot be the same as the imported package, or else will ahve AttributeError. python thought this file is the package