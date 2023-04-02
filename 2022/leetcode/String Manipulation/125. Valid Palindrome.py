class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        new_s = s[::-1]
        if s == new_s:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama")) # True
print(s.isPalindrome("race a car")) # False
print(s.isPalindrome(" ")) # True
print(s.isPalindrome("0P")) # False

# Runtime: 40 ms, faster than 96.90% of Python3 online submissions for Valid Palindrome.

'''
<풀이 - 1>
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalpha()).lower()
        new_s = s[::-1]
        if s == new_s:
            return True
        else:
            return False

input : "0P"
output: True
expected: False

숫자도 남겨야 한다. 숫자와 알파벳을 대상으로 팰린드롬을 확인하는 문제이다.
(수정)
s = ''.join(char for char in s if char.isalpha() or char.isnumeric()).lower()

(결과) 
Runtime: 47 ms, faster than 87.90% of Python3 online submissions for Valid Palindrome.
'''

'''
<풀이 - 2>
# 정규식 사용 
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-z0-9]","",s)
        new_s = s[::-1]
        if s == new_s:
            return True
        else:
            return False

(결과)
Runtime: 54 ms, faster than 74.67% of Python3 online submissions for Valid Palindrome.
'''

'''
<풀이 - 3>
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for a in s:
            if a.isalnum():
                new_s.append(a.lower())
        while len(new_s) > 1:
            if new_s.pop(0) != new_s.pop():
            # 한번이라도 같으면 True를 반환하기 때문에
            # == 으로 조건을 달면 안된다
                return False
        return True

(결과)
Runtime: 288 ms, faster than 5.03% of Python3 online submissions for Valid Palindrome.
'''

'''
<풀이 -4>
# deque 이용 
import collections
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for a in s:
            if a.isalnum():
                strs.append(a.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

(결과)
Runtime: 66 ms, faster than 54.92% of Python3 online submissions for Valid Palindrome.
'''

