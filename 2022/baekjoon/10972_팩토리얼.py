n = int(input())

def fact(n):
    if n >= 1:
        return n * fact(n-1)
    else:
        return 1

print(fact(n))

'''
def fact(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * fact(n-1)
'''