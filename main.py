def add_numbers(*args, **kwargs) :
    
    # 숫자 리스트에 담기 
    numbers = list(args) 
    
    # 다른 key값이 있을 경우 None 반환 
    keys = list(('abs', 'only_even', 'unique'))
    for k in kwargs.keys() :
        if k not in keys :
            return None 
    
    # abs가 있을 경우 절댓값 변환 
    if 'abs' in kwargs and kwargs['abs'] == True :
        numbers = [abs(num) for num in numbers]
    
    # only_even이 있을 경우 짝수만 계산 
    if 'only_even' in kwargs and kwargs['only_even'] == True :
        numbers = [num for num in numbers if num % 2 == 0]
        
    # unique가 있을 경우 중복 제거 후 합산 
    if 'unique' in kwargs and kwargs['unique'] == True :
        temp = []
        for num in numbers :
            if temp and temp[-1] == num :
                continue
            temp.append(num)
        numbers = temp
    
    total = 0 
    for val in numbers :
        total += val
    print(f'합계는 {total}입니다.')
    
add_numbers(1, -2, 2, -3)

add_numbers(1, -2, 2, -3, abs=True, only_even=True)

add_numbers(1, 2, 2, 3, 3, 4, unique=True)

add_numbers(1, 2, 3, round=True)

