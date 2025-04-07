# random 모듈 불러오기 
import random

# 가위 바위 보 리스트 만들기 
list_value = ['가위', '바위', '보']

# 가위 바위 보 input 
input_value = input('가위, 바위, 보 중에서 하나를 선택하세요 : ')
if not input_value in list_value :
    print('지금은 가위 바위 보 중입니다.')
    exit()
 
# 컴퓨터는 랜덤으로 가위, 바위, 보 중에서 선택함  
computer = random.choice(list_value)
print(f'컴퓨터의 선택 : {computer}') 

# 규칙 입력 
if input_value == computer :
    result = '비김'
elif input_value == '가위' and computer == '보' or input_value == '바위' and computer == '가위' or input_value == '보' and computer == '바위' : 
    result = '당신의 승리'
else :
    result = 'ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ'
print(result)