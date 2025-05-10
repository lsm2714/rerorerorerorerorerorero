# 점수 분류 및 평균 계산 
# 학생들의 점수 리스트 
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89] 

# 점수에 따라 등급 분류 (딕셔너리)
list_value_Dict = {
    'A' : [i for i in scores if i >= 90],
    'B' : [i for i in scores if 90 > i >= 80],
    'C' : [i for i in scores if 80 > i >= 70], 
    'D' : [i for i in scores if 70 > i >= 60], 
    'F' : [i for i in scores if i < 60] 
}

# 등급 출력, 평균 점수도 
print('등급 분포 및 평균 점수 : ')
# 딕셔너리 값을 하나하나 저장하기
for ABCDF, list_value in list_value_Dict.items() :
    print(f'{ABCDF}등급 : 평균 점수 = {(sum(list_value) / len(list_value)):.2f}')
    for i in list_value : 
        print('*', end='')
    print(f' {len(list_value)}명') 