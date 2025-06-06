# 추가값 넣을 리스트 만들기 
list_value = []

# 반복 설정 
while True :
    num = int(input('''
작업을 선택하세요 :
1: 추가 (Create)
2: 조회 (Read)
3: 수정 (Update)
4: 삭제 (Delete)
5: 종료 (Exit)
입력 : '''))
    
    # 인덱스 리스트 설정 
    list_index = []
    for i, ch in enumerate(list_value) :
        list_index.append(i)

    # 종료 설정 
    if num == 5 :
        print('프로그램을 종료합니다.')
        break
    # 추가 설정 
    elif num == 1 :
        input_value = input('추가할 값을 입력하세요 : ')
        list_value.append(input_value)
        print('추가 완료.')
    # 조회 설정 
    elif num == 2 :
        print('\n[현재 리스트 내용]')
        for i, ch in enumerate(list_value) :
            print(f'{i} : {ch}')
    # 수정 설정 
    elif num == 3 :
        input_value = int(input('수정할 인덱스를 입력하세요 : '))
        if input_value in list_index :
            new = input('새로운 값을 입력하세요 : ')
            list_value[input_value] = new 
            print('수정 완료.')
        else : 
            print('유효하지 않은 인덱스입니다.')
    # 삭제 설정 
    elif num == 4 :
        input_value = int(input('삭제할 인덱스를 입력하세요 : '))
        if input_value in list_index :
            del list_value[input_value]
            print('삭제 완료.')
        else :
            print('유효하지 않은 인덱스입니다.')
    # 잘못된 입력 설정 
    else :
        print('잘못된 입력입니다. 올바른 번호를 입력하세요.')