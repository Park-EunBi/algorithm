def gridChallenge(grid):
    # Write your code here
    n = len(grid)
    m = len(grid[0])
    ret = 'YES'
    # Only elements within the same row can be rearranged
    for i in range(n):
        grid[i] = sorted(grid[i])
    for i in range(m):
        for j in range(n-1):
            if (ord(grid[j][i]) - ord(grid[j + 1][i])) > 0:
                ret = 'NO'
                break
    return ret

print(gridChallenge(['eabcd', 'fghij', 'olkmn', 'trpqs', 'xywuv'])) # YES
print(gridChallenge(['mpxz', 'abcd', 'wlmf'])) # NO

