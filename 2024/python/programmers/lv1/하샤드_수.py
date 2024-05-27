def solution(x):
    temp = 0
    for num in str(x):
        temp += int(num)

    return False if x % temp else True

    # SOL2
    return x % sum(int(x) for x in str(x))