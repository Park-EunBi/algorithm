n = int(input())
words = set()
for _ in range(n):
    w = input()
    words.add((w, len(w)))

words = list(words)
words.sort(key = lambda x : (x[1], x[0]))
for w in words:
    print(w[0])