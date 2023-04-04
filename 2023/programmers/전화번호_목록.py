# 한 번호가 다른 번호의 접두어인지 확인
# 접두어인 경우가 있다면 false, 아니면 true 반환
def solution(phone_book):
    '''
    # 1. 완탐 - 시간 초과
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                return False
            if phone_book[j].startswith(phone_book[i]):
                return False
    else:
        return True
    '''

    '''
    # 2. sort - 뒤만 확인하면 된다
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # if phone_book[i] in phone_book[i+1]: # 오답
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        else:
            return True

    print(phone_book)
    '''

    # 3. hash
    phone = {}
    for p in phone_book:
        if p not in phone:
            phone[p] = 1
        else:
            phone[p] += 1

    check = ''
    for p in phone_book:
        for i in range(len(p)):
            if p[0:i] in phone:
                # print(p[0: i])
                return False
    else:
        return True
    print(phone)

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))