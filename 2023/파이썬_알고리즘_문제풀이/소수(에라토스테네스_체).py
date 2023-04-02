import sys
sys.stdin = open("input.txt", "rt")

# 1~n까지의 소수의 개수를 출력
# 20 -> 2, 3, 5, 7, 11, 13, 17, 19 => 8
# 제한시간 1초

n = int(input())

# 소수 == 1과 자기자신을 제외한 수로 나눌 수 없는 수
# 배수인 경우 1으로 표시하는 방법을 사용

nums = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
    if nums[i] == 0: # 소수
        cnt += 1
    for j in range(i, n+1, i): # i의 배수로 증가
        nums[j] = 1

print(cnt)

'''
# 시간 초과 된 코드 
## 시간 복잡도는 O(n^2)이며, 
## 이중 반복문을 사용하기 때문에 입력값이 커질수록 느리게 동작
cnt = 0
for i in range(2, n+1):
    if i == 2:
        cnt +=1
        continue
    for j in range(2, i):
        if(i % j == 0):
            cnt += 1
            break

print(n - cnt)
'''

# 에라토스테네스 체 적용

'''
# 시간 초과 
## remove()는 리스트에서 해당 요소를 찾아야 하기에
## 리스트에 크기가 증가함에 따라 선형적으로 시간이 증가함
nums = list(range(2, n+1))

for i in nums:
    for j in range(i + 1, n+1):
        if j % i == 0:
            if j in nums:
                nums.remove(j) 

print(len(nums))
'''
