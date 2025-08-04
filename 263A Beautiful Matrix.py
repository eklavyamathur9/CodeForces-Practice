matrix=[]
for _ in range(5):
    matrix.append(list(map(int,input().split())))
row,col=0,0
m=len(matrix)
for x in range(m):
    for y in range(5):
        if matrix[x][y]==1:
            col=abs(x-2)
            row=abs(y-2)
print(row+col)
