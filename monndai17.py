# 단어 맞추기 게임 
import random

# 단어를 넣을 리스트 설정 
list_words = [] 

# 반복할 횟수 리스트 설정 
list_num = ['첫 ', '두 ', '세 '] 

# for문으로 단어 입력 반복 
for num in list_num :
    word = input(f'{num}번째 단어를 입력하세요\n')
    # 단어 길이 조건을 충족할 경우 list_words 리스트에 Create 
    if 5 <= len(word) <= 20 :
        list_words.append(word) 
    # 길이 조건을 충족하지 않을 경우 충족할 때까지 반복 
    else : 
        while True : 
            re_word = input('5이상 20이하 글자로 구성된 단어를 입력하세요\n')
            if 5 <= len(re_word) <= 20 :
                list_words.append(re_word)
                break 
            else :
                re_word  
# 입력한 단어 중 랜덤으로 하나 선택 후 출력 
ran = random.choice(list_words) 
print(f'\n단어 선택 완료 게임을 시작합니다. 선택된 단어 : {ran}')

# blind 처리할 단어의 인덱스 리스트 만들기 
indexes = list(range(len(ran))) 

# 단어 길이에 맞게 blind 처리할 글자 개수 설정 
num_to_hide = round(len(ran) / 2 + 0.1) 
# 랜덤으로 blind 처리할 인덱스 설정 
hide_indexes = random.sample(indexes, num_to_hide) 

# for문과 enumerate()를 활용한 blind 처리 
blinded = [ch if i not in hide_indexes else '_' for i, ch in enumerate(ran)]

# .join 으로 출력 
print(f'문제 단어 :', ' '.join(blinded)) 

# 반복할 때마다 증가할 attempts 설정 
attempts = 1 
# '_' 이 blinded에 있을 경우 True 반복 설정 
while '_' in blinded :
    # 입력 안내 출력 
    print(f'\n{attempts}번째 시도, 아래 단어를 구성하는 글자를 한 개 입력하세요.')
    print(' '.join(blinded)) 
    
    # attempts에 1 추가
    attempts += 1
    
    # 추즉 글자 입력 
    guess = input() 
    
    # guess가 1글자가 아닐 경우 다시 입력 
    if len(guess) != 1 :
        print('\n한 글자만 입력하세요.')
        continue
    
    # 만약 입력한 글자가 ran에 포함되어 있을 경우 설정 
    if guess in ran :
        hit = 0 
        updated = False
        # enumerate() 로 인덱스와 그 값을 전체 스캔하여 변수에 각각 저장 
        for i, ch in enumerate(ran) :
            # 만약 blind 처리된 곳에 추측한 글자가 있을 경우 hit 1증가, blind 제거 
            if guess == ch and blinded[i] == '_' :
                hit += 1 
                blinded[i] = guess 
                updated = True 
        # 결과 출력 
        if updated :
            print(f'\n입력한 글자 단어 내 포함 : {hit}글자')
        else :
            print('\nblind 처리되지 않는 글자입니다.')
    # 만약 포함되지 않았을 경우 잘못된 입력 출력 
    else : 
        print('\n단어 내 포함되지 않는 글자입니다.')
# 결과 출력 
print(f'\nClear - 선택된 단어 : {ran}, 총 시도 횟수 : {attempts - 1}')