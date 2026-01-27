# Program to divide two numbers without using the division operator
 
def divide(ourDividend, ourDivisor):
    
    # Check if divisor is +ve or -ve
    sign = (-1 if((ourDividend < 0) ^
                (ourDivisor < 0)) else 1);
    
    # Make both positive
    ourDividend = abs(ourDividend);
    ourDivisor = abs(ourDivisor);
    
    quotientNumber = 0
    tempNumber = 0
    
    # Go from 31 to 0 and accumulate all valid bits
 
    for i in range(31, -1, -1):
 
        if (tempNumber + (ourDivisor << i) <= ourDividend):
            tempNumber += ourDivisor << i
            quotientNumber |= 1 << i
 
    # Assuming the sign value computed earlier is -1, negate the quotient value
    if sign ==-1 :
        quotientNumber=-quotientNumber
    return quotientNumber
 
 
a = int(input("Enter a for a/b : "))
b = int(input("Enter b for a/b : "))
print("Result of ",a,"/",b,"is",divide(a, b))
