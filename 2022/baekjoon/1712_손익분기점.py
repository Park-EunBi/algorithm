a, b, c = map(int, input().split())

# list = input().split(' ')
#
# a = int(list[0])
# b = int(list[1])
# c = int(list[2])

if (b >= c):
    res = -1
else:
    res = int(a / (c - b)) + 1
    print(type(round(a / (c - b))))

print(res)

'''
틀린 이유

1. b == c 일 때에도 손익 분기점을 계산할 수 없기에 
if 문의 조건을 b >= c 로 작성해야 한다. 

2. 손익 분기점을 계산 할 때 계산한 결과를 int로 변환해야 한다.
예제를 입력했을 때 정수로 출력이 되어
변환하지 않아도 된다고 생각하였지만
type을 출력해보니 float이었다. 

-> 계산 결과를 int로 변환시키거나
-> // 연산자를 사용하면 된다. 

<틀렸습니다>
a, b, c = map(int, input().split())

if (b >= c):
    res = -1
else:
    res = (a / (c - b)) + 1
    
print(res)

'''