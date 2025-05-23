"""# 리스트 요소의 CRUD 조작 
# 빈 리스트 만들기 
aita_list = [] 

# 작업 입력 (반복)
while True :
    CRUD = int(input('''
작업을 선택하세요 : 
1: 추가 (Create)
2: 조회 (Read)
3: 수정 (Update)
4: 삭제 (Delete)
5: 종료 (Exit)
입력 : '''))
    
    # 인덱스 리스트 만들기 
    indexes = list(range(len(aita_list)))

    # 입력한 숫자에 따라 올바른작업 실행 
    # 추가 
    if CRUD == 1 :
        create = input('추가할 값을 입력하세요 : ')
        aita_list.append(create) 
        print('추가 완료')
    # 조회 
    if CRUD == 2 :
        print('\n[현재 리스트 내용]')
        for i, ch in enumerate(aita_list) :
            print(f'{i} : {ch}')
    # 수정 
    if CRUD == 3 :
        create_index = int(input('수정할 인덱스를 입력하세요 : '))
        if create_index in indexes :
            update2 = input('새로운 값을 입력하세요 : ')
            aita_list[create_index] = update2 
            print('수정 완료')
        else :
            print('유효하지 않은 인덱스입니다.')
    # 삭제 
    if CRUD == 4 :
        delete_index = int(input('삭제할 인덱스를 입력하세요 : '))
        if delete_index in indexes :
            aita_list.pop(delete_index)
            print('삭제 완료')
        else :
            print('유효하지 않은 인덱스입니다.')
    # 종료 
    if CRUD == 5 :
        print('프로그램을 종료합니다.')
        break"""
# 문자열 검색 및 위치 찾기 
# 미리 지정된 문자열 
text = 'apple banana orange apple kiwi apple mango'

# 빈 리스트 만들기 
list_text = []
# 문자열 리스트에 넣기 
bar = ''
for val in text :
    # val이 ' '가 아닐 때만 bar에 val 더하기 
    if val != ' ' :
        bar += val 
    # ' '일 경우 리스트에 bar 추가
    else :
        list_text.append(bar)
        # bar 초기화 
        bar = ''
# 마지막 단어도 추가 
list_text.append(bar)

# 찾을 문자열 입력 
find_text = input('찾을 문자열을 입력하세요 : ')

# 입력한 문자열이 리스트 안에 있을 경우 총 등장 횟수와 위치 (인덱스) 출력 
count1 = 0
for idx1 in list_text :
    if idx1 == find_text :
        count1 += 1
print(f'"{find_text}"은 총 {count1}번 등장합니다.')

count2 = 0
index_list = []
for idx2 in list_text :
    if idx2 == find_text :
        index_list.append(count2)
    count2 += 1
print(f'위치 (인덱스) : {index_list}')
    
        
        
