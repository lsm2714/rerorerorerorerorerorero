# 명시적 형변환 
# 숫자들을 쉼표로 구분하여 입력받기 
numbers_str1 = input('숫자들을 쉼표로 구분하여 입력하세요 : ') 

# 쉼표를 기준으로 문자열 구분하기 
numbers_str2 = numbers_str1.split(',')

# 문자열 리스트를 정수형 리스트로 변환
numbers_int = [int(num) for num in numbers_str2] 

number = 0 # 이후의 계산을 위한 값 0 설정 
vaild_number = [] # 100이 넘을 경우 따로 담을 리스트 만들기 

# 모든 숫자의 합 계산 
for num in numbers_int :
    if number > 100 :
        break # 100을 초과할 때 break를 걸어 반복을 멈추어 딱 100을 초과하는 숫자까지만 리스트에 담게 하기
    vaild_number.append(num)
    number += num 
    
# 결과 출력 
# 만약 100을 초과할 경우와 아닌 경우 설정 
if number > 100 :
    print('총합이 100을 초과하였습니다.')
    print(f'현재까지의 입력값들 : {vaild_number}')
    print(f'현재까지의 총합 : {number}')
else : 
    print('총합이 100을 초과하지 않았습니다.') 
    print(f'입력된 모든 숫자들 : {numbers_int}')
    print(f'최종 총합 : {number}')


    

