# 단어 맞추기 게임 
import random 

# 단어를 넣을 리스트 설정 
words = []

# 단어 입력 리스트 만들기 
number = ['첫 ', '두 ', '세 ']

# 단어 세 개 입력 
for num in number :
    word = input(f'{num}번째 단어를 입력하세요.\n')
    # 단어 길이에 맞게 조건 설정 
    if 5 <= len(word) <= 20 :
        words.append(word) 
    # 만약 위 조건식을 충족하지 못했을 경우에는 다시 입력 
    else : 
        running = True
        while running :
            re_word = input('5이상 20이하 글자로 구성된 단어를 입력하세요.\n')
            if 5 <= len(re_word) <= 20 :
                words.append(re_word)
                break 
            else : 
                re_word 
# 게임 시작 출력과 랜덤으로 선택된 단어 출력 
ran = random.choice(words)
print(f'\n단어 선택 완료 게임을 시작합니다. 선택된 단어 : {ran}')

# 선택한 단어 blind 처리 설정 
# 선택한 단어의 위치 번호를 indexes에 저장 
indexes = list(range(len(ran)))      

# 단어의 길이의 50% 정도로 blind 처리할 위치 번호 설정 
num_to_hide = round((len(ran) / 2) + 0.1) # blind할 개수 설정, round로 반올림 
hide_indexes = set(random.sample(indexes, num_to_hide))

# for문과 enumerate()를 활용한 blind 처리 
blinded = [ch if i not in hide_indexes else '_' for i, ch in enumerate(ran)]

# .join()으로 리스트 틀 제거 후 출력 
print('문제 단어 :', ' '.join(blinded))

# 단어 맞추기 설정 
# 반복할 때마다 증가할 attpemts 설정 
attempts = 1 

# while 반복문으로 단어 입력 ('_'가 blinded에 있을 경우 True)
while '_' in blinded :
    print(f'\n{attempts}번째 시도, 아래 단어를 구성하는 글자를 한 개 입력하세요.')
    print(' '.join(blinded)) 
    
    # 추측 글자 입력 설정 
    guess = input() 
    
    # 만약 추측 글자가 1글자 초과일 경우 다시 입력 
    if len(guess) > 1 :
        print('\n한 글자 이상 입력하세요.')
        attempts += 1
        # 다시 while문으로 올라가기 
        continue 
    
    # 반복할 때마다 attenpts 1추가 
    attempts += 1
    
    # 알맞은 글자를 입력할 경우 blind 제거 후 위로 올리기 
    if guess in ran :
        hit = 0 # 알맞은 단어의 개수마다 증가할 hit 설정 
        # enumerate() 로 선택된 단어의 위치 번호와 문자를 전체 스캔하여 문자가 뒤에 있어도 정상 동작되게 하기 
        for i, ch in enumerate(ran) :
            # 만약 guess과 ch가 같고 그 위치에 '_'가 있을 경우 hit 증가, '_' 을 guess로 바꾸기 
            if ch == guess and blinded[i] == '_' :
                blinded[i] = guess 
                hit += 1
            # 포함된 글자의 수 출력 
        print(f'\n입력한 글자 단어 내 포함 : {hit}글자')
    # 위의 조건이 True가 아닌 경우 포함되지 않다고 출력 
    else :
        print('\n단어 내 포함되지 않는 글자입니다.')    
# while 반복문을 빠져나갈 경우 결과와 시도 횟수 출력 
print(f'\nClear - 선택된 단어 : {ran}, 총 시도 횟수 : {attempts - 1}') 
        