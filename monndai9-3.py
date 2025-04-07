# 명시적 형변환, 사용자로부터 여러 개의 숫자를 쉼표로 구분하여 문자열로 입력받기 
input_value = input('숫자들을 쉼표로 구분하여 입력하세요 : ')
# 쉼표를 기준으로 구분하기 
numbers_str = input_value.split(',')
# 리스트를 정수형으로 바꾸기 
numbers_int = [int(num) for num in numbers_str]
# for문을 활용하여 리스트의 각 요소를 서로 더하기 
result = 0
valid_numbers = [] # 총합이 100을 초과할 경우 넣을 리스트 선언 
for num in numbers_int :
    result += num 
    # 더하는 중 100을 넘을 경우 break 걸고 100을 넘는 숫자까지 리스트에 포함하기 
    # 100을 넘지 않아도 리스트에 포함되긴 함 
    valid_numbers.append(num)
    if result > 100 :
        break 
# 100을 넘을 경우 알맞게 출력
if result > 100 :
    print(
f'''총합이 100을 초과하였습니다.')
현재까지의 입력값들 : {valid_numbers}')
현재까지의 총합 : {result}''')
# false일 경우 알맞게 출력  
else :
    print(f'''
총합이 100을 초과하지 않았습니다.
입력된 모든 숫자들 : {numbers_int}
최종 총합 : {result}
''')
    







































