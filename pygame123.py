# pygame 모듈 불러오기 
import pygame 

# 원활한 실행을 위해 pygame.init() 초기화 
pygame.init() 

# 화면 크기 설정 
WINDOW_WIDTH = 1200 
WINDOW_HEIGHT = 1000 

# 음악 모듈 초기화 
pygame.mixer.init()

# 음악 로드 
pygame.mixer.music.load('yume.mp3')
# 볼륨 설정 
pygame.mixer.music.set_volume(0.3)
# 음악 재생 
pygame.mixer.music.play(loops=-1)

# 효과음 팟 설정 
paxtu_effect = pygame.mixer.Sound('paxtu.mp3')
paxtu_effect.set_volume(0.3)

# 초당 프레임 설정 
clock = pygame.time.Clock()

# 공이 움직이는 방향, 속도 설정 
ball_dx = 5
ball_dy = 5

# geo, mushroom 이미지, ball 이미지 설정
geo_image = pygame.image.load('geo.png')
geo_rect = geo_image.get_rect() 
geo_rect.center = (WINDOW_WIDTH//2, 40) 

mushroom_image = pygame.image.load('mushroom.png')
mushroom_rect = mushroom_image.get_rect() 
mushroom_rect.center = (WINDOW_WIDTH//2, 850)

ball_image = pygame.image.load('ball.png')
ball_rect = ball_image.get_rect()
ball_rect.topleft = (300, 500)

# 텍스트 설정 
system_font = pygame.font.SysFont('verdana', 40)

win_lose_text = system_font.render('???', True, (255, 204, 0), None)
win_lose_text_rect = win_lose_text.get_rect()
win_lose_text_rect.center = (WINDOW_WIDTH//2, 400)

# 화면 크기 적용, 이름 설정 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption('네모 처리하기')

# 벽돌 개수 설정 
bricks = [] # 빈 벽돌 리스트 만들어서 나중에 모을 수 있게 함 
brick_rows = 4
brick_cols = 10 
# 벽돌 크기 설정
brick_width = 100 
brick_height = 30 

# for문을 활용하여 벽돌 위치 설정 
for row in range(brick_rows) :
    for col in range(brick_cols) :
        brick_x = 60 + col * (brick_width + 10) 
        brick_y = 80 + row * (brick_height + 10) 
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height) 
        bricks.append(brick_rect)

# 화면이 계속 출력될 수 있도록 while 반복문에 True 조건 설정하기 
running = True 
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 
            
    # 버섯 양옆으로 움직이게 하기
    # key 기능 추가 
    key = pygame.key.get_pressed() # get_pressed() 메서드를 입력해야 키보드에서 어떤 키가 눌렸는지 실시간으로 확인 가능 

    if (key[pygame.K_LEFT] or key[pygame.K_a]) and mushroom_rect.left > 0:     # 위의 코드를 입력하고 어떠한 키를 입력할 때마다 이 코드로 인식을 하여 알맞은 실행을 한다.
       mushroom_rect.x -= 7
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and mushroom_rect.right < WINDOW_WIDTH:    # 이건 외우지 말고 필요할 때마다 붙여쓰자 
       mushroom_rect.x += 7
            
    # 공 움직이기 
    ball_rect.x = ball_rect.x + ball_dx 
    ball_rect.y = ball_rect.y + ball_dy
    
    # 공이 바닥을 제외한 벽에 튕기게 하기 
    if ball_rect.x > WINDOW_WIDTH - 30 or ball_rect.x < 0 :
        ball_dx *= -1 
    if ball_rect.y < 0 :
        ball_dy *= -1 
        
    # 만약 버섯과 공이 부딪힐 경우 공이 반대로 튕기게 설정 
    if mushroom_rect.colliderect(ball_rect) :
        ball_dy *= -1 
        # 효과음 팟 실행 
        paxtu_effect.play()
            
    # 화면 검은색으로 덮어서 이미지 이동시 겹쳐 보이지 않게 하기 
    display_surface.fill((0, 0, 0))
    
    # 만약 공이 geo와 부딪힐 경우 공이 멈추고 YOU WIN!!! 출력 
    if ball_rect.colliderect(geo_rect) :
        ball_dy = 0
        ball_dx = 0
        win_lose_text = system_font.render('YOU WIN!!!', True, (255, 204, 0), None) 
        display_surface.blit(win_lose_text, win_lose_text_rect) 
    
    # 공이 아래로 떨어져 없어질 경우 YOU LOSE... 출력 
    if ball_rect.y > WINDOW_HEIGHT :
        win_lose_text = system_font.render('YOU LOSE...', True, (255, 204, 0), None) 
        display_surface.blit(win_lose_text, win_lose_text_rect) 
        
    # 벽돌 그리기 
    for brick in bricks :
        pygame.draw.rect(display_surface, (255, 255, 0), brick) 
    
    # 벽돌이 공이랑 부딪힐 경우 사라지게 설정 
    hit_index = ball_rect.collidelist(bricks) 
    # 벽돌이 부딪히지 않을 때는 -1이 되므로 -1이 아닐 경우 삭제 설정
    if hit_index != -1 :
        del bricks[hit_index] 
        # 부딪히고 난 후 공을 반대로 튕기기 
        ball_dy *= -1 
        # 효과음 팟팟 적용 
        paxtu_effect.play() 
        
    # LOSE가 출력될 경우 배경음 끄고 LOSE 브금 재생 
    if ball_rect.y > WINDOW_HEIGHT :
        pygame.mixer.music.stop() 
        pygame.mixer.music.load('hinaget.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()
        
    # 이미지 출력 
    display_surface.blit(geo_image, geo_rect)
    display_surface.blit(mushroom_image, mushroom_rect)
    display_surface.blit(ball_image, ball_rect)
    
    # 화면 업데이트로 출력이 유지되게 하기 
    pygame.display.update() 
    
    # 초당 프레임 적용 
    clock.tick(60)
            
# 원활한 종료를 위해 quit() 설정
pygame.quit() 