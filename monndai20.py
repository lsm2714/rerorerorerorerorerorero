# 메뉴로 구성된 구구단과 삼각형 출력 프로그램 
import random

# 반복 설정 
while True :
    # 메뉴 입력 
    menu = int(input('''---------------------
1. 구구단 출력 
2. 랜덤값 삼각형 출력 
3. 종료 
---------------------
원하는 메뉴 번호를 입력하세요: '''))
    
    # 구구단 출력 설정 
    if menu == 1 :
        while True : 
            gugudan = input('출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n')
            if '~' in gugudan :
                gugudan_list = gugudan.split('~')
                gugudan_list = [int(i) for i in gugudan_list]
                if any(num <= 1 or num >= 10 for num in gugudan_list) :
                    print('2~9 사이의 값으로 입력하세요')
                    continue
                for num1 in range(gugudan_list[0], gugudan_list[1] + 1) :
                    for num2 in range(10) :
                        print(f'{num1} * {num2} = {num1 * num2}')
                        if num2 == 9 :
                            print() 
            else :
                gugudan = int(gugudan)
                if gugudan <= 1 or gugudan >= 10 :
                    print('2~9 사이의 값으로 입력하세요')
                    continue
                for num in range(10) :
                    print(f'{gugudan} * {num} = {gugudan * num}')
            break
    
    # 랜덤값 삼각형 출력 
    elif menu == 2 :
        while True : 
            triangle = int(input('삼각형의 높이 줄 수를 입력하세요 (2이상 3이하)\n'))
            if 3 >= triangle >= 2 :
                numbers = [num for num in range(10)]
                random_numbers = [num for num in random.sample(numbers, 10)]
                for num in range(1, triangle + 1) :
                    # ' ' 출력 
                    for _ in range(triangle - num) :
                        print(' ', end='')
                    # 랜덤 숫자 출력 
                    for _ in range(num) :
                        print(random_numbers.pop(0), end='')
                    print() 
            else :
                print('2 또는 3을 입력하세요')
                continue
            break
    # 종료 설정 
    elif menu == 3 :
        print('프로그램을 종료합니다.')
        break
    
    # 잘못된 입력설정 
    else : 
        print('잘못된 입력입니다. 1~3 중에 선택하세요')
        continue