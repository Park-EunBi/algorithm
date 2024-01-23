class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sol_1
        return sorted(s) == sorted(t)