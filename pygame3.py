# pygame 모듈 꺼내오기 
import pygame 
# random 모듈 꺼내오기 
import random

# 원활한 실행을 위해 init() 추가
pygame.init() 

# 화면 크기 설정 
WINDOW_WIDTH = 800 
WINDOW_HEIGHT = 600 

# 프레임 설정 
clock = pygame.time.Clock()

# 리브 스코어 설정 
live_score = 5

# 화면 설정
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('몬스터 킬러 파란 새')

# 이미지 설정 
bird_image = pygame.image.load('birdie-icon.png') 
bird_rect = bird_image.get_rect()
bird_rect.center = (WINDOW_WIDTH//2, 300)

monster_image = pygame.image.load('comix-icon.png')
monster_rect = monster_image.get_rect() 
monster_rect.topleft = (80, 80)

# 텍스트 설정 
system_font = pygame.font.SysFont('verdana', 30) 

kill_text = system_font.render('KILL MONSTER!!!', True, (0, 25, 220), (255, 0, 0))
kill_text_rect = kill_text.get_rect()
kill_text_rect.center = (WINDOW_WIDTH//2, 200)

live_text = system_font.render('live : ' + str(live_score), True, (0, 157, 255), (255, 230, 222))
live_text_rect = live_text.get_rect()
live_text_rect.topleft = (0, 0)

# 화면이 게속 출력될 수 있게 while 반복문에 True 조건을 걺
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 
    
    # key 기능 추가 
    key = pygame.key.get_pressed() # get_pressed() 메서드를 입력해야 키보드에서 어떤 키가 눌렸는지 실시간으로 확인 가능 

    if (key[pygame.K_LEFT] or key[pygame.K_a]) and bird_rect.left > 0:     # 위의 코드를 입력하고 어떠한 키를 입력할 때마다 이 코드로 인식을 하여 알맞은 실행을 한다.
       bird_rect.x -= 5
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and bird_rect.right < WINDOW_WIDTH:    # 이건 외우지 말고 필요할 때마다 붙여쓰자 
      bird_rect.x += 5
    if (key[pygame.K_UP] or key[pygame.K_w]) and bird_rect.top > 0:
       bird_rect.y -= 5
    if (key[pygame.K_DOWN] or key[pygame.K_s]) and bird_rect.bottom < WINDOW_HEIGHT:
       bird_rect.y += 5
    
    # 이미지나 텍스트가 움직일 경우 겹쳐 보이는 것을 방지하기 위해 fill() 메서드 사용
    display_surface.fill((0, 0, 0))
    
    # 만약 두 그림이 닿을 경우 True 설정 
    show_collision = False
    if bird_rect.colliderect(monster_rect) :
        show_collision = True
        # 닿을 때마다 리브 스코어가 1씩 감소하고 몬스터가 랜덤한 위치로 이동하게 하기
        live_score -= 1
        monster_rect.x = random.randint(50, WINDOW_WIDTH - 50)
        monster_rect.y = random.randint(50, WINDOW_HEIGHT - 50)
    else :
        show_collision = False
    
    live_text = system_font.render('live : ' + str(live_score), True, (0, 157, 255), (255, 230, 222))
    
    display_surface.blit(kill_text, kill_text_rect)
    display_surface.blit(bird_image, bird_rect)
    # 몬스터 이미지를 리브 스코어가 0보다 클 때 출력되게 하기 
    if live_score > 0 :
        display_surface.blit(monster_image, monster_rect)
    else : 
        live_text = system_font.render('WIN!!!!!', True, (0, 157, 255), (255, 230, 222))
        kill_text = system_font.render('YES!!! YES!!! YES!!!', True, (0, 25, 220), (255, 0, 0))
    display_surface.blit(live_text, live_text_rect)
    
    # 화면 업데이트를 통해 이미지나 텍스트 등이 계속 출력될 수 있도록 하기 
    pygame.display.update()
    
    # 프레임 적용
    clock.tick(60)

# 원활한 종료를 위해 pygame.quit() 코드 입력
pygame.quit() 