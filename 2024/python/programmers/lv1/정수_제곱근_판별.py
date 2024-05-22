import math


def solution(n):
    temp = math.sqrt(n)

    if temp - int(temp):
        return -1
    else:
        return (temp + 1) ** 2