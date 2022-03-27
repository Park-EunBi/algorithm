from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit, alpha = [], []

        for log in logs:
            if log.split()[1].isdigit():
               digit.append(log)
            else:
                alpha.append(log)
        alpha.sort(key=lambda x:(x.split()[1:],x.split()[0]))
        return alpha + digit

'''
(결과)
Runtime: 40 ms, faster than 84.50% of Python3 online submissions for Reorder Data in Log Files.
'''

sol = Solution()
print(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print(sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))