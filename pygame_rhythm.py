# pygame 모듈 불러오기 
import pygame 

# 원활한 실행을 위해 init()로 pygame 초기화 
pygame.init() 

# 화면 크기 설정
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500 

# 콤보 텍스트 설정 
COMBO = 0 

# 판정 시간, 판정 텍스트 미리 설정 
judgement_time = 0
judgement_text = ''

# FPS 설정 
clock = pygame.time.Clock() 

# 음악 넣기 
pygame.mixer.music.load('INSOMNIA.mp3')
pygame.mixer.music.set_volume(0.4) 
pygame.mixer.music.play()

# 화면 크기 적용, 이름 설정하기 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('파이리즈무 : INSOMNIA')

# 판정 폰트 설정 
impact_font = pygame.font.SysFont('impact', 20)

# 노트 리스트 설정 : 시간, x, y 좌표
notes = [
    {'time' : 1000, 'x' : 75, 'y' : -50},
    {'time' : 2000, 'x' : 225, 'y' : -50},
    {'time' : 3000, 'x' : 375, 'y' : -50},
    {'time' : 4000, 'x' : 525, 'y' : -50}
]

# 현재 떨어지는 노트를 따로 분리할 리스트 선언 
falling_notes = []

# ASDF 키 리스트 설정 
key_maps = {
    pygame.K_a : 75,
    pygame.K_s : 225,
    pygame.K_d : 375,
    pygame.K_f : 525
}

# 화면이 계속 실행될 수 있게 while 반복문으로 True 조건 실행하기
running = True 
while running :
    # 현재 시간 저장 
    current_time = pygame.time.get_ticks() 
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 
            
    # for 반복문 활용하여 특정 시간이 되면 떨어지는 노트 따로 분리, 원래 리스트의 노트를 삭제 
    for note in notes[:] :
        if current_time >= note['time'] :
            falling_notes.append(note) 
            notes.remove(note) 
    
    # 화면 검은색으로 덮어서 이미지가 움직일 때 겹쳐 보이지 않게 하기 
    display_surface.fill((0, 0, 0))
    
    # 떨어지는 노트 그리기, 이동 속도 설정 (시간 기반) 
    NOTE_SPEED = 0.7 # 속도 설정 (곱할 것이기 때문에 1 이하가 적당)
    for note in falling_notes :
        # 노트 시작 변수는 현재 시간 - 특정 시간 을 해서 값이 점점 커지게 하기 
        time_since_note_start = current_time - note['time'] 
        # 노트가 떨어지는 속도 설정 
        note['y'] = -50 + NOTE_SPEED * time_since_note_start 
        # 사각형의 노트 그리기 
        pygame.draw.rect(display_surface, (255, 0, 255), (note['x'], note['y'], 50, 10))
        
        # 키 설정
        keys = pygame.key.get_pressed() # 누른 키를 실시간으로 keys 변수에 전달 
        
        # 노트 판정, 판정 텍스트 출력 
        for key, x in key_maps.items() :
            if keys[key] : # 여기서 누른 키의 값에 따라 그에 맞는 x값을 가져온다. 
                for note in falling_notes[:] :
                    if abs(note['x'] - x) < 5 and abs(note['y'] - 400) < 30 : 
                        offset = note['y'] - 400 
                        abs_offset = abs(offset) # 절댓값으로 바꿔주는 이유 : 
                        # 이게 바꾸기 전( 그냥 offset 값으로 판정 설정 )에서는 371의 위치에서 클릭해도 PERFECT가 떴던 건 
                        # 371 - 400 = -29 로 첫 번째 if 조건식 ( < 10 )과 일치하니까 PERFECT가 출력됬던거고 이제 이걸 절댓값으로 바꾸니까 
                        # -가 사라져서 맨 위에서 클릭하면 29가 되서 MISS 출력
                        # 옵셋 값에 따라 판정 텍스트, 콤보 설정 
                        if abs_offset < 10 :
                            COMBO += 1 
                            judgement_text = 'PERFECT'
                            result_text = impact_font.render(judgement_text, True, (255, 0, 255), None)
                        elif abs_offset < 20 :
                            COMBO += 1 
                            judgement_text = 'GREAT'
                            result_text = impact_font.render(judgement_text, True, (255, 240, 71), None)
                        else :
                            COMBO = 0
                            judgement_text = 'MISS'
                            result_text = impact_font.render(judgement_text, True, (214, 214, 214), None)
                        # 위의 조건식이 True이면 ASDF 중 하나 누른 후 note 삭제 
                        judgement_time = current_time # 노트 삭제와 동시에 노트가 사라지니까 위의 조건식이 초기화가 되어서 딱 그 순간의 값이 저장됨 
                        falling_notes.remove(note)
                        break # 오류 방지 
        
    # 판정선 그리기 
    pygame.draw.line(display_surface, (214, 214, 214), (0, 400), (WINDOW_WIDTH, 400), 4)
    
    # 판정 텍스트 출력 (1초 동안) 
    if current_time - judgement_time < 1000 and judgement_text :
        display_surface.blit(result_text, (300, 450))
        
    # 콤보 수 출력 
    combo_text = impact_font.render(f'COMBO : {COMBO}', True, (255, 0, 255), None)
    display_surface.blit(combo_text, (10, 10))
    
    # 화면 계속 업데이트
    pygame.display.update() 
        
    # FPS 설정 
    clock.tick(60)

# 화면의 원활한 종료를 위해 quit() 설정 
pygame.quit() 