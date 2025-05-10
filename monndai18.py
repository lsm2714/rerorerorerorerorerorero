# 학생들의 점수 리스트 
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99] 

# 리스트 안의 숫자에 따라 우수, 양호, 보통, 미흡 분류 (List comprehension 사용)
best = [i for i in scores if i >= 90]

good = [i for i in scores if 90 > i >= 70]

soso = [i for i in scores if 70 > i >= 50]

bad = [i for i in scores if 50 > i]

# 출력 
print(f'우수 : {best} 평균 : {sum(best) / len(best)}')
print(f'양호 : {good} 평균 : {sum(good) / len(good)}')
print(f'보통 : {soso} 평균 : {sum(soso) / len(soso)}')
print(f'미흡 : {bad} 평균 : {sum(bad) / len(bad)}')

kaka = max(best)

print(kaka)