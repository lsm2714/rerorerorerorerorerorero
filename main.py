book_dict = {} 
menu_list = ['소설', '만화', '과학', '종료']

# 반복 설정 
while True : 
    menu = input('도서 장르를 입력하세요 (예: 소설, 만화, 과학, 종료): ')
    if menu not in menu_list :
        print('올바르지 않은 입력입니다. 소설, 만화, 과학, 종료 중에서 선택하세요.')
        continue 
    if menu == '종료' :
        break
    name = input('책 제목을 입력하세요: ')
    # 딕셔너리 設定 
    if menu not in book_dict :
        book_dict[menu] = {name : 1}
    else : 
        if name in book_dict[menu] :
            book_dict[menu][name] += 1
        else : 
            book_dict[menu][name] = 1
    
# 대여 기록 출력 
if book_dict == {} :
    print('저장된 대여 기록이 존재하지 않습니다.')
else : 
    print('\n--- 장르별 대여 기록 ---')
    for k1, v1 in book_dict.items() : 
        print(f'[{k1}]')
        all_num_list = []
        for k2, v2 in v1.items() :
            print(f'{k2}: {v2}회')
        for v3 in v1.values() :
            all_num_list.append(v3)
        print(f'총 대여 수: {sum(all_num_list)}회')
        
    





            