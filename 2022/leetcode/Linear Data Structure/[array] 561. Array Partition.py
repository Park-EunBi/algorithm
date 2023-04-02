from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        '''
        list 를 n 개의 쌍으로 나누기
        최소값들을 뽑아내기
        그것들의 합 중 가장 큰 값을 반환
        '''

        # 다시 말하면 최솟값들의 합이 커지도록
        # 내림차순 정렬해서 개수의 반개의 합 -> 안된다
        # nums = [4, 3, 2, 1] 일 때 4와 3은 큰 수는 맞지만
        # 두 수 중 최소 값이 되지는 않는다 (4는 항상 최대 값이라 더해질 수 없다)

        # 내림 차순으로 정렬한 뒤 홀수 번째 항목들을 더하면 최솟값들의 최대 합이 된다
        nums = sorted(nums)
        nums = nums[::2]
        result = sum(nums)

        return result

s = Solution()
print(s.arrayPairSum([1,4,3,2]))
print(s.arrayPairSum([6,2,6,5,1,2]))

# 다른 풀이
## 모든 조합을 고려해보기

'''
from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 완전 전부 해보는 것이 아니라 정렬을 한 뒤 조합을 구하면 된다
        # 최소값이 크도록 조합하는 것이기에 오름차순 정렬을 한 뒤 2개씩 묶으면
        # 최솟값이 최대가 된다 [1, 2, 3, 4] 로 생각해보기

        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

        return result

s = Solution()
print(s.arrayPairSum([1,4,3,2]))
print(s.arrayPairSum([6,2,6,5,1,2]))
'''

# 다른 풀이
## 짝수 번째 값만 더하기
'''
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 위에 작성한 풀이에서 홀수번째 인덱스 값들의 최대가 되는 최솟값이라는 것을 앎
        # 이를 이용
        sum = 0
        nums.sort()
        for i in range(len(nums)):
            if i % 2 == 0:
                sum += nums[i]

        return sum

        return result

s = Solution()
print(s.arrayPairSum([1, 4, 3, 2]))
print(s.arrayPairSum([6, 2, 6, 5, 1, 2]))
'''