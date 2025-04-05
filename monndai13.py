# 공백을 기준으로 문자열에서 특정 단어의 출현 빈도 계산후 출력하기 
# 문자열 입력 
input_value1 = input('문자열을 입력하세요 : ')
# 특정 단어 입력 
input_value2 = input('단어를 입력하세요 : ')
# 공백을 기준으로 단어를 나눠야 되므로 .split() 메서드 사용 
words = input_value1.split() # 공백을 기준으로 구분할 것이기 때문에 .split() 함수 안에 아무것도 입력안해도 됨
# 문자열이나 리스트에서 특정 단어나 요소의 출현 빈도를 세려면 .count() 메서드를 사용할 것 
count = words.count(input_value2)
print(f'단어 "{input_value2}"의 출현 빈도 : {count}')































































'''# 공백을 기준으로 문자열에서 특정 단어의 출현 빈도 계산하기 
# 문자열, 단어 입력 받기 
input_value1 = input('문자열 입력 : ')
input_value2 = input('단어 입력 : ') 
words = input_value1.split() # .split() 메서드는 문자열에 공백이나 지정한 문자나 기호 등이 있을 경우 그것을 기준으로 해 문자를 따로따로 구분해주는 역할을 하는 메서드
count = words.count(input_value2) # .count() 메서드는 '문자열'.count('특정 단어') 의 형태로 만들며 문자열 안에 특정 단어가 몇 개 들어갔는지 정수형으로 반환하는 메서드 
# 문자열 안에 단어가 들어있는지 확인과 동시에 그 단어의 개수 출력 
print(f'단어 "{input_value2}"의 출현 빈도 : {count}')'''

''' '''
    

