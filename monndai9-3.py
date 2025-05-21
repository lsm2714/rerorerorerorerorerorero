# 리스트 요소의 CRUD 조작 
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
        break