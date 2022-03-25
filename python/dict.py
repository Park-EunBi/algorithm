# create dict
a = {} # a = dict()

# add data
a = {0: 'apple'}
a[1] = 'banana'

# key lookup
print(a)
print(a[1])

for k, v in a.items():
    print(k, v)

# defaultdict
'''
존재하지 않는 키를 조회할 경우, 디폴트 값을 기준으로 
해당 키에 대한 딕셔너리 아이템 생성 
'''
import collections
b = collections.defaultdict(int)
b[0] += 1
print(b)

# counter
'''
아이템의 개수를 계산하여 딕셔너리로 리턴 
'''
c = [1, 2, 3, 4, 5, 5, 5, 6, 6]
print(collections.Counter(c))
# 빈도수가 높은 상위 2개 요소 추출
print(collections.Counter(c).most_common(2))

# OrderDict
'''
dict의 입력 순서를 유지
3.6 버전 이하에서 사용 
(dict으로 입력 순서를 기대하지 말자 (사용하지 말자)) 
'''
d = collections.OrderedDict({0: 'apple', 1: 'banana', 2: 'pineapple'})
print(d)