# 주민등록번호 검사기 만들기, 주민등록번호 입력
resident = input('주민등록번호를 입력하세요 : ')
# 계산해야 되므로 하이픈 기호 제거
numbers = resident.replace('-', '')
# 앞 12자리 숫자와 곱할 숫자 리스트 만들기 
multipilers = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

# for 반복문과 zip() 함수를 사용하여 각각의 숫자를 곱한 후 더하기 
result = 0 
for digit, mul in zip(numbers[:-1], multipilers) :
    result += int(digit) * mul 
# 계산할 거 계산하기 
result = (11 - (result % 11) ) % 10 
# 마지막 숫자와 일치할 것
last_digit = result
if  last_digit == int(numbers[-1]) :
    print('유효한 주민번호입니다.')
else :
    print('유효하지 않은 주민번호입니다.')











































'''# 주민번호 유효성 검사기 만들기, 주민번호 입력하기 
Resident = input('주민번호를 입력하세요 : ')
# 문자열에서 앞 12자리의 숫자와 곱할 숫자들의 리스트 만들기 
multipliers = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
# 숫자를 곱할 때 방해되는 하이픈 기호 제거 
numbers = Resident.replace("-", "") # .replace() 함수 사용시 문자열을 원하는 대로 바꾸기 가능 (바꿀 문자열, 바꾼 후의 문자열)
# for 반복문과 zip() 함수를 사용하여 마지막 숫자를 제외한 12자리 숫자와 리스트의 숫자를 각각 곱하고 서로 더하기 
number = 0 # number = 0을 반복문 밖에 놔둬야 하는 이유는 반복문 안에 들어가면 반복하면서 더한 값이 0으로 초기화되기 때문이다. 
for Res, mul in zip(numbers[:-1], multipliers) :
    number += int(Res) * mul  
# 계산할 거 계산하기 
result = (11 - (number % 11) ) % 10 
# 주민번호 마지막 숫자와 result가 같을 경우 유효한 비밀번호 
last_number = int(numbers[-1])
if result == last_number :
    print('유효한 주민번호입니다.')
else :
    print('유효하지 않은 주민번호입니다.')'''