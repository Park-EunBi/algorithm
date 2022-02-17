num = int(input())
honeycomb = [1]

while(1):
    if (num == 1):
        break
    else:
        honeycomb.append(honeycomb[-1] + (6 * len(honeycomb)))
        if(honeycomb[-1] >= num):
            break

print(len(honeycomb))

'''
틀린 이유

1. if (num == 1):
        break
을 작성하지 않아 1이 들어왔을 때 2가 출력되는 오류를 잡지 못하였다. 

2. if(honeycomb[-1] >= num):
여기에서 등호를 빼고 생각하여 수의 경계가 잘못 나뉘었다. 

'''

'''
다른 분들의 풀이

1. 리스트를 사용하지 않고 리스트를 대신할 변수를 사용함 
- 리스트의 마지막 수만 저장할 변수
- 리스트의 길이를 대신할 변수

2. and 를 사용하여 해당 범위 내에 수가 있을 때 값을 출력하도록 함
if (num + 1 <= N) and (N <= num + 6 * m) 
'''