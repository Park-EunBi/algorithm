import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w # 동시 진입 가능 차량의 개수
time = 0

# 다리에 모든 트럭이 지나갈 때 까지 - 다리 큐가 0이 될 때 까지 진행
while bridge:
    time += 1
    bridge.pop(0) # 맨 앞 트럭 제거

    if trucks:
        if sum(bridge) + trucks[0] <= l: # 트럭을 한 대 추가해도 괜찮은 무게인지
            bridge.append(trucks.pop(0)) # 가장 앞에 있는 트럭 다리에 올리기
        else: # 다리에 공간이 있지만 무게 때문에 진입 불가
            bridge.append(0) # 빈공간으로 채워줘야 함

print(time)