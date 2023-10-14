import sys
# hash
tree_hash = {}
total = 0
while 1:
    tree = sys.stdin.readline().rstrip()

    if tree == '':
        break

    if tree not in tree_hash:
        tree_hash[tree] = 1
    else:
        tree_hash[tree] += 1
    total += 1

# 비율 계산
tree_hash = sorted(tree_hash.items())

for t in tree_hash:
    # round 사용하면 틀림
    print(t[0], "%.4f" %(t[1]/total * 100))