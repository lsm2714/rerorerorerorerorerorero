# pygame 모듈 불러오기 
import pygame 

# 원활한 실행을 위해 init() 메서드 설정
pygame.init() 

# 화면 크기 설정 
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000 

# 음악 설정 
pygame.mixer.music.load('yume.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play() 

# FPS 설정 
clock = pygame.time.Clock() 

# 노트 리스트 만들기 : 시간(ms), x 좌표, y 좌표 
notes = [ 
    {'time' : 1000, 'x' : 300, 'y' : -50},
    {'time' : 2000, 'x' : 500, 'y' : -50},
    {'time' : 3000, 'x' : 400, 'y' : -50}
]

# 현재 떨어지고 있는 노트들을 담을 리스트 
falling_notes = []

# 화면 크기 적용, 이름 설정 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption('正夢') 

# 화면이 계속 출력될 수 있게 while 반복문에 True 조건 설정 
running = True
while running :
    current_time = pygame.time.get_ticks() # 현재 시간 설정 (ms) 
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
            
    # 이미지 등이 겹쳐 보이지 않게 fill() 메서드 사용
    display_surface.fill((0, 0, 0))
    
    # 노트 시간 확인 후 떨어뜨릴지 결정하기 
    for note in notes[:] :
        if current_time >= note['time'] :
            falling_notes.append(note)
            notes.remove(note)
    
    # 떨어지고 있는 노트들의 위치 업데이트 
    for note in falling_notes :
        note['y'] += 5  # 사각형 그리기 ( 화면, (색상), (x축 위치, y축 위치, 너비, 높이))
        pygame.draw.rect(display_surface, (255, 255, 0), (note['x'], note['y'], 50, 20))
    
    # 판정 라인 그리기 (화면, 색상, 시작 지점(y), 끝 지점(x), 선의 굵기)
    pygame.draw.line(display_surface, (255, 0, 0), (0, 900), (WINDOW_WIDTH, 900), 5)
    
    # 화면 업데이트 
    pygame.display.update() 
    
    # FPS 적용 
    clock.tick(60)

# 원활한 종료를 위해 pygame.quit() 설정 
pygame.quit() 