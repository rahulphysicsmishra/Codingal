# Program for searching an element using Linear Search

# Function to search for an element
def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i

    # if element is not found in the array
    # return -1
    return -1

# Take array input from user
# Enter element to search for
arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)

# Function call
result = search(arr, n, x)
# check returned index and print the output
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)