# 야구 게임 만들기 
import random 

# 0부터 9까지의 숫자 중에서 중복되지 않는 3개의 숫자 랜덤으로 선택하기 
numbers = random.sample(range(10), 3) # random.sample(리스트, 개수)의 형태로 원하는 개수만큼 리스트에서 숫자 선택 

# SBO 설정 
strike = 0 
ball = 0
out = 0

# while문으로 정해진 횟수만큼 반복 설정 
count = 1
while count < 6 :
    # 세 개의 숫자 입력 
    input_value = input(f'시도 {count} : 입력한 숫자 - ')
    # 시도할 때마다 count 증가 
    count += 1
    
    # 띄어쓰기를 기준으로 문자열 구분 
    spl = input_value.split() 
    # 문자열 리스트를 정수형으로 바꾸기 
    list_int = [int(i) for i in spl]
    
    # SBO 조건 설정, 그에따라 값 출력, 3회 반복 
    for i in range(3) : 
        # 직선끼리 같을 경우 Strike에 1추가 
        if list_int[i] == numbers[i] :
            strike += 1
        # 직선끼리 같지는 않지만 그 숫자가 numbers 리스트에 포함되어 있을 경우 ball에 1추가 
        elif list_int[i] in numbers :
            ball += 1
        # 두 조건 다 거짓일 경우 out에 1추가 
        else :
            out += 1
    # 출력이 3회 반복되지 않도록 밖에서 결과 출력 
    print(f'결과 : {strike} Strike, {ball} Ball', end='')
    
    # 만약 out이 1과 같거나 클 경우 out 출력 
    if out >= 1 :
        print(f', {out} Out\n')
        
    # Strike가 3일 경우 승리와 정답을 출력 후 반복문 빠져나가기 
    if strike == 3 :
        print('게임 종료 : 승리') 
        print('정답 : ', end='')
        for num in numbers :
            print(num, end=' ')
        break
    
    # 제한된 횟수 내에 정답을 맞추기 못했을 경우 패배와 함께 정답 출력, 반복문 빠져나가기 
    if count == 6 :
        print('게임 종료 : 패배 (시도 횟수 5회 초과)') 
        print('정답 : ', end='')
        for num in numbers :
            print(num, end=' ')
        break
    
    # for 반복이 끝날 때마다 SBO 값 초기화 
    strike = 0
    ball = 0 
    out = 0 