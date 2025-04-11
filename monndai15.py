# 가위/바위/보 확장 버전, 랜덤 모듈 가져오기 
import random 

# 랜덤으로 선택한 값을 컴퓨터에 저장 
list_value = ['가위', '바위', '보']
computer = random.choice(list_value)

# 승패무 변수 선언
win = 0
lose = 0
draw = 0

# while 반복문에 count < 3 조건을 걸어 세 번 반복하게 하기
count = 0
while count < 3 :
# 가위/바위/보 입력 
    input_value = input('\n가위, 바위, 보 중 하나를 입력하세요 : ')
    if input_value != '가위' and input_value != '바위' and input_value != '보' :
       print('잘못된 입력입니다. 가위, 바위, 보 중에서 입력하세요')
       exit()
    
    # 입력할 때마다 count에 1씩 추가 
    count += 1
    
    # 가위 바위 보 규칙 정하기 
    if input_value == computer :
        print('무승부!', end=' ') # 여기서 end=' '은 아래에 있는 print()를 옆으로 끌고오는 기능을 가지고 있다. 
        draw += 1
    elif (input_value == '가위' and computer == '보') or \
        (input_value == '바위' and computer == '가위') or \
        (input_value == '보' and computer == '바위') :
            print('승리!', end=' ') 
            win += 1
    else :
        print('패배!', end=' ')
        lose += 1
    print(f'현재 전적 : {win}승 {lose}패 {draw}무')
   
# 가위 바위 보 결과 출력 
print(f'\n최종 전적 : {win}승 {lose}패 {draw}무')
if win > lose :
    print('최종 승자 : 이승민')
elif lose > win :
    print('최종 승자 : 파소콩')
else : 
    print('최정 결과 : 무승부')























































'''# 가위 바위 보 확장판 만들기
# 랜덤 모듈 불러오기 
import random 

# 승/패/무 변수를 0으로 선언(1씩 추가해야 하므로)
win = 0
lose = 0
draw = 0

# count = 0으로 변수 선언한 후 while 반복문에 조건으로 달기
count = 0

while count < 3 : # 3회 반복이므로 3보다 작을 때 True (0~2)
    # 가위/바위/보 입력하고 잘못된 입력 구분하기 
    print()
    input_value = input('가위, 바위, 보 중에서 입력하세요 : ')
    if input_value != '가위' and input_value != '바위' and input_value != '보' :
        print('잘못된 입력입니다. 가위, 바위, 보 중에서 입력하세요')
        exit() 
        
    # input()으로 입력할 때마다 count에 1추가
    count += 1
    
    # 컴퓨터가 랜덤으로 선택한 값 출력 
    list_value = ['가위', '바위', '보']
    computer = random.choice(list_value)
    print(f'컴퓨터의 선택 : {computer}')
    
    # 가위/바위/보 규칙 정하고 결과에 따라 승/패/무 에 1씩 추가하기 
    if input_value == computer :
        print('무승부!', end=' ') # 아래의 print()를 끌고 오기 위해 옆에다가 end=' ' 입력 
        draw += 1 
    elif (input_value == '가위' and computer == '보') or \
        (input_value == '바위' and computer == '가위') or \
        (input_value == '보' and computer == '바위') :
        print('승리!', end=' ')
        win += 1
    else :
        print('패배!', end=' ')
        lose += 1
    print(f'현재 전적 : {win}승 {lose}패 {draw}무')

# 3회 반복 후 알맞은 출력 
print(f'\n전적 : {win}승 {lose}패 {draw}무')
if win > lose :
    print('최종 승자 : 이승민')
elif lose > win :
    print('최종 승자 : 파소콩')
else :
    print('최종 결과 : 무승부 ')'''







            