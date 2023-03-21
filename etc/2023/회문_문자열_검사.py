import sys
sys.stdin = open("input.txt", "rt")

# 회문이면 YES 아니면 NO
# 대소문자 구분 x

n = int(input())
for i in range(n):
    word = str(input()).lower()
    for j in range(len(word)//2):
        if word[j] != word[len(word) -j -1]:
            print("#", i + 1, "NO")
            break
    else:
        print("#", i + 1, "YES")
