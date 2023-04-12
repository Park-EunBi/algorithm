from itertools import product
def solution(word):
    # 몇 번째 단어인리 리턴 
    # 모두 카운트

    make_word = ['A', 'E', 'I', 'O', 'U']
    result = []

    for i in range(1, 6):
        for c in product(make_word, repeat=i):
            result.append(''.join(list(c)))
    result.sort()
    return result.index(word) + 1 