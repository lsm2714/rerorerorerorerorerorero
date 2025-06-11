# 메뉴로 구성된 구구단과 삼각형 출력 프로그램 
import random

# 반복 
while True:
    # 메뉴 출력 
    menu = int(input('''----------------
1. 구구단 출력 
2. 랜덤 삼각형 출력 
3. 종료
----------------
원하는 메뉴 번호를 입력하세요: '''))

    # 구구단 설정 
    if menu == 1:
        input_value = input('출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n')
        if '~' in input_value:
            list_value = input_value.split('~')
            # 리스트 정수형으로 변경 
            list_value_int = [int(i) for i in list_value]
            # 2~9 사이의 값이 아닐 경우 설정
            for num in list_value_int:
                if num == 1 or num >= 10:
                    print('2~9 사이의 값을 입력하세요')
                    break
            else:
                # 연속된 숫자 리스트에 넣기 
                list_value_int_2 = []
                for num in range(list_value_int[0], list_value_int[1] + 1):
                    list_value_int_2.append(num)
                # 구구단 출력 
                for num1 in list_value_int_2:
                    for num2 in range(1, 10):
                        print(f'{num1} * {num2} = {num1 * num2}')
                    print()
        else:
            if len(input_value) == 1 and input_value != '1':
                list_value_int_2 = [int(input_value)]
                # 구구단 출력 
                for num1 in list_value_int_2:
                    for num2 in range(1, 10):
                        print(f'{num1} * {num2} = {num1 * num2}')
            else:
                print('2~9 사이의 값을 입력하세요')
    
    # 랜덤값 삼각형 설정 
    elif menu == 2 : 
        tri = int(input('삼각형의 높이 줄 수를 입력하세요 (2이상 3이하)\n'))
        if 3 >= tri >= 2 : 
            random_numbers = []
            list_tri = [str(val) for val in range(10)]
            for ran in random.sample(list_tri, 9) :
                random_numbers.append(ran)
            # 삼각형 출력 
            for n in range(1, tri + 1) :
                # ' '출력 
                for _ in range(tri - n) :
                    print(' ', end='')
                # 숫자 출력 
                for _ in range(n) :
                    print(random_numbers.pop(0), end='')
                print() 
        else :
            print('2 또는 3을 입력하세요')
            
    # 종료 설정 
    elif menu == 3 :
        print('프로그램을 종료합니다.')
        break
    # 잘못된 입력 설정 
    else : 
        print('잘못된 입력입니다. 1~3 사이의 값을 입력하세요.')