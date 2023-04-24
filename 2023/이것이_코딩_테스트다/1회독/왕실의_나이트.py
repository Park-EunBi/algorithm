import sys
sys.stdin = open("input.txt", "rt")

start = list(''.join(input()))

move = [[1, 2], [1, -2],  [-1, 2], [-1, -1], [2, 1], [2, -1], [-2, 1], [-2, -1]]
word = {'a' : 1, 'b ': 2, 'c' : 3, 'd' : 4, 'e': 5, 'f':6, 'g':7, 'h':8}

if start[0] in word:
    start[0] = word[start[0]]
start[1] = int(start[1])

'''
input_data = input()
row = input_data[1]
colum = int(ord(input_data[0])) - int(ord('a')) + 1
'''
res = 0
for i in range(len(move)):
    dx = start[0]
    dy = start[1]

    dx += move[i][0]
    dy += move[i][1]

    if dx < 1 or dx > 9 or dy < 1 or dy >9:
        continue
    res += 1

print(res)