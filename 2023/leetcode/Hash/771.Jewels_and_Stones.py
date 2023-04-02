class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # j : 보석, s: 돌
        # s에 보석이 몇 개나 있는지, 대소문자 구별
        # 한 글자라도 같으면 같은 보석

        # 해시 테이블 선언
        freq = {}
        count = 0

        # 해시 테이블 생성
        freq = {}
        for c in stones:
            if c not in freq: # key-value 한 쌍 생성
                freq[c] = 1
            else:
                freq[c] += 1

        # 보석의 개수 세기
        count = 0
        for c in jewels:
            if c in freq:
                count += freq[c] # 이미 값을 세었으니 한번에 추가 가능


        return count
s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))