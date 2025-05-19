# 단어 맞추기 게임 
import random 

# 입력한 단어를 넣을 빈 리스트 만들기 
list_words = [] 

# 단어 횟수 리스트 만들기 
numbers = ['첫', '두', '세']

# 단어 입력
for num in numbers :
    word = input(f'{num} 번째 단어를 입력하세요\n')
    # 단어 길이 조건 맞추기 
    if 5 <= len(word) <= 20 :
        list_words.append(word) 
    # 길이 조건을 충족하지 않을 경우 충족할 때까지 반복 
    else :
        while True : 
            re_word = input('5이상 20이하 글자로 구성된 단어를 입력하세요\n')
            if 5 <= len(re_word) <= 20 :
                list_words.append(word)
                # 충족할 경우 break로 빠져나가기 
                break
            # 아닐 경우 무한 반복 
            else :
                re_word
# 리스트에서 랜덤으로 단어 선택 후 출력 
ran = random.choice(list_words) 
print(f'\n단어 선택 완료 게임을 시작합니다. 선택된 단어 : {ran}')

# 선택한 단어의 인덱스 번호 따기 
indexes = list(range(len(ran))) 
# blind 처리할 글자 개수 정하기 50% 정도 
num_to_hide = round(len(ran) / 2 + 0.1) 
# blind 처리할 글자 개수에 맞게 인덱스 번호 랜덤으로 선택하기 
random_indexes = random.sample(indexes, num_to_hide)

# for문과 enumerate()를 활용하여 blind 처리하기 
blinded = [w if n not in random_indexes else '_' for n, w in enumerate(ran)]

# .join()으로 문제 출력 
print('문제 단어 :', ' '.join(blinded))

# 반복할 때마다 증가할 count 설정 
count = 1 

# 반복 설정 ('_'가 blinded 안에 있을 경우 True)
while '_' in blinded :
    # 단어 입력 안내 
    print(f'\n{count}번째 시도, 아래 단어를 구성하는 글자 하나를 입력하세요')
    print(' '.join(blinded)) 
    
    # 추측 글자 입력 
    guess = input() 
    count += 1
    
    # 만약 추측 글자가 1글자가 아닌 경우 안내와 함께 다시시도 
    if len(guess) != 1 :
        print('\n한 글자만 입력하세요')
        continue
    
    # 만약 입력한 글자가 ran 내에 포함되어 있을 경우 설정 
    if guess in ran :
        hit = 0 
        update = False 
        # enumerate()를 활용하여 입력한 글자와 대칭하기 
        for n, w in enumerate(ran) :
            if guess == w and blinded[n] == '_' :
                blinded[n] = guess 
                hit += 1 
                update = True 
        # updata가 True일 경우 hit와 blinded 출력 
        if update :
            print(f'\n입력한 글자 단어 내 포함 : {hit}글자')
        # 아닐 경우 출력 
        else : 
            print('\n단어에 포함되는 문자이지만 blind 처리되어 있지 않습니다.')
    # 포함되어 있지 않은 경우 출력 
    else : 
        print('\n단어 내 포함되지 않은 글자입니다.')
        
# 결과 출력 
print(f'\nClear - 선택된 단어 : {ran}, 총 시도 횟수 : {count - 1}')


