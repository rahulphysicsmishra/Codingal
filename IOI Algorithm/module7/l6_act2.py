def sortArray(A):

    # base case
    if len(A) <= 1:
        return

    x = -1
    y = -1
    prev = A[0]

    # process each pair of adjacent elements
    for i in range(1, len(A)):

        # if the previous element is greater than the current element
        if prev > A[i]:
            # first occurrence of conflict
            if x == -1:
                x = i - 1
                y = i
            else:
                # second occurrence of conflict
                y = i

        prev = A[i]

    # swap the elements at index `x` and `y`
    swap(A, x, y)

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

if __name__ == '__main__':
    a = [3, 5, 6, 9, 8, 7]
    print("Original Array:", a)
    sortArray(a)
    print("Sorted Array:", a)