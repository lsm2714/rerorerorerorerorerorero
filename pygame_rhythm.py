# pygame 모듈 불러오기 
import pygame

# csv 모듈 불러오기
import csv 

# 원활한 실행을 위해 init() 설정 
pygame.init() 

# 화면 크기 설정 
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

# FPS 설정 
clock = pygame.time.Clock()

# 음악 설정 
pygame.mixer.music.load('Snow_Drop.mp3')
pygame.mixer.music.set_volume(0.4) 
pygame.mixer.music.play() 

# 콤보 설정 
COMBO = 0 

# 판정 텍스트, 판정 시간 변수 설정 
judgement_text = ''   
judgement_time = 0

# 텍스트 폰트 설정 
impact_font = pygame.font.SysFont('impact', 20)

# 화면 크기 적용, 이름 설정 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('파이리즈무 : Snow_Drop') 

# 노트 리스트 초기화
notes = [] 
# open()으로 파일 불러오기, newline='' 으로 빈줄 오류 방지, as로 note_file의 형태로 저장 
with open('notes.csv', newline='') as note_file : # with를 쓰는 이유는 아래에서 모든 작업을 끝낸 후 자동으로 close() 닫아줘야 오류를 막을 수 있기 때문 
    # DictReader() 로 note_file를 딕셔너리 값으로 변환 후 저장 
    reader = csv.DictReader(note_file) 
    # 딕셔너리 값을 노트 리스트에 append()로 옮기기, 그 안에서도 딕셔너리 값 설정 
    for note_data in reader :
        notes.append({
            'time' : int(note_data['time']),
            'x' : int(note_data['x']),
            'y' : int(note_data['y'])
        })

# 떨어질 때의 리스트 설정 
falling_notes = []

# 키 리스트 설정 
key_maps = {
    pygame.K_a : 75,
    pygame.K_s : 225,
    pygame.K_d : 375,
    pygame.K_f : 525
}

# 화면이 계속 출력될 수 있도록 while 반복문에 True 조건 설정 
running = True
while running :
    current_time = pygame.time.get_ticks() # 현재 시간의 흐름을 변수에 저장 
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 
            
    # 특정 시간이 될 때 떨어지기 전의 노트 삭제, 떨어질 때의 노트 리스트로 옮기기
    for note in notes[:] :
        if current_time >= note['time'] :
            falling_notes.append(note)
            notes.remove(note) 
    
    # 이미지 등이 출력될 수 있도록 fill() 으로 매 프레임마다 화면 칠하기 
    display_surface.fill((0, 0, 0))
            
    # 떨어지는 노트 움직이기 (시간 기반), 노트 그리기
    NOTE_SPEED = 0.5 
    for note in falling_notes :
        time_since_note_start = current_time - note['time'] 
        note['y'] = -50 + NOTE_SPEED * time_since_note_start 
        pygame.draw.rect(display_surface, (255, 0, 255), (note['x'], note['y'], 50, 10))

        # 키 입력에 따라 판정 설정 (노트가 떨어질 때 실행되야 하므로 움직이는 for문 아래서 실행)
        keys = pygame.key.get_pressed() # 현재 누르는 키 실시간으로 확인
        for key, x in key_maps.items() : # 딕셔너리 값 하나하나 저장 
            if keys[key] : # 현재 누른 키가 key의 값 중 하나일 경우 True 
                for note in falling_notes[:] : 
                    if abs(note['y'] - 400) < 40 and abs(note['x'] - x) < 5 :
                        abs_offset = abs(note['y'] - 400) # 양방향 판정을 위해 절댓값 함수로 +로 바꾸기 
                        if abs_offset < 10 :
                            COMBO += 1 
                            judgement_text = 'PERFECT' 
                            result_surface = impact_font.render(judgement_text, True, (255, 0, 255), None)
                        elif abs_offset < 20 :
                            COMBO += 1 
                            judgement_text = 'GREAT' 
                            result_surface = impact_font.render(judgement_text, True, (255, 102, 255), None)
                        elif abs_offset < 30 :
                            COMBO = 0
                            judgement_text = 'GOOD' 
                            result_surface = impact_font.render(judgement_text, True, (51, 204, 255), None)
                        else :
                            COMBO = 0
                            judgement_text = 'BAD' 
                            result_surface = impact_font.render(judgement_text, True, (0, 255, 153), None)
                        # 키를 누를 때 노트 삭제 and 판정 시간 = 누를 때의 시간 
                        falling_notes.remove(note)
                        judgement_time = current_time # 누르자마자 노트가 사라지므로 위 조건식이 False가 되어 딱 그 시간이 저장됨 
                        break 
                    
        # 놓친 노트 MISS 판정
        for note in falling_notes[:] :
            if note['y'] > 460 : 
                COMBO = 0
                judgement_text = 'MISS' 
                result_surface = impact_font.render(judgement_text, True, (214, 214, 214), None)
                # 460을 초과한 노트를 삭제하여 위 조건식을 False로 만들기 ( False로 만들어 줘야 다음 노트 판정 시 올바른 값이 출력된다. )
                falling_notes.remove(note) 
                # MISS 판정도 1초 동안 출력하기 위해 판정 시간 설정 
                judgement_time = current_time
    
    # 콤보 텍스트 출력
    COMBO_TEXT = impact_font.render(f'COMBO : {COMBO}', True, (255, 0, 255), None)
    display_surface.blit(COMBO_TEXT, (10, 10)) 
    
    # 판정 텍스트 출력 (1초 동안) 
    # 현재 시간 - 누를 때의 시간이 1000보다 작고 and 판정 텍스트가 True일 경우 실행
    if current_time - judgement_time < 1000 and judgement_text :
        display_surface.blit(result_surface, (250, 420))
    
    # 판정선 그리기 
    pygame.draw.line(display_surface, (214, 214, 214), (0, 400), (WINDOW_WIDTH, 400), 4)
    
    # 화면 업데이트 
    pygame.display.update() 
    
    # FPS 적용 
    clock.tick(60) 
            
# 원활한 종료를 위해 quit() 설정 
pygame.quit() 