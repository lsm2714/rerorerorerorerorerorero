# 사칙연산 계산기 만들기, 전역변수와 지역변수를 사용할 것
# 기본값 입력 
baseValue = int(input('기본값을 입력하세요 : '))
# 사칙연산 출력 
for calculation in '1. 더하기', '2. 빼기', '3. 곱하기', '4. 나누기' :
    print(calculation) 
# 1부터 4 중에 선택하기 
choice = int(input('1부터 4 중에 선택하세요 : '))
if 0 == choice or choice > 4 :
    print('잘못된 입력입니다. 1부터 4 중에서 선택하세요')
# 숫자 입력하기 
number = int(input('숫자를 입력하세요 : ')) 
# 만약 4를 선택하고 0을 입력했을 경우 
if choice == 4 and number == 0 :
    print('에러 : 0으로 나올 수 없습니다.')
    exit()
if choice == 1 :
    print(f'연산 결과 : {baseValue + number}')
elif choice == 2 :
    print(f'연산 결과 : {baseValue - number}')
elif choice == 3 :
    print(f'연산 결과 : {baseValue * number}')
else :
    print(f'연산 결과 : {baseValue / number}')


