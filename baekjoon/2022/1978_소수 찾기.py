num_count = int(input())
num_list = list(map(int, input().split(' ')))
res = 0

if len(num_list) == num_count:
    for i in num_list:
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            res += 1
print(res)