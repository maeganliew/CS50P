import sys    #sys stands for system

if len(sys.argv) < 2:   #no argv[1] will lead to IndexError
    sys.exit("Argument needed")   #sys.exit exits the program with the error message
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
print("hello", sys.argv[1])

#"DavidMalan" is considered as one arg. wrapped in quotes



#slices of list. (means only wanting a portion of the list, not the whole thing)
for arg in sys.argv[1:]:     #sys.argv[start:end]
    print(arg)