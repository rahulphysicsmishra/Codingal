# Program to rotate an array 'n' times

# Input array, length and 'n'
def rotations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)

# Rotate array to the left by 1 place
def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size-1):
        a[i] = a[i + 1]
    a[a_size-1] = temp

def printArray(a, a_size):
    for i in range(a_size):
        print("% d" % a[i], end = " ")
    print("\n")

a = [12,1,31,85,2,3,53,56323]
printArray(a,len(a))
rotations(a, 2, len(a))
printArray(a, len(a))