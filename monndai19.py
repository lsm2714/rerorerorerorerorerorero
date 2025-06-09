# 학생들의 점수 리스트
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89] 

# 등급 딕셔너리 만들기 
dictionary = {'A' : [val for val in scores if val >= 90],
         'B' : [val for val in scores if 90 > val >= 80],
         'C' : [val for val in scores if 80 > val >= 70],
         'D' : [val for val in scores if 70 > val >= 60],
         'F' : [val for val in scores if 60 > val] }

# 등급 분포 및 평균 점수 출력 
print('등급 분포 및 평균 점수 :') 
for ABCDF, numbers_list in dictionary.items() :
    print(f'{ABCDF}등급 : 평균 점수 = {(sum(numbers_list) / len(numbers_list)):.2f}')
    count = 0 
    for _ in numbers_list : 
        print('*', end='')
        count += 1
    print(f' ({count}명)')