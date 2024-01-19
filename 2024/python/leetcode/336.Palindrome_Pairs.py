class Node:
    def __init__(self, key):
        self.key = key
        self.palindrome = []
        self.word_id = -1
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node(None)

    @staticmethod
    def isPalindrome(word):
        return word[::] == word[::-1]

    def insert(self, index, word):
        node = self.root

        for i, ch in enumerate(reversed(word)):
            if self.isPalindrome(word[:len(word) - i]):
                node.palindrome.append(index)

            if ch not in node.children:
                node.children[ch] = Node(ch)

            node = node.children[ch]

        node.word_id = index

    def search(self, index, word):
        node = self.root

        result = []

        while word:
            if node.word_id > -1:
                if self.isPalindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result

            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        for p in node.palindrome:
            result.append([index, p])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        '''
        # sol_1 - 브루트포스 (O(n^2) 시간초과)
        ret = []
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                check_word = words[i] + words[j]
                check_word_reverse = words[j] + words[i]
                if check_word == check_word[::-1]:
                    ret.append([i, j])
                if check_word_reverse == check_word_reverse[::-1]:
                    ret.append([j, i])

        return ret
        '''

        trie = Trie()

        results = []

        for i, word in enumerate(words):
            trie.insert(i, word)

        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results