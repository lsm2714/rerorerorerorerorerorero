# 메뉴로 구성된 구구단과 삼각형 출력 프로그램 
import random 

# 반복 설정 
while True :
    # 메뉴 입력
    menu = int(input('''-------------------
1. 구구단 출력 
2. 랜덤 삼각형 출력
3. 종료
-------------------
원하는 메뉴 번호를 입력하세요: '''))
    
    # 구구단 출력 
    if menu == 1 :
        while True :
            gugudan = input('출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n')
            if '~' in gugudan :
                list_value = gugudan.split('~')
                list_value = [int(i) for i in list_value] 
                if any(val for val in list_value if val <= 1 or val >= 10) :
                    print('2~9 사이의 값으로 입력하세요.')
                    continue
                for dan in range(list_value[0], list_value[1] + 1) :
                    for num in range(1, 10) :
                        print(f'{dan} * {num} : {dan*num}')
                        if num == 9 :
                            print()
            else : 
                gugudan = int(gugudan) 
                if gugudan <= 1 or gugudan >= 10 :
                    print('2~9 사이의 값으로 입력하세요.')
                    continue
                for num in range(1, 10) :
                    print(f'{gugudan} * {num} = {gugudan * num}')
            break
            
    # 랜덤값 삼각형 출력 
    elif menu == 2 :
        while True :
            triangle = int(input('삼각형 높이 줄 수를 입력하세요 (2 이상 3 이하)\n'))
            if 3 >= triangle >= 2 :
                random_list = [val for val in range(10)]
                random_list_num = [val for val in random.sample(random_list, 10)]
                # 삼각형 출력 
                for num in range(1, triangle + 1) :
                    # ' ' 출력 
                    for _ in range(triangle - num) :
                        print(' ', end='')
                    # 랜덤 숫자 출력 
                    for _ in range(num) :
                        print(random_list_num.pop(0), end='')
                    print() 
                break 
            else : 
                print('2 또는 3을 입력하세요')
                continue
    # 종료 설정 
    elif menu == 3 :
        print('프로그램을 종료합니다.')
        break
    
    # 잘못된 입력 설정 
    else :
        print('잘못된 입력입니다. 1~3 중에 선택하세요')
        continue