def rotateimage(arr):
    rows, cols = len(arr), len(arr[0])
    for i in range(0, rows):
        for j in range(i, cols):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    
    for i in range(0, rows):
        for j in range(0, rows//2):
            arr[i][j], arr[i][rows-1-j] = arr[i][rows-1-j], arr[i][j]