# https://school.programmers.co.kr/learn/courses/30/lessons/60060
# p.370
import sys
sys.setrecursionlimit(100001)

def solution(words, queries):
    answer = []
    # ? 부터 단어가 시작될 때
    rev_words = []
    # 단어의 개수
    counted = []

    for w in words:
        rev_words.append(w[::-1])
        counted.append(len(w))

    # ? 로 단어가 끝날 때 사용할 trie
    trie = make_trie({}, words)
    # ? 로 단어가 시작할 때 사용할 trie
    rev_trie = make_trie({}, rev_words)

    for query in queries:
        # 모든 글자가 ? 일 때
        if query[0] == '?' and query[-1] == '?':
            answer.append(counted.count(len(query)))
        # ? 로 시작할 때
        elif query[0] == '?':
            answer.append(search_trie(rev_trie, query[::-1], len(query)))
        # ? 로 끝날 때
        elif query[-1] == '?':
            answer.append(search_trie(trie, query, len(query)))

    return answer

def make_trie(trie, words):
    for word in words:
        cur = trie
        l = len(word)
        for w in word:
            if w in cur:
                cur = cur[w]
                cur['!'].append(l)
            else:
                cur[w] = {}
                cur = cur[w]
                cur['!'] = [l]
    return trie

def search_trie(trie, query, length):
    count = 0
    if query[0] == '?':
        return trie['!'].count(length)
    elif query[0] in trie:
        count += search_trie(trie[query[0]], query[1:], length)
    return count