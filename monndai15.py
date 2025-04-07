# 가위 바위 보 확장 버전, in, not in 사용 금지 
# 랜덤 모듈 가져오기 
import random 

# 전적 변수 선언하기 
win = 0
draw = 0
lose = 0

# count 변수 선언하여 while 반복문의 조건으로 달기 
count = 0
# 3세판이므로 3과 같을 경우 False로 루프 종료 
while count < 3 :
    print() # 공백으로 보기 편하게 하기 
    input_value = input('가위, 바위, 보 중 하나를 선택하세요 : ')
    # 만약 다른 입력일 경우 잘못된 입력입니다 출력 후 프로그램 종료 
    if input_value != '가위' and input_value != '바위' and input_value != '보' :
        print('잘못된 입력입니다. 가위, 바위, 보 중에서 선택해 주세요.')
        exit()
    # False일 경우 count에 1씩 추가 
    count += 1
    # 컴퓨터가 랜덤으로 선택한 값도 출력 
    list_value = ['가위', '바위', '보']
    computer = random.choice(list_value)
    print(f'컴퓨터의 선택 : {computer}')
    
    # 가위/바위/보 의 규칙 정하고 알맞은 값을 출력 
    if input_value == computer :
        print('무승부!', end=' ')
        draw += 1 
    elif (input_value == '가위' and computer == '보') or \
        (input_value == '바위' and computer == '가위') or \
        (input_value == '보' and computer == '바위') :
            print('승리!', end=' ') 
            win += 1
    else :
        print('패배!', end=' ')
        lose += 1
    # end=' '로 현재 전적 끌고 오기 
    print(f'현재 전적 : {win}승 {lose}패 {draw}무')
    
# 결과 출력 
print(f'\n전적 : {win}승 {lose}패 {draw}무')
if win > lose : 
    print('최종 승자 : 사용자')
elif lose > win :
    print('최종 승자 : 파소콩')
else :
    print('최종 결과 : 무승부')
            