def lonelyinteger(a):
    # Write your code here
    hash = {}
    for num in a:
        if num not in hash:
            hash[num] = 1
        else:
            hash[num] += 1

    for h in hash:
        if hash[h] == 1:
            return h