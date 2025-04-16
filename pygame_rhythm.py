# pygame 모듈 불러오기 
import pygame 

# 원활한 실행을 위해 init() 메서드 설정 
pygame.init() 

# 판정 텍스트, 시간 초기값 설정 
judgement_text = None
judgement_timer = 0

# 화면 크기 설정 
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

# 판정 텍스트 설정 
system_font = pygame.font.SysFont('impact', 20)

judgement_text = system_font.render('', True, (0, 0, 0), None)
judgement_text_rect = judgement_text.get_rect()
judgement_text_rect.center = (WINDOW_WIDTH - 330, 350)

# 음악 설정 
pygame.mixer.music.load('yume.mp3')
pygame.mixer.music.set_volume(0.4) 
pygame.mixer.music.play() 

# FPS 설정 
clock = pygame.time.Clock() 

# 화면 크기 적용, 이름 설정 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption('正夢')

# 노트 리스트 설정 : 시간, x, y 좌표 
notes = [
    {'time' : 1000, 'x' : 75, 'y' : -50},
    {'time' : 2000, 'x' : 225, 'y' : -50},
    {'time' : 3000, 'x' : 375, 'y' : -50},
    {'time' : 4000, 'x' : 525, 'y' : -50}
]

# 떨어지는 상태의 노트를 추가할 리스트 생성 
falling_notes = [] 

# 판정 함수 만들기 
def check_judgement(line_x) : 
    global judgement_text, judgement_timer
    for note in falling_notes :
        # 먼저 같은 라인인지 확인 (x좌표가 같아야 함) 
        if abs(note['x'] - line_x) < 10 :
            # 그다음 y좌표로 판정 distance = 거리 
            distance = abs(note['y'] - JUDGEMENT_LINE_Y)
            if distance < 20 :
                judgement_text = system_font.render('PERFECT', True, (255, 102, 255), None)
                judgement_timer = pygame.time.get_ticks()
                falling_notes.remove(note)     
                return
            elif distance < 50 :
                judgement_text = system_font.render('GOOD', True, (255, 204, 0), None)
                judgement_timer = pygame.time.get_ticks()
                falling_notes.remove(note)  
                return
            else :
                judgement_text = system_font.render('MISS', True, (191, 191, 191), None)
                judgement_timer = pygame.time.get_ticks()
                falling_notes.remove(note)  
                return

# 화면이 계속 출력될 수 있도록 while 반복문에 True 조건 설정 
running = True 
while running :
    current_time = pygame.time.get_ticks() # 현재 흘러가는 시간을 변수에 저장 
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT : 
            running = False 
                # asdf 키보드 입력 감지하기 
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_a :
                check_judgement(75)
            if event.key == pygame.K_s :
                check_judgement(225)
            if event.key == pygame.K_d :
                check_judgement(375)
            if event.key == pygame.K_f :
                check_judgement(525)
            
    # 이미지 등이 겹쳐 보이지 않게 fill() 메서드로 검게 칠하기 
    display_surface.fill((0, 0, 0))
    
    # 특정 시간이 되면 떨어지기 전의 노트를 삭제
    # 떨어지는 상태의 노트 구분을 설정하여 각각의 리스트에 집어넣어 오류 방지  
    for note1 in notes[:] :
        if current_time >= note1['time'] :
            falling_notes.append(note1)
            notes.remove(note1)
    
    # 노트 그리기, 자동으로 움직이기 
    for note2 in falling_notes : 
        note2['y'] += 5 # 떨어지는 특정 노트의 속도를 설정하고 아래의 사각형의 y좌표와 같기 때문에 
        # 사각형이 8의 속도로 내려갈수 있는 것이다.
        pygame.draw.rect(display_surface, (255, 255, 0), (note2['x'], note2['y'], 50, 20))
    
    # 판정선 기준 위치 선언하고 그리기 
    JUDGEMENT_LINE_Y = 400
    pygame.draw.line(display_surface, (255, 0, 0), (0, JUDGEMENT_LINE_Y), (WINDOW_WIDTH, JUDGEMENT_LINE_Y), 5)
    
    # 판정 텍스트 출력 
    if judgement_text and pygame.time.get_ticks() - judgement_timer < 1000 :
        display_surface.blit(judgement_text, judgement_text_rect)
            
    # 화면을 FPS마다 업데이트 
    pygame.display.update() 
    
    # FPS 적용 
    clock.tick(60) 

# 원활한 종료를 위해 quit() 설정 
pygame.quit() 