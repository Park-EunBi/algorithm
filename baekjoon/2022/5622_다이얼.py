string = list(input())

dial = {
    3: ["A", "B", "C"],
    4: ["D", "E", "F"],
    5: ["G", "H", "I"],
    6: ["J", "K", "L"],
    7: ["M", "N", "O"],
    8: ["P", "Q", "R", "S"],
    9: ["T", "U", "V"],
    10: ["W", "X", "Y", "Z"]
}

res = 0
for i in string:
    for j in range(3, 11):
        if i in dial[j]:
            res += j

print(res)