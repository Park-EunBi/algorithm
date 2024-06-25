def solution(a, b):
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

    # 흘러간 날짜를 구하기
    passed = sum([
        day[i]
        for i in range(a - 1)
    ]) + b

    # 7로 나눈 수를 인덱스로 활용
    return week[(passed + 4) % 7]

'''
# sol2)
def getDayName(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]
'''
