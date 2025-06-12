# 메뉴로 구성된 구구단과 삼각형 출력 프로그램
import random 

# 반복 설정 
while True : 
    # 원하는 메뉴 입력 
    menu = int(input('''---------------------
1. 구구단 출력 
2. 랜덤값 삼각형 출력 
3. 종료 
---------------------
원하는 메뉴 번호를 입력하세요: ''')) 
    
    # 구구단 설정
    if menu == 1 : 
        while True : 
            gugudan = input('출력한 구구단을 아래 형식으로 입력하세요 (예: 2, 4~8)\n')
            if '~' in gugudan:
                gugudan_int = gugudan.split('~') # '~'를 기준으로 리스트에 저장 
                gugudan_int = [int(val) for val in gugudan_int] # 정수형으로 변환 
                gugudan_int_list = []
                for num in range(gugudan_int[0], gugudan_int[1] + 1) :
                    gugudan_int_list.append(num)
                # 1, 두자릿수 제한 (반복) 
                if any(num == 1 or num >= 10 for num in gugudan_int) : # 하나의 조건이라도 충족할 경우 반복 
                    print('2~9 사이의 값을 입력하세요')
                    continue
                # 올바른 입력일 경우 구구단 출력 
                for num1 in gugudan_int_list :
                    for num2 in range(10) :
                        print(f'{num1} * {num2} = {num1 * num2}')
                        if num2 == 9 :
                            print() 
                break
            else : 
                gugudan = int(gugudan) 
                # 1, 두자릿수 제한 (반복) 
                if gugudan == 1 or gugudan >= 10 : 
                    print('2~9 사이의 값을 입력하세요')
                    continue
                # 올바른 입력일 경우 구구단 출력  
                for num2 in range(10) :
                    print(f'{gugudan} * {num2} = {gugudan * num2}')
                    if num2 == 9 :
                        print() 
                break
    # 랜덤 삼각형 설정 
    elif menu == 2 :
        while True :
            triangle = int(input('삼각형의 높이 줄 수를 입력하세요(2이상 3이하)\n'))
            # 줄 수 조건 설정 
            if 3 >= triangle >= 2 :
                # 랜덤 숫자로 이루어진 삼각형 출력 설정 
                list_random = []
                for ran in random.sample([val for val in range(10)], 10) :
                    list_random.append(ran) 
                for num in range(1, triangle + 1) :
                    # ' ' 출력 설정 
                    for _ in range(triangle - num) :
                        print(' ', end='')
                    # 랜덤 숫자 출력 설정 
                    for _ in range(num) :
                        print(list_random.pop(0), end='')
                    print() # 다음 반복 숫자가 붙지 않도록 방지 
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
        print('1~3 사이의 값을 입력하세요')
        continue