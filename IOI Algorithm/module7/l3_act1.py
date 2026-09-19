# Find if There is a Pair in A[0..N-1] with Given Sum

# Method
def isPairSum(A, N, X):

    for i in range(N):
        for j in range(N):

            # as equal i and j means same element
            if(i == j):
                continue

            # pair exists
            if (A[i] + A[j] == X):
                return [A[i], A[j]]

            # as the array is sorted
            if (A[i] + A[j] > X):
                break

    # No pair found with given sum
    return 0

# array declaration
arr = [2, 3, 5, 8, 9, 10, 11]

# value to search
val = 17

print("Pair with the sum equal to {} is - {}".format(val, isPairSum(arr, len(arr), val)))