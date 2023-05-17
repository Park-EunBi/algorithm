def countingSort(arr):
    ret = [0] * 100
    for a in arr:
        ret[a] += 1

    return ret