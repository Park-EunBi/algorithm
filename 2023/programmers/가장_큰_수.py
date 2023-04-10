def solution(numbers):
    numbers = list(map(str, numbers))
    # 아래 코드는 3, 32, 34 일 때 3, 32, 34로 정렬함
    # numbers.sort(reverse = True, key = lambda x : str(x)[0])
    numbers.sort(reverse = True, key = lambda x :x * 3)

    answer = ''
    for n in numbers:
        answer += str(n)
    return str(int(answer)) # "000"일 때 제외 하기위해서 int 로 변경