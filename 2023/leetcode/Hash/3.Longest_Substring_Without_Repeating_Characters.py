class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 중복 문자가 없는 가장 긴 부분 문자열의 길이 리턴

        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장한 문자라면 start 위치 갱신
            if char in used and start <= used[char]:
                # and start <= used[char] 조건이 없다면
                # 슬라이딩 윈도우 밖에 있는 값도 확인하게 된다
                # 확인 케이스 : "tmmzuxt"
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            # 현재 문자열의 위치 삽입
            used[char] = index
            # print(used, max_length)
        return max_length


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))