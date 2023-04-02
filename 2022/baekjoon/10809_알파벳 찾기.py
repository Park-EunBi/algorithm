s = list(input())

alphabet = []
for i in range(26):
    alphabet.append(-1)

for i in range(len(s)):
    index = ord(s[i]) - 97
    if (alphabet[index] == -1):
        alphabet[index] = i

for i in range(len(alphabet)):
    print(alphabet[i], end=' ')