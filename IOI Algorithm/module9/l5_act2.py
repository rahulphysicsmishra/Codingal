# initializing matrices

x = [[8, 2],
    [4, 1]]

y = [[3, 8],
    [9, 15]]

answer = [[0,0],
    [0,0]]

# iterate through rows of x
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            answer[i][j] += x[i][k] * y[k][j]

for r in answer:
    print(r)