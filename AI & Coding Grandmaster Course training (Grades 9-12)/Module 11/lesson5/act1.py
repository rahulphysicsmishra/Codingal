# Program to swap two numbers without using 3rd variable 
 
def swap1(a,b):
 
    # Code to swap 'a' and 'b'
    a = a ^ b 
    b = a ^ b
    a = a ^ b 
    print ("After Swapping: a = ", a, " b =", b)
 
def swap2(a, b):
 
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print ("After Swapping: a = ", a, " b =", b)
 
swap1(1,2)
swap2(1,2)
