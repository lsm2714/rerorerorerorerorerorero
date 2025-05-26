# 문자열 검색 및 위치 찾기 (바닐라 버전)

# 미리 정의된 문자열 설정 
text = 'bar bar pos foo kin bar mab pos foo bar sol sol bar foo kin' 

# 문자열을 띄어쓰기 기준으로 리스트에 집어넣기 
bar = ''
list_text = []
for val in text :
    # 문자열 단어 리스트에 넣기.
    if val == ' ' :
        list_text.append(bar)
        bar = '' # bar 초기화로 다음 단어 시작  
        continue
    # 단어 만들기 
    bar += val
    
# 마지막 단어 추가 
list_text.append(bar)

# 찾을 문자열 입력 
find_text = input('찾을 문자열을 입력하세요 : ')

# 만약 있을 경우 그 문자열의 개수 세기 
count = 0
if find_text in list_text :
    for find in list_text :
        if find == find_text :
            count += 1
    print(f'{find_text}는 총 {count}번 등장합니다.')
# 위치 (인덱스) 리스트에 추가 
    index = 0 
    list_index = []
    for find_index in list_text :
        if find_index == find_text :
            list_index.append(index)
        index += 1 
    print(f'위치 (인덱스) : {list_index}')
else :
    print('입력하신 문자열은 없는 문자열입니다.')

    