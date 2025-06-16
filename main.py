def add_numbers(*args, **kwargs) :
    if kwargs :
        for key, value in kwargs.items() :
            if key == 'abs' and value == True :
                list_abs = []
                for num in args :
                    list_abs.append(abs(num))
            elif key == 'only_even' and value == True :
                list_num = []
                for num in list_abs :
                    if num % 2 == 0 :
                        list_num.append(num)
                print(f'합계는 {sum(list_num)}입니다.')
            elif key == 'unique' and value == True :
                list_num2 = []
                for num in args :
                    if list_num2 and num == list_num2[-1] :
                        continue
                    list_num2.append(num) 
                print(f'합계는 {sum(list_num2)}입니다.')
            else :
                print(None)
                        
    else :
        print(f'합계는 {sum(args)}입니다.')

add_numbers(1, -2, 2, -3)

add_numbers(1, -2, 2, -3, abs=True, only_even=True)

add_numbers(1, 2, 2, 3, 3, 4, unique=True)

add_numbers(1, 2, 3, round=True)