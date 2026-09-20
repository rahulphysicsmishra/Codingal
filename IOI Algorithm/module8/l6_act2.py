# Program to check the array is rotated and sorted
arr = [3, 4, 5, 1, 2]
n = len(arr)
count = 0

# interating loop from 1 to length of array
for i in range(1, n):
    # comparing items of array
    if(arr[i-1]>arr[i]):
        count+=1

# special case- comparing last element to the first element
if(arr[n-1]>arr[0]):
    count+=1

# driver code
print(count<=1)