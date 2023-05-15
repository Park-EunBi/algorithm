def timeConversion(s):
    # Write your code here
    if s[8:] == 'AM':
        # 12가 문자열임에 주의
        if s[:2] == '12':
            return '00'+s[2:8]
        return s[:8]

    else:
        if s[:2] == '12':
            return s[:8]
        else:
            change = str(int(s[:2]) + 12)
            return change+s[2:8]

s = input()

result = timeConversion(s)
print(result)

