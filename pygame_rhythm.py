# pygame 모듈 불러오기 
import pygame

# 원활한 실행을 위해 init()으로 pygame 초기화
pygame.init() 

# 화면 크기 설정 
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

# FPS 설정 
clock = pygame.time.Clock() 

# 음악 설정 
pygame.mixer.music.load('INSOMNIA.mp3') 
pygame.mixer.music.set_volume(0.4) 
pygame.mixer.music.play() 

# 콤보 설정 
COMBO = 0 

# 판정 텍스트, 판정 시간 설정 
judgement_time = 0
judgement_text = ''

# 판정, 콤보 텍스트 폰트 설정 
impact_font = pygame.font.SysFont('impact', 20)

# 화면 크기 적용, 이름 설정 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('파이리즈무 : INSOMNIA')

# 노트 리스트 설정 
notes = [
    {'time' : 1000, 'x' : 75, 'y' : -50},
    {'time' : 3000, 'x' : 225, 'y' : -50},
    {'time' : 2000, 'x' : 375, 'y' : -50},
    {'time' : 4000, 'x' : 525, 'y' : -50}
]

# 떨어질 때의 노트 리스트 설정 
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
    current_time = pygame.time.get_ticks() # 현재 흘러가는 시간을 변수에 실시간으로 저장 
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 
            
    # 화면 fill() 로 칠해서 노트 등이 보이게 하기 
    display_surface.fill((0, 0, 0))
    
    # 특정 시간이 되면 떨어지기 전의 노트를 삭제하고 falling_notes리스트에 따로 저장하기
    for note in notes[:] :
        if current_time >= note['time'] :
            falling_notes.append(note) 
            notes.remove(note) 
            
    # falling_notes 리스트에 있는 노트 아래로 떨어뜨리기 (시간 기반)
    NOTE_SPEED = 0.5 
    for note in falling_notes :
        time_since_note_start = current_time - note['time'] # 현재 시간 - 특정 시간을 설정하여 0부터 증가하는변수 만들기 
        note['y'] = -50 + NOTE_SPEED * time_since_note_start 
        pygame.draw.rect(display_surface, (255, 0, 255), (note['x'], note['y'], 50, 14))
        
        # 키 설정 
        keys = pygame.key.get_pressed() 
        # 노트 판정, 콤보 수 증가 설정 
        for key, x in key_maps.items() :
            if keys[key] :
                for note in falling_notes[:] : 
                    if abs(note['x'] - x) < 5 and abs(note['y'] - 400) < 35 :
                        # abs()로 +로 바꿔주지 않으면 -34도 아래 조건에 의해 PERFECT가 출력되기 때문에 abs() 절댓값 함수로 값을 바꿔줘야 한다. 
                        abs_offset = abs(note['y'] - 400) 
                        # 판정 텍스트, 콤보 설정 
                        if abs_offset < 10 :
                            COMBO += 1 
                            judgement_text = 'PERFECT'
                            result_surface = impact_font.render(judgement_text, True, (255, 0, 255), None)
                        elif abs_offset < 20 :
                            COMBO += 1 
                            judgement_text = 'GOOD'
                            result_surface = impact_font.render(judgement_text, True, (214, 214, 0), None)
                        else :
                            COMBO = 0
                            judgement_text = 'BAD'
                            result_surface = impact_font.render(judgement_text, True, (0, 214, 104), None)
                        # 위 조건이 참일 시 노트 삭제 
                        falling_notes.remove(note)
                        judgement_time = current_time
                        break 
                    # 키를 클릭하고 노트를 삭제하고 break를 걸면 위의 조건식이 False가 되므로 
                    # 딱 그 시간의 값이 judgement_time에 저장된다. 
                    # break를 걸면 다시 키를 누르기 전까지 위 조건식이 거짓이 되므로 두 개의 노트가 동시에 판정되는 오류를 막을 수 있다. 
        
    # 판정선 그리기
    pygame.draw.line(display_surface, (214, 214, 214), (0, 400), (WINDOW_WIDTH, 400), 4)  
    
    # 콤보 텍스트 설정
    combo_text = impact_font.render(f'COMBO : {COMBO}', True, (255, 0, 255), None)
    display_surface.blit(combo_text, (10, 10))
    
    # 판정 텍스트 출력 (1초 동안) 
    if current_time - judgement_time < 1000 and judgement_text :
        display_surface.blit(result_surface, (250, 450))
              
    # 화면 업데이트
    pygame.display.update() 
    
    # FPS 설정 
    clock.tick(60) 

# 원활한 종료를 위해 quit() 설정 
pygame.quit() 