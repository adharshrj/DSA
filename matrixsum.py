def matrixSum(mat):
    temp, rows, cols = 1, len(mat), len(mat[0])
    for i in range(0, rows):
        if mat[i][0]==0: temp = 0
        for j in range(1, cols):
            if mat[i][j]==0:
                mat[i][0]=mat[0][j]=0
    
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, 0, -1):
            if mat[i][0]==0 or mat[0][j]==0:
                mat[i][j]=0
        if temp == 0: mat[i][0]=0


print(matrixSum([[1,1,1], [1,0,1], [0,1,0]]))