import re, collections
from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                 if word not in banned]

        cnt = collections.Counter(words)
        return cnt.most_common(1)[0][0]

'''
(풀이 -1)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # lower and remove . ,
        paragraph = re.sub(r"[^a-z0-9]"," ",paragraph.lower())

        # split
        word = paragraph.split(sep=' ')

        # remove banned from word
        for w in word:
            if w in banned:
                word.remove(w)

        # count the frequency of a word
        cnt = collections.Counter(word)

        return cnt.most_common(1)[0][0]


(결과)
Wrong Answer

Input     "Bob. hIt, baLl"
          ["bob", "hit"]
Output    ""
Expected  "ball" 

'''

'''
(lambda)
lambda 매개변수 : 표현식

(sort)
sort(key = a, b)
sort는 key를 여러개 등록할 수 있다. 
왼쪽 부터 차례로 적용된다. 
'''


s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.","hit"))
print(s.mostCommonWord("a.", ""))