# 단어 맞추기 게임 
import random

# 횟수 리스트 설정 
list_num = ['첫', '두', '세']

# 단어 리스트 설정 
list_words = []

# 단어 입력 반복 설정 
for num in list_num :
    input_value = input(f'{num} 번째 단어를 입력하세요\n')
    # 단어 길이 조건 설정 
    if 5 <= len(input_value) <= 20 :
        list_words.append(input_value)
        continue
    else : # 길이 조건을 충족하지 않을 경우 충족할 때까지 입력 
        while True :
            input_value = input('5이상 20이하 글자로 구성된 단어를 입력하세요\n') 
            if 5 <= len(input_value) <= 20 :
                list_words.append(input_value) 
                break 
            else :
                input_value

# 랜덤으로 하나의 단어 선택 
ran = random.choice(list_words) 
print(f'\n단어 선택 완료. 게임을 시작합니다. 선택된 단어 : {ran}')

# 선택된 문자열의 인덱스 리스트 설정 
indexes = list(range(len(ran))) 
# 선택된 문자열의 절반을 센 숫자 설정 (홀수일 경우 반올림 ex) 9 -> 4.5 -> 5) <round() 사용 금지>
word_50P = len(ran) / 2
if word_50P % 2 != 0 :
    word_50P += 0.5
word_50P = int(word_50P)
# 랜덤으로 blind 처리할 인덱스 설정 
random_blind_indexes = random.sample(indexes, word_50P) # sample에 들어갈 숫자는 반드시 정수형이어야 함 
# blind 처리 
blinded = [ch if i not in random_blind_indexes else '_' for i, ch in enumerate(ran)]

# 문제 출력 
print('문제:',' '.join(blinded))

# 시도할 때마다 증가할 count 설정 
count = 1
# 반복 설정 ('_'가 blinded에 있을 경우 True)
while '_' in blinded :
    # 입력 안내 출력 
    print(f'\n{count}번째 시도, 아래 단어를 구성하는 글자를 한 개 입력하세요.')
    print(' '.join(blinded)) 
    
    # 추측 글자 입력 
    guess = input() 
    
    count += 1
    
    # 만약 추측 글자가 1글자가 아닌 경우 안내와 함께 다시시도 
    if len(guess) != 1 :
        print('\n한 글자만 입력하세요')
        continue
    
    # 만약 guess가 ran에 포함되어 있을 경우 설정 
    if guess in ran : 
        hit = 0
        update = False 
        for i, ch in enumerate(ran) :
            if blinded[i] == '_' and guess == ch :
                blinded[i] = guess
                hit += 1
                update = True 
        if update :
            print(f'\n입력한 단어 내 포함 : {hit}글자')
        else :
            print('\nblind 처리되지 않은 글자입니다.') 
    else :
        print('\n단어 내 포함되지 않는 글자입니다.')

# 결과 출력 
print(f'Clear - 선택된 단어 : {ran}, 총 시도 횟수 : {count - 1}')
            


