def caesarCipher(s, k):
    # Write your code here
    upper_start = ord('A')
    upper_end = ord('Z')
    lower_start = ord('a')
    lower_end = ord('z')
    ret = ''
    step = lower_end - lower_start + 1
    k %= step
    for string in s:
        if string.isalpha():
            asc = ord(string)
            if lower_start <= asc and lower_end >= asc:
                if asc + k > lower_end:
                    # asc = asc - step + k - 1
                    asc = (asc - lower_start + k) % step + lower_start
                else:
                    asc += k
            elif upper_start <= asc and upper_end >= asc:
                if asc + k > upper_end:
                    # asc = asc - step + k - 1
                    asc = (asc - upper_start + k) % step + upper_start
                else:
                    asc += k
            ret += chr(asc)
        else:
            ret += string

    return ret


'''
def caesarCipher(s, k):
    k = k% 26       
    result:str = '';
    temp:str = '';
    for i in s:
        temp = chr(ord(i) + k)        
        if i <= 'Z' and i >= 'A':            
            if temp > 'Z':
                result += chr(ord(temp) - 26)
            else:
                result += temp
        elif i <= 'z' and i >= 'a':
            if temp > 'z':
                result += chr(ord(temp) - 26)
            else:
                result += temp   
        else:
            result += i
            continue                             
    return result 
'''

print(caesarCipher('middle-Outz', 2)) # okffng-Qwvb
print(caesarCipher('There\'s-a-starman-waiting-in-the-sky', 3)) # okffng-Qwvb