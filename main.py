# 딕셔너리를 활용한 학생 성적 관리 프로그램 
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
    
    # 1번 설정 
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
        
    # 2번 설정 
    elif menu == 2 :
        if students == {} :
            print('저장된 학생 성적이 없습니다.')
            continue
        print('\n[ 전체 학생 성적 ]')
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
        for key, value in students.items() :
            print(f'{key}\t{value['이름']}\t{value['국어']}\t{value['영어']}\t{value['수학']}\t{value['합계']}\t{value['평균']:.2f}')
            
    # 3번 설정 
    elif menu == 3 :
        if students == {} :
            print('조회할 학생 정보가 없습니다.')
            continue 
        check = int(input('조회할 학번 입력 : '))
        if check in students :
            value = students[check]
            print(f'학번 : {check}')
            print(f'이름 : {value['이름']}')
            print(f'국어 : {value['국어']}')
            print(f'영어 : {value['영어']}')
            print(f'수학 : {value['수학']}')
            print(f'합계 : {value['합계']}')
            print(f'평균 : {value['평균']:.2f}')
    
    # 4번 설정 
    elif menu == 4 :
        if students == {} :
            print('삭제할 학생 성적 정보가 없습니다.')
            continue
        delete = int(input('삭제할 학번 입력: '))
        if delete in students :
            del students[delete]
            print('학생 정보가 삭제되었습니다.')
        else :
            print('해당 학번의 학생 정보가 없습니다.')
            
    # 5번 설정 
    elif menu == 5 :
        print('프로그램을 종료합니다.')
        break
    
    # 잘못된 입력 설정 
    else :
        print('잘못된 입력입니다. (1~5) 사이의 숫자로 입력하세요.')