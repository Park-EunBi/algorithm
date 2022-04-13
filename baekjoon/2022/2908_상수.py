a, b = list(input().split())
new_a = []
new_b = []

for i in a:
    new_a.insert(0, i)
for i in b:
    new_b.insert(0, i)

new_a = ''.join(new_a)
new_b = ''.join(new_b)

print(max(new_a, new_b))

