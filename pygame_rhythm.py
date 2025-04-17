# pygame 모듈 불러오기 
import pygame 

# 원활한 실행을 위해 init() 메서드 설정 
pygame.init() 

# 화면 크기 설정 
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

# 음악 설정 
pygame.mixer.music.load('yume.mp3')
pygame.mixer.music.set_volume(0.4) 
pygame.mixer.music.play() 

# FPS 설정 
clock = pygame.time.Clock() 

# 콤보 변수 추가 
COMBO = 0 

# 화면 크기 적용, 이름 설정 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption('正夢')

# 판정 폰트 설정 
impact_font = pygame.font.SysFont('impact', 20)

# 떨어지는 상태의 노트를 추가할 리스트 생성 
falling_notes = [] 

# 노트 리스트 설정 : 시간, x, y 좌표 
notes = [
    {'time' : 1000, 'x' : 75, 'y' : -50},
    {'time' : 2000, 'x' : 225, 'y' : -50},
    {'time' : 3000, 'x' : 375, 'y' : -50},
    {'time' : 4000, 'x' : 525, 'y' : -50}
]

# 키별 라인 설정 (a, s, d, f)
key_map = {
    pygame.K_a : 75,
    pygame.K_s : 225,
    pygame.K_d : 375,
    pygame.K_f : 525,
}

# 판정 결과 변수 추가 
judgement_text = "" 
judgement_time = 0 

# 화면이 계속 출력될 수 있도록 while 반복문에 True 조건 설정 
running = True 
while running :
    current_time = pygame.time.get_ticks() # 현재 흘러가는 시간을 변수에 저장 
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            running = False 
            
    # 이미지 등이 겹쳐 보이지 않게 fill() 메서드로 검게 칠하기 
    display_surface.fill((0, 0, 0))
    
    # 특정 시간이 되면 떨어지기 전의 노트를 삭제
    # 떨어지는 상태의 노트 구분을 설정하여 각각의 리스트에 집어넣어 오류 방지  
    for note in notes[:] :
        if current_time >= note['time'] :
            falling_notes.append(note)
            notes.remove(note)
    
    # 노트의 이동 속도 설정, 노트 그리기 (시간 기반)
    NOTE_SPEED = 0.7 # 노트 속도 설정 (곱할 것이기 때문에 0.n 정도가 좋다.)
    for note in falling_notes :
        # 현재 시간 - 정해진 시간을 노트 시작 변수에 실시간으로 저장 
        # 아래를 보면 만약 현재 시간이 10000일 때 'time'키도 10000이 되므로 빼면 0부터 다시 시작하여 속도가 앞의 것들과 일치한 것이다.
        time_since_note_start = current_time - note['time']  
        note['y'] = -50 + NOTE_SPEED * time_since_note_start 
        pygame.draw.rect(display_surface, (255, 104, 255), (note['x'], note['y'], 50, 10))
        
        # 키 입력 판정 처리 (for문 안에 넣는 거 맞음) 
        keys = pygame.key.get_pressed() 
        
        for key, x in key_map.items() :
            if keys[key] :
                for note in falling_notes[:] :
                    if abs(note['x'] - x)  < 5 and abs(note['y'] - 400) < 30 :
                        offset = abs(note['y'] - 400) 
                        if offset < 10 :
                            judgement_text = 'PERFECT'
                            COMBO += 1
                            result_surface = impact_font.render(judgement_text, True, (255, 0, 255), None)
                        elif offset < 20 :
                            judgement_text = 'GOOD' 
                            COMBO += 1 
                            result_surface = impact_font.render(judgement_text, True, (255, 240, 71), None)
                        else :
                            judgement_text = 'MISS'
                            COMBO = 0
                            result_surface = impact_font.render(judgement_text, True, (214, 214, 214), None)
                        judgement_time = current_time
                        falling_notes.remove(note) 
                        break
    
    # 판정선 그리기 
    pygame.draw.line(display_surface, (214, 214, 214), (0, 400), (WINDOW_WIDTH, 400), 4)
    
    # 콤보 출력
    combo_text = impact_font.render(f'COMBO : {COMBO}', True, (255, 102, 255), None)
    display_surface.blit(combo_text, (10, 10))
    
    # 판정 텍스트 출력 (1초 유지) 
    if current_time - judgement_time < 1000 and judgement_text :
        display_surface.blit(result_surface, (250, 450))
            
    # 화면을 FPS마다 업데이트 
    pygame.display.update() 
    
    # FPS 적용 
    clock.tick(60) 

# 원활한 종료를 위해 quit() 설정 
pygame.quit() 