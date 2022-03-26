from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

'''
(결과)
Runtime: 379 ms, faster than 12.94% of Python3 online submissions for Reverse String.
'''

'''
<풀이 -1>
class Solution:
    def reverseString(self, s: List[str]) -> None:
        print(s[::-1])

(결과)
출력 결과가 다름 
['o', 'l', 'l', 'e', 'h'] 로 출력됨 

(원인)
원래 문자열 슬라이싱은 리스트에도 사용이 가능함 
근데 이 문제는 공간 복잡도가 O(1)로 제한이 되어 있어 오류가 발생한다. 

(해결)
s[:] = s[::-1]
'''

'''
<풀이 -2>
Two Pointer 사용 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) -1
        while (left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1

(결과)
Runtime: 299 ms, faster than 38.92% of Python3 online submissions for Reverse String.

'''
sol = Solution()
print(sol.reverseString(["h","e","l","l","o"]))
print(sol.reverseString(["H","a","n","n","a","h"]))