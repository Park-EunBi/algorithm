self_nums = [True] * 10001

for i in range(1, 10001):
    num = list(map(int, str(i)))
    ret = i + sum(num)
    if ret < 10001:
        self_nums[ret] = False

for i in range(1, 10001):
    if self_nums[i]:
        print(i)


