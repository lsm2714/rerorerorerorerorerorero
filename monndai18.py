# 학생들의 점수 리스트 
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99] 

# 우수, 양호, 보통, 미흡 나누기 
best = [val for val in scores if val >= 90]
good = [val for val in scores if 90 > val >= 70]
soso = [val for val in scores if 70 > val >= 50]
bad = [val for val in scores if 50 > val]

# 결과 출력 
print(f'우수 : {best} 평균 : {sum(best) / len(best)}')
print(f'양호 : {good} 평균 : {sum(good) / len(good)}')
print(f'보통 : {soso} 평균 : {sum(soso) / len(soso)}')
print(f'미흡 : {bad} 평균 : {sum(bad) / len(bad)}')
