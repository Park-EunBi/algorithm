num_list = list(range(10001))
for i in range(10001):
    result = i
    for j in str(i):
        result += int(j)
        if result in num_list:
            num_list.remove(result)

for i in range(len(num_list)):
    print(num_list[i])

