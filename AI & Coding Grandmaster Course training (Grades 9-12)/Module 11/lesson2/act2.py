# Program to check if the Nth bit is set or not 
 
def setOrNot(number, n):
 
    # Make a mask variable by left shifting 1 (k-1) times and check if (n AND mask) equals 1 or 0
    if number & (1 << (n - 1)):
        print( "\nSET")
    else:
        print("\nNOT SET")
 
 
number = int(input("Enter number : "))
n = int(input("Enter bit number : "))
setOrNot(number, n)
