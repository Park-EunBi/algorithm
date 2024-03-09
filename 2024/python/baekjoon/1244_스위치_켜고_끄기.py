# 1: 켜짐, 0: 꺼짐 / 1: 남, 2: 여
# idx 처리 주의
n = int(input())
light = list(map(int, input().split()))
t = int(input()) # 사람 수
people = [list(map(int, input().split())) for _ in range(t)] # 성별, 숫자

# num의 배수 상태 전환
def man(number):
    temp = light
    for k in range(number, n + 1, number):
        temp[k - 1] = 1 - temp[k - 1]
    return temp

# number를 중심으로 가장 넓은 대칭
def woman(number):
    mid = number - 1
    temp = light

    if number == n:
        temp[n - 1] = 1 - temp[n - 1]
        return temp

    for k in range(mid + 1):
        # 대칭 체크
        if mid + k < n and light[mid - k] == light[mid + k]:
            temp[mid - k] = light[mid + k]= 1 - temp[mid - k]
        else:
            break

    return temp

# main
for i in range(t):
    gender, number = people[i]
    # 남성
    if gender == 1:
        light = man(number)
    # 여성
    elif gender == 2:
        light = woman(number)

# 출력
repeat = n//20
for j in range(repeat + 1):
    print(*light[20*j:20*(j + 1)])

# if n//20 and n%20:
#     print(*light[20*repeat:])

'''
5
1 1 1 1 1
1
2 4


'''