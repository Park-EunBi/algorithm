n = int(input())
cnt = n

for _ in range(n):
    word = input()
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            pass
        elif word[i] in word[i+1:]: # 이후에 글자가 다시 등장하면
            cnt -= 1
            break

print(cnt)