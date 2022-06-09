def pascalstriangle(numRows):
    res = [[1]]
    for i in range(numRows-1):
        arr = [1]
        for j in range(len(res)-1):
            arr.append(res[i][j]+res[i][j+1])
        arr.append(1)
        res.append(arr)
    return res

print(pascalstriangle(6))