from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 높은 빈도로 등장하는 k 번째 값 까지 출력

        # 해시 만들고
        count_nums = {}
        for i in nums:
            if i not in count_nums:
                count_nums[i] = 1
            else:
                count_nums[i] += 1

        # 해시를 어떻게 정렬? -> lambda 사용
        count_nums = sorted(count_nums.items(), key=lambda item: item[1], reverse= True)

        # 등장 횟수 높은 순으로 k 번째 까지 출력
        res = []
        for i in range(k):
            res.append(count_nums[i][0])

        return res



s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))
print(s.topKFrequent([1], 1))
print(s.topKFrequent([1, 2], 2))