# pygame 모듈 불러오기 
import pygame 

# 원활한 실행을 위해 init() 로 pygame 초기화
pygame.init() 

# 화면 크기 설정
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1000

# 초당 프레임 설정
clock = pygame.time.Clock()

# 공의 이동 속도, 방향 설정 
ball_dx = 4
ball_dy = 4

# 화면 크기 적용, 이름 설정 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('벽돌깨기 게임')

# 구출할 캐릭터, 벽돌을 깰 공, 벽돌을 반사하는 캐릭터 이미지 설정 
geo_image = pygame.image.load('geo.png')
geo_rect = geo_image.get_rect() 
geo_rect.center = (WINDOW_WIDTH//2, 40)

ball_image = pygame.image.load('ball.png')
ball_rect = ball_image.get_rect()
ball_rect.center = (400, 400)

mushroom_image = pygame.image.load('mushroom.png')
mushroom_rect = mushroom_image.get_rect()
mushroom_rect.center = (WINDOW_WIDTH//2, 850)

# 공이 geo와 부딪힐 시 YOU WIN 텍스트 설정, 공이 아래로 추락할 시 출력할 YOU LOSE 설정 
System_font = pygame.font.SysFont('verdana', 30)

win_lose_text = System_font.render('???', True, (255, 204, 0), None)
win_lose_text_rect = win_lose_text.get_rect()
win_lose_text_rect.center = (WINDOW_WIDTH//2, 400)

# 벽돌 리스트 만들기 
bricks =[] 
# 벽돌 개수 설정
brick_rows = 4
brick_cols = 10 
# 벽돌 사이즈 설정 
brick_width = 100 
brick_height = 30 

# 벽돌 위치 설정 
for row in range(brick_rows) :
    for col in range(brick_cols) :
        # 블록 개수만큼 x 좌표 위치 설정 
        brick_x = 60 + col * (brick_width + 10)
        # 블록 개수만큼 y 좌표 위치 설정 
        brick_y = 80 + row * (brick_height + 10)
        # (x좌표, y좌표, 너비, 높이) 로 pygame.Rect() 를 활용하여 사각형 만들기 
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        # 만든 사각형들을 bricks 리스트에 저장하기 (나열해서 집어넣어야 하기 때문에 for문 안에 씀)
        bricks.append(brick_rect) 


# 화면이 계속 출력될 수 있게 while 반복문에 True 조건 걸기 
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
            
    # key 기능 추가 
    key = pygame.key.get_pressed() # get_pressed() 메서드를 입력해야 키보드에서 어떤 키가 눌렸는지 실시간으로 확인 가능 

    if (key[pygame.K_LEFT] or key[pygame.K_a]) and mushroom_rect.left > 0:     # 위의 코드를 입력하고 어떠한 키를 입력할 때마다 이 코드로 인식을 하여 알맞은 실행을 한다.
       mushroom_rect.x -= 5
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and mushroom_rect.right < WINDOW_WIDTH:    # 이건 외우지 말고 필요할 때마다 붙여쓰자 
       mushroom_rect.x += 5
       
    # 공 자동으로 움직이게 설정 
    ball_rect.x = ball_rect.x + ball_dx 
    ball_rect.y = ball_rect.y + ball_dy
            
    # 이미지가 움직일 경우 겹쳐보이지 않게 fill() 설정
    display_surface.fill((0, 0, 0))
    
    # 공이 바닥을 제외한 벽에 튕기게 설정 
    if ball_rect.x > WINDOW_WIDTH - 30 or ball_rect.x < 0 :
        ball_dx *= -1 
    if ball_rect.y < 0 :
        ball_dy *= -1
        
    # 공이 버섯이랑도 부딪힐 경우 반대 방향으로 튕기게 설정
    if ball_rect.colliderect(mushroom_rect) :
        ball_dy *= -1 
    
    # 공이 geo랑 부딪힐 경우 YOU WIN 출력 
    if ball_rect.colliderect(geo_rect) :
        ball_dx = 0 
        ball_dy = 0
        win_lose_text = System_font.render('YOU WIN!!!', True, (255, 204, 0), None)
        display_surface.blit(win_lose_text, win_lose_text_rect)
        
    # 공이 아래로 추락할 경우 YOU LOSE 출력 
    if ball_rect.y > WINDOW_HEIGHT :
        win_lose_text = System_font.render('YOU LOSE...', True, (255, 204, 0), None)
        display_surface.blit(win_lose_text, win_lose_text_rect)

    # 이미지 출력 (순서 조심)
    display_surface.blit(geo_image, geo_rect)
    display_surface.blit(ball_image, ball_rect)
    display_surface.blit(mushroom_image, mushroom_rect)
    
    # 벽돌 화면에 출력
    for brick in bricks :
        pygame.draw.rect(display_surface, (255, 255, 0), brick)
    
    # 벽돌이 부딪힐 때마다 벽돌 제거 
    hit_index = ball_rect.collidelist(bricks)
    # 부딪히지 않는 경우는 -1이므로 -1이 아닐 경우 참이 되고 
    if hit_index != -1 :
        # 참일 경우 부딪힌 벽돌 제거 
        del bricks[hit_index]
        # 제거 후 반대 방향으로 전환 
        ball_dy *= -1
        
    
    # 화면 업데이트 
    pygame.display.update()
    
    # 초당 프레임 적용
    clock.tick(60) 

# 원활한 종료를 위해 pygame.quit() 설정
pygame.quit() 