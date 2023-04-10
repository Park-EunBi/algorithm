def solution(bridge_length, weight, truck_weights):
    result = 0
    # 다리의 길이만큼 초기화
    bridge = [0 for _ in range(bridge_length)]

    while bridge:
        result += 1
        bridge.pop(0)

        if truck_weights:
            # 다리에 올라간 트럭들의 무게와 대기 첫번째 트럭의 무게의 합을 구함
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
            # print(bridge)
    return result

# print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
