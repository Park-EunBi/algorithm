import sys
sys.stdin = open("input.txt", "rt")

# 문자와 숫자가 섞여 있는 문자열에서 숫자만 추출
# 순서대로 자연수 만들기
# 만드렁진 자연수와 약수 개수 쳑
word = input()

# 숫자만 추출
res = []
for w in word:
    if w.isnumeric():
        res.append(w)

res = int(''.join(res))
print(res)

# 약수의 개수 출력
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt +=1
print(cnt)