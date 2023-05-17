def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    ret1 = 0
    ret2 = 0
    for i in range(n):
        ret1 += arr[i][i]
        ret2 += arr[i][n -1 -i]

    return abs(ret1 - ret2)