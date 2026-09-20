# initializing matrices
x = [[8, 2, 3],
    [4, 1, 9],
    [1, 4, 8]]

answer = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        # transpose matrix
        answer[i][j] = x[j][i]

for r in answer:
    print(r)