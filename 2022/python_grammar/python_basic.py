# enumerate - 인덱스와 리스트 값을 동시에 출력
for i, v in enumerate(range(10, 20, 2)):
    print(i, v)
print()

# join - list 값을 묶어서 처리
a = ['a', 'b']
print(a)
print(' '.join(a))
print()

# f-string - 변수를 인라인으로 삽입하여 출력 (.format 보다 간결)
index = 1
fruit = 'apple'
print(f'{index + 1} : {fruit}')
print()

# pass - 함수의 골격을 잡고 test 해볼 때 사용
def test():
    pass

# locals - 클래스 메소드 내부의 모든 로컬 변수 출력 (디버깅)
import pprint
pprint.pprint(locals())
