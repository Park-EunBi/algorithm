from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #문자를 다 정렬해서 새로운 리스트에 넣자
        # 주의 - 그냥 바로 sorted() 사용하면 리스트에 있는 문자들이 정렬됨
        # 한글자 내부의 있는 알파벳의 정렬을 원하는 것임
        # 이후에 판단을 쉽게 하기 위해 sorted 해야 함
        strs = sorted(strs)
        print(strs)
        sort_str = []
        for s in strs:
            # 이렇게 하면 문자가 따로따로 이차원 배열으로 정렬됨 -> 합치기
            sort_str.append(''.join(sorted(s)))

        # 애너그램 끼리 묶고 반환하기 (수정 중)
        # for i in range(len(sort_str)):
        #     for j in range(i, len(sort_str)):
        #         if sort_str[i] == sort_str[j]:
        #

        return sort_str
'''
        sorted(s)
        test = []
        for i in sort_str:
            test.append(''.join(i))
'''
s = Solution()

print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams(""))
print(s.groupAnagrams("a"))

