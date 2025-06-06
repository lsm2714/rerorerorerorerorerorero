# 문자열 검색 및 위치 찾기 (바닐라 버전) 
text = 'bar bar pos kin kin kin sol bar foo bar pos kin foo' 

# 문자열 넣을 리스트 추가 
word_list = []  

# 리스트에 띄어쓰기를 기준으로 문자열 집어넣기 
word = ''
for w in text :
    if w == ' ' :
        word_list.append(word)
        word = '' 
        continue
    word += w 
# 마지막 문자열도 추가 
word_list.append(word) 

# 찾을 문자열 입력 
find_word = input('찾을 문자열을 입력하세요 : ') 

# 만약 find_word가 리스트 안에 있을 경우 count 증가로 등장 횟수 출력, 인덱스의 위치 출력 
if find_word in word_list :
    count1 = 0
    count2 = 0
    index_list = []
    for find1 in word_list :
        if find1 == find_word :
            count1 += 1
    print(f'"{find_word}는 총 {count1}번 등장합니다."')
    for find2 in word_list :
        if find2 == find_word :
            index_list.append(count2)
        count2 += 1 
    print(f'위치 (인덱스) : {index_list}')
else :
    print('입력하신 단어는 존재하지 않습니다.')
    