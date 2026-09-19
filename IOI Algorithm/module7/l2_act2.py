# Program to perform binary search recursively
def binarySearch(arr, l, r, x):
    # Check if the length of array is greater than or equal to 0
    if r >= l:
        # find the mid element's index
        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller check in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else check in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # Element is not present in the array
        return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element {} is present at index {}".format(x, result))
else:
    print("Element is not present in array")