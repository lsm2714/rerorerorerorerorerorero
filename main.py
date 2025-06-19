'''def add_numbers(*args, **kwargs) :
    
    # args 리스트로 만들기 
    numbers = list(args) 
    
    # 아래 3개 이외의 key값이 있을 경우 None 출력 
    keys = list(('abs', 'only_even', 'unique'))
    for k in kwargs.keys() :
        if k not in keys :
            return None 
    
    # kwargs에 abs가 있을 경우 설정 
    if 'abs' in kwargs and kwargs['abs'] == True :
        numbers = [abs(num) for num in numbers]
        
    # kwargs에 only_even이 있을 경우 설정 
    if 'only_even' in kwargs and kwargs['only_even'] == True :
        numbers = [num for num in numbers if num % 2 == 0]
        
    # kwargs에 unique가 있을 경우 설정 
    if 'unique' in kwargs and kwargs['unique'] == True :
        temp = [] 
        for num in numbers :
            if temp and temp[-1] == num :
                continue
            temp.append(num)
        numbers = temp
    
    total = 0
    for num in numbers :
        total += num 
    print(f'합계는 {total}입니다.') 

add_numbers(1, -2, 2, -3)

add_numbers(1, -2, 2, -3, abs=True, only_even=True) 

add_numbers(1, 2, 2, 3, 3, 4, unique=True)

add_numbers(1, 2, 3, round=True)'''

students = {} 

while True :
    menu = int(input('''
===== 학생 성적 관리 프로그램 =====
1. 학생 성적 입력 
2. 학생 성적 출력
3. 학생 성적 확인
4. 학생 성적 삭제 
5. 종료 
메뉴 선택 (1~5): '''))
    
    # 1번 선택 설정 
    if menu == 1 :
        ID = int(input('학번 입력: '))
        if ID in students :
            print('이미 등록된 학번입니다.')
            continue 
        name = input('이름 입력: ')
        kor = int(input('국어 성적 입력: '))
        eng = int(input('영어 성적 입력: '))
        math = int(input('수학 성적 입력: '))
        total = kor + eng + math 
        avg = total / 3
        students[ID] = {
            '이름' : name,
            '국어' : kor,
            '영어' : eng,
            '수학' : math,
            '합계' : total,
            '평균' : avg 
        }
        print('성적이 저장되었습니다.')
    
    # 2번 선택 설정 
    elif menu == 2 :
        if students == {} :
            print('저장된 학생 정보가 없습니다.')
            continue
        print('\n[ 전체 학생 성적 ]')
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
        for key, value in students.items() :
            print(f'{key}\t{value['이름']}\t{value['국어']}\t{value['영어']}\t{value['수학']}\t{value['합계']}\t{value['평균']:.2f}')
    
    # 3번 선택 설정 
    elif menu == 3 :
        if students == {} :
            print('조회할 학번이 저장되어 있지 않습니다.')
            continue
        check = int(input('조회할 학번 입력: '))
        if check not in students :
            print('해당 학번의 학생 정보가 없습니다.')
            continue
        else :
            value = students[check] 
            print('\n[ 학생 정보 ]')
            print(f'학번 : {check}')
            print(f'이름 : {value['이름']}')
            print(f'국어 : {value['국어']}')
            print(f'영어 : {value['영어']}')
            print(f'수학 : {value['수학']}')
            print(f'합계 : {value['합계']}')
            print(f'평균 : {value['평균']:.2f}')
    
    # 4번 선택 설정 
    elif menu == 4 : 
        if students == {} :
            print('저장된 학생 정보가 없습니다.')
            continue
        delete = int(input('삭제할 학번 입력: '))
        if delete not in students :
            print('해당 학번의 학생 정보가 없습니다.')
            continue
        else :
            del students[delete]
            print('학생 정보가 삭제되었습니다.')
    
    # 5번 선택 설정 
    elif menu == 5 :
        print('프로그램을 종료합니다.')
        break
    
    # 잘못된 입력 설정 
    else :
        print('잘못된 입력입니다.')
        continue