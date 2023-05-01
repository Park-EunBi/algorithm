answer = 0
def dfs(idx, numbers, target, result):
    global answer
    n = len(numbers)
    if idx == n and target == result:
        answer += 1
        return
    if idx == n:
        return
    dfs(idx + 1, numbers, target, result - numbers[idx])
    dfs(idx + 1, numbers, target, result + numbers[idx])

def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer

'''
# bfs 
def solution(numbers, target):
    leaves = [0]
    count = 0
    
    for num in numbers:
        temp = []
        
        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)
        leaves = temp
    for leaf in leaves:
        if leaf == target:
            count += 1
            
    return count 
'''