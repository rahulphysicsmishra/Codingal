# initializing matrices

x = [[8, 2],
    [4, 1]]

y = [[3, 8],
    [9, 15]]

answer = [[0,0],
    [0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        answer[i][j] = x[i][j] + y[i][j]

for r in answer:
    print(r)