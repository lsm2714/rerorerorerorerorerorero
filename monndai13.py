
'''print("1", end='ㅁㅁ')
print("2", end='ㅁㅁ')
print("3")

# end=' '는 아래에 있는 print() 함수를 위로 끌고 오는 것 (무조건 end=' '의 형태이어야 함)'''

# 공백을 기준으로 특정 단어의 출현 빈도 계산 
# 문자열 입력 
input_value1 = input('문자열 입력 : ')
# 단어 입력 
input_value2 = input('단어 입력 : ')
# 띄어쓰기를 기준으로 단어 구분
input_value1 = input_value1.split()
# 단어의 출현 빈도 계산 후 출력 
words = input_value1.count(input_value2)
print(f'단어 "{input_value2}"의 출현 빈도 : {words}')



'''print("1", end='ㅁㅁ')
print("2", end='ㅁㅁ')
print("3")

# end=' '는 아래에 있는 print() 함수를 위로 끌고 오는 것 (무조건 end=' '의 형태이어야 함)'''






















































'''# 공백을 기준으로 문자열에서 특정 단어의 출현 빈도 계산하기 
# 문자열, 단어 입력 받기 
input_value1 = input('문자열 입력 : ')
input_value2 = input('단어 입력 : ') 
words = input_value1.split() # .split() 메서드는 문자열에 공백이나 지정한 문자나 기호 등이 있을 경우 그것을 기준으로 해 문자를 따로따로 구분해주는 역할을 하는 메서드
count = words.count(input_value2) # .count() 메서드는 '문자열'.count('특정 단어') 의 형태로 만들며 문자열 안에 특정 단어가 몇 개 들어갔는지 정수형으로 반환하는 메서드 
# 문자열 안에 단어가 들어있는지 확인과 동시에 그 단어의 개수 출력 
print(f'단어 "{input_value2}"의 출현 빈도 : {count}')'''

''' '''
    

