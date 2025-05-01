'''
기초공학 시험 범위는 공학의 기본 개념부터 변형율까지 
1. 최소비용원칙, 최대비용원칙
2. 1차~4차 산업혁명의 흐름 이해 
3. 기본 연산 
4. 국제단위계 기본단위 
5. 접두어 p ~ T 까지를 활용한 계산 
6. 원주율(파이) 
7. Degree 와 Radian 변환 
8. sin, cos, tan 와 아크값 
9. 면적 계산 
10. 진수 변환 문제 
11. 뉴턴의 1, 2, 3 법칙 
12. 하중의 4가지 분류
13. 힘(뉴턴) 단위 
14. 응력 구하기 문제, 지름값 구하는 문제, 하중 구하는 문제
15. 변형율 
'''

# pygame 모듈 불러오기 
import pygame 

# 원활한 실행을 위해 init() 설정 
pygame.init() 

# FPS 설정 
clock = pygame.time.Clock() 

# 화면 크기 설정
WINDOW_WIDTH = 2500
WINDOW_HEIGHT = 900

# 화면 크기 적용, 이름 설정 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('두 개의 이미지 이동 프로그램 기능 확장 ')

# 이미지 불러오기 
geo_image = pygame.image.load('geo.png')
geo_rect = geo_image.get_rect() 
geo_rect.center = (WINDOW_WIDTH//2, 300)

# 화면이 계속 출력될 수 있도록 while 반복문에 True 조건 설정 
running = True 
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
            
    # FPS 적용, 초당 200 프레임 이동 (잘 기억해 둘 것)
    speed = clock.tick(60) / 1000 # 한 장 그리는데 걸리는 시간 / 1000(1초) 
    delta = 200 # 초당 프레임 설정 
            
    # 화면 하얀색으로 칠하기 
    display_surface.fill((255, 255, 255))

    # 위치 설정 
    haha = geo_rect.center 
    
    # key 기능 추가 
    key = pygame.key.get_pressed() # get_pressed() 메서드를 입력해야 키보드에서 어떤 키가 눌렸는지 실시간으로 확인 가능 
    
    # geo 이미지 키로 움직이기 
    if key[pygame.K_a] and geo_rect.left > 0 :
        geo_rect.x -= delta * speed
    if key[pygame.K_w] and geo_rect.top > 0 :
        geo_rect.y -= delta * speed
    if key[pygame.K_s] and geo_rect.bottom < WINDOW_HEIGHT :
        geo_rect.y += delta * speed
    if key[pygame.K_d] and geo_rect.right < WINDOW_WIDTH :
        geo_rect.x += delta * speed
    
    # 사각형 설정 
    rect_index = [
        pygame.Rect(150, 100, 100, 100),
        pygame.Rect(300, 300, 150, 50),
        pygame.Rect(500, 200, 50, 150),
        pygame.Rect(400, 400, 200, 50),
    ]
    
    # 사각형 그리기 
    for kaka in rect_index : 
        pygame.draw.rect(display_surface, (0, 0, 255), kaka)
    
    # 충돌 감지 
    mama = geo_rect.collidelist(rect_index) 
    if mama != -1 :
        # 만약 충돌할 경우 이전 위치로 돌아가기 
        geo_rect.center = haha 
    
    # 이미지 출력 
    display_surface.blit(geo_image, geo_rect)
            
    # 화면 업데이트 
    pygame.display.update() 
            
# 원활한 종료를 위해 quit() 설정 
pygame.quit() 