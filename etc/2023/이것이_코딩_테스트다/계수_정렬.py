# 원소의 개수를 세는 것
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

cnt = [0] * (max(array) + 1)

for i in range(len(array)):
    # 각 데이터의 인덱스 값에 해당하는 값 증가
    cnt[array[i]] += 1

for i in range(len(cnt)):
    for j in range(cnt[i]): # 개수만큼 출력
        print(i, end=' ')
