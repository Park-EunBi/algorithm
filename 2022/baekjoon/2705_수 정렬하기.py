n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))
num = sorted(num, reverse=True)
for _ in range(n):
    print(num.pop())