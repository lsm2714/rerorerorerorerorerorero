# 단어 맞추기 게임 
import random 

# 저장할 단어 리스트 설정 
list_words = [] 

# 반복할 횟수 리스트 설정 
numbers = ['첫 ', '두 ', '세 '] 

# for 반복문으로 반복 설정 
for num in numbers :
    word = input(f'{num}번째 단어를 입력하세요\n')
    # 만약 단어가 길이 조건을 충족할 경우 list_words 리스트에 담기 
    if 5 <= len(word) <= 20 :
        list_words.append(word)
    # 충족하지 못할 경우 충족할 때까지 반복 
    else :
        while True : 
            re_word = input('5이상 20이하 글자로 구성된 단어를 입력하세요\n')
            if 5 <= len(re_word) <= 20 :
                list_words.append(re_word) 
                # 충족할 경우 break로 반복문 빠져나가서 위의 for 반복 실행 
                break 
            else :
                re_word

# 입력한 3개의 단어 중 하나 랜덤으로 선택 
ran = random.choice(list_words) 
print(f'\n단어 선택 완료 게임을 시작합니다. 선택된 단어 : {ran}')

# 선택한 단어의 위치 번호를 리스트에 저장 
indexes = list(range(len(ran))) 

# 단어 길이에 맞게 숨길 단어의 개수 설정 
num_to_hide = round(len(ran) / 2 + 0.1) 
# 랜덤으로 숨길 위치 설정 
hide_indexes = random.sample(indexes, num_to_hide) 

# for 반복문과 enumerate()를 활용한 blind 처리 
blinded = [ch if i not in hide_indexes else '_' for i, ch in enumerate(ran)] 

# join으로 출력 
print('문제 단어 :', ' '.join(blinded)) 

# 반복할 때마다 증가할 attempts 설정 
attempts = 1 

# while 반복문으로 반복 설정 (blinded에 '_'이 있을 경우 True)
while '_' in blinded :
    print(f'\n{attempts}번째 시도, 아래 단어를 구성하는 글자 한 개를 입력하세요.')
    print(' '.join(blinded)) 
    
    # 추즉 글자 입력, 입력할 때마다 attempts 증가 
    guess = input() 
    attempts += 1
    
    # 만약 1글자가 아닐 경우 잘못된 입력 출력 
    if len(guess) != 1 :
        print('\n한 글자만 입력하세요')
        continue 
    
    # 만약 입력한 글자가 ran에 포함되어 있을 경우 설정 
    if guess in ran : 
        hit = 0 
        updated = False # 새로 맞춘 글자가 있는지 체크 
        # enumerate()는 전체를 스캔하므로 뒷글자를 입력해도 정상 처리된다.
        for i, ch in enumerate(ran) :
            if guess == ch and blinded[i] == '_' :
                blinded[i] = guess 
                hit += 1 
                updated = True 
        if updated:
            print(f'\n입력한 단어 내 포함 : {hit}글자')
        else:
            print('\n이미 모든 글자를 맞췄습니다.')
    # 포함되어 있지 않을 경우 
    else :
        print('\n단어 내 포함되지 않은 글자입니다.')

# while 반복문을 빠져나올 경우 정답과 총 시도 횟수 출력 
print(f'\nClear - 선택된 단어 : {ran}, 총 시도 횟수 : {attempts - 1}')
    
        