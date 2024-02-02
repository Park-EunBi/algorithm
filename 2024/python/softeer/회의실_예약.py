import sys

n, m = map(int, input().split())  # 회의실, 회의 시간
room = {}

for _ in range(n):
    room[input()] = [0] * 19

for _ in range(m):
    a, b, c = input().split()
    for i in range(int(b), int(c)):
        room[a][i] = 1

room = dict(sorted(room.items()))  # dict 으로 감싸야 함

for idx, r in enumerate(room):
    print(f'Room {r}:')
    times = []
    current = 1  # flag - 이전 값 표시
    for i in range(9, 18):
        if current == 1 and room[r][i] == 0:  # 이전 값이 1이고, 현재 0 이라면 (비어 있다면)
            current = 0
            start = i
        elif current == 0 and room[r][i] == 1:  # 이전 값이 0이고, 현재 1 이라면 (마지막 사용 시간)
            current = 1
            end = i
            times.append([start, end])
    if current == 0:
        times.append([start, 18])

    if len(times) == 0:
        print('Not available')
    else:
        print(f'{len(times)} available:')
        for t in times:
            print(f'{t[0]:02d}-{t[1]}')

    if idx != len(room) - 1:
        print('-----')
