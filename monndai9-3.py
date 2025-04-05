'''# 별 패턴 그리기, 숫자 입력받기 
star = int(input('숫자를 입력하세요 : '))
# for 반복문과 range() 함수를 이용해 별 패턴 그리기
for stars in range(1, star + 1) :
    print('*' * stars)
for stars in range(star - 1, 0, -1) :
    print('*' * stars)


# input() 으로 숫자를 입력한 후 for 반복문과 range() 함수를 이용해서 별 패턴을 그려야 함. 
# 어떻게 실행되는 거냐면 for stars in range(1, star + 1) 에서 range() 안의 1은 시작 값, star + 1은 끝 값으로 for 반복문을 썼으니
# 1부터 star + 1까지 밑으로 나열됨. 나열된 숫자들을 stars에 저장한 후 print('*' * stars)에서 곱하기를 하면 '*'는 for문으로 지정된 숫자만큼 밑으로 나열되고
# stars도 1부터 지정한 숫자까지 나열되서 그걸 서로 곱해가지고 출력을 낸다.
# 예를 들어 3을 입력하면 

* ('*' * 1)
** ('*' * 2)
*** ('*' * 3)
이런 식으로 출력이 된다. 두 번째 for문도 마찬가지로 range(star - 1, 0, -1) 이므로 stars가 for문으로 인해 star - 1부터 1까지 -1씩 나열되어서 
** ('*' * 2)
* ('*' * 1) 이렇게 출력이 된다. 
한번에 나타내면 
*
**
***
**
* 
이런 식으로 출력이 된다. 
'''

'''sasa = int(input('숫자 입력ㅋ : '))

for kaka in range(1, sasa + 1) :
    print('ㅋ' * kaka)
for kaka in range(sasa - 1, 0, -1) :
    print('ㅋ' * kaka)'''
    



# 명시적 형변환 
input_value = input('숫자들을 쉼표로 구분하여 입력하세요 : ')
# 문자열에서 쉼표를 기준으로 문자 구분하기 
numbers_str = input_value.split(',')
# 문자열 리스트를 정수로 변환 
numbers_int = [int(num) for num in numbers_str]
# for 문을 활용하여 리스트 안의 숫자를 서로 더하기
result = 0
# 100을 초과할 경우 숫자를 넣을 리스트 선언 
valid_numbers = []
for num in numbers_int :
    result += num 
    valid_numbers.append(num)
    if result > 100 :
        break
if result <= 100:
    print('총합이 100을 초과하지 않았습니다.')
    print(f'입력된 모든 숫자들 : {numbers_int}')
    print(f'최종 총합 : {result}')
else:
    print('총합이 100을 초과하였습니다.')
    print(f'현재까지의 입력값들 : {valid_numbers}')
    print(f'현재까지의 총합 : {result}')

''' 

'''

    







































'''# 명시적 형변환, 사용자로부터 여러 개의 숫자를 문자열로 입력받기 
numbers_str = input('숫자들을 쉼표로 구분하여 입력하세요 : ') 
# 쉼표로 숫자들을 따로 분리하고 정수형으로 변환
numbers = numbers_str.split(',') 
numbers = [int(num) for num in numbers] # ()가 안에 있으므로 바깥 괄호는 []로 한다. 
# 입력한 모든 숫자 리스트와 숫자들을 서로 더한 값을 출력하는데 100초과 100이하도 출력 
result = 0
for num in numbers : # 리스트의 값을 하나하나 꺼내서 계산하기 위해 for 반복문 사용 
    result += num
if result > 100 :
    print_value = '총합이 100을 초과하였습니다.'
else :
    print_value = '총합이 100을 초과하지 않습니다.'
print(print_value) 
print(f'입력된 모든 숫자들 : {numbers} ')
print(f'최종 총합 : {result} ')'''

