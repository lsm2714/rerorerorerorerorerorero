# 파이게임 모듈 불러오기 
import pygame
# 랜덤 모듈 불러오기 
import random

# 원활한 실행을 위한 초기화 
pygame.init()

# 화면 크기 설정 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 화면 크기 적용, 이름 추가
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('새와 몬스터의 충돌 (스코어가 구현된)')

# 새와 몬스터 이미지 집어넣기 
bird_image = pygame.image.load('birdie-icon.png')
bird_image_rect = bird_image.get_rect()
bird_image_rect.center = (WINDOW_WIDTH//2, 300)

monster_image = pygame.image.load('comix-icon.png')
monster_image_rect = monster_image.get_rect()
monster_image_rect.center = (WINDOW_WIDTH/4, 50)

# 초당 프레임 설정
clock = pygame.time.Clock()

# 리브 스코어 설정 
score_live = 5

# FIGHT!!! 텍스트와 충돌 시 나타날 Collision!!! 텍스트 설정 
system_font = pygame.font.SysFont('verdana', 30) # 이거는 다 따로따로 할 필요 없이 그냥 하나만 선언해 두고 써먹으면 된다.

game_fight_font = system_font.render('KILL MONSTER!!!!', True, (0, 0, 255), (234, 31, 31))
game_fight_font_rect = game_fight_font.get_rect()
game_fight_font_rect.center = (WINDOW_WIDTH//2, 130)

game_collision_font = system_font.render('Collision!!!!!', True, (255, 115, 0), None)
game_collision_font_rect = game_collision_font.get_rect()
game_collision_font_rect.center = (WINDOW_WIDTH//2, 360)

# 스코어 텍스트 객체 만들기 
game_live_font = system_font.render('lives : ' + str(score_live), True, (234, 23, 190), (255, 255, 255))
game_live_font_rect = game_live_font.get_rect()
game_live_font_rect.topleft = (10, 10)

# 화면의 유지를 위해 while 반복문에 True 조건 달기 
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False 
    
    # key 기능 추가 
    key = pygame.key.get_pressed() # get_pressed() 메서드를 입력해야 키보드에서 어떤 키가 눌렸는지 실시간으로 확인 가능 

    if (key[pygame.K_LEFT] or key[pygame.K_a]) and bird_image_rect.left > 0:     # 위의 코드를 입력하고 어떠한 키를 입력할 때마다 이 코드로 인식을 하여 알맞은 실행을 한다.
       bird_image_rect.x -= 5
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and bird_image_rect.right < WINDOW_WIDTH:    # 이건 외우지 말고 필요할 때마다 붙여쓰자 
       bird_image_rect.x += 5
    if (key[pygame.K_UP] or key[pygame.K_w]) and bird_image_rect.top > 0:
       bird_image_rect.y -= 5
    if (key[pygame.K_DOWN] or key[pygame.K_s]) and bird_image_rect.bottom < WINDOW_HEIGHT:
       bird_image_rect.y += 5
       
    # 만약 새와 충돌할 경우 Collision!!! 출력 설정 - 1
    show_collision = False
    
    if bird_image_rect.colliderect(monster_image_rect) :
        show_collision = True
    else :
        show_collision = False
        
    # 만약 새와 충돌할 경우 Collision!!! 출력 설정 - 2
    if show_collision :
        display_surface.blit(game_collision_font, game_collision_font_rect)
        # 충돌할 때마다 리브 스코어 깎이게 하기 
        score_live -= 1 
        monster_image_rect.x = random.randint(0, WINDOW_WIDTH - 50) 
        # randint()는 입력한 숫자 사이의 랜덤한 값을 지정하는 기능
        monster_image_rect.y = random.randint(0, WINDOW_HEIGHT - 50)
    # 점수판 표시 
    if score_live > 0 :
        game_live_font = system_font.render('lives : ' + str(score_live), True, (234, 23, 190), (255, 255, 255))
    else :
        game_live_font = system_font.render('DIED...', True, (234, 23, 190), (255, 255, 255))
        
    # 이미지, 텍스트 화면에 출력
    display_surface.fill((0, 0, 0)) # 이미지가 움직일 때마다 검은색으로 칠하여 겹쳐 보이지 않게 하기 
    display_surface.blit(bird_image, bird_image_rect)
    if score_live > 0 :
        display_surface.blit(monster_image, monster_image_rect)
    else :
        game_fight_font = system_font.render('YES!!! YES!!! YES!!!', True, (0, 0, 255), (234, 31, 31))
    display_surface.blit(game_fight_font, game_fight_font_rect)
        
    # 스코어 텍스트 출력 
    display_surface.blit(game_live_font, game_live_font_rect)
    
    pygame.display.update() 
    
    # 초당 프레임 적용
    clock.tick(60)
            
# 원활한 종료를 위해 pygame.quit() 선언
pygame.quit()