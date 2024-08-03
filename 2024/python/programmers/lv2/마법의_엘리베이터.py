def solution(storey):
    ans = 0
    while storey:
        temp = storey % 10
        
        # 6 ~ 9
        if temp > 5:
            ans += (10 - temp)
            storey += 10
        
        # 0 ~ 4
        elif temp < 5:
            ans += temp 
    
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            ans += temp
        storey //= 10
        
    return ans
    