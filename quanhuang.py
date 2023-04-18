import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义窗口大小和标题
screen_widthscreen_height = 640, 480
pygame.display.set_caption('拳皇游戏')

# 创建游戏窗口
screen = pygame.display.set_mode((screen_width, screen_height))

# 定义角色属性和初始位置
player = {'health': 100, 'attack': 10, 'defense': 5, 'x': 100, 'y': 200}
enemy = {'health': 100, 'attack': 10, 'defense': 5, 'x': 400, 'y': 200}

# 绘制角色的函数
def draw_character(color, x, y):
    pygame.draw.circle(screen, color, (x, y), 20)
    pygame.draw.line(screen, color, (x, y + 20), (x, y + 50), 5)
    pygame.draw.line(screen, color, (x, y + 50), (x - 20, y + 70), 5)
    pygame.draw.line(screen, color, (x, y + 50), (x + 20, y + 70), 5)
    pygame.draw.line(screen, color, (x, y + 20), (x - 20, y + 40), 5)
    pygame.draw.line(screen, color, (x,y + 20), (x + 20, y + 40), 5)

# 玩家攻击的函数
def player_attack():
    damage = player['attack'] - enemy['defense']
    enemy['health'] -= damage
    print('玩家攻击，敌人受到了{}点伤害'.format(damage))

# 敌人攻击的函数
def enemy_attack():
    damage = enemy['attack'] - player['defense']
    player['health'] -= damage
    print('敌人攻击，玩家受到了{}点伤害'.format(damage))

# 显示血量的函数
def draw_health():
    font = pygame.font.Font(None, 30)
    player_health_text = font.render('玩家血量：{}'.format(player['health']), True, (0, 0, 0))
    enemy_health_text = font.render('敌人血量：{}'.format(enemy['health']), True, (0, 0, 0))
    screen.blit(player_health_text, (10, 10))
    screen.blit(enemy_health_text, (screen_width - enemy_health_text.get_width() - 10, 10))

# 判断游戏是否结束的函数
def game_over():
    if player['health'] <= 0:
        print('游戏结束，你输了！')
        return True
    elif enemy['health'] <= 0:
        print('游戏结束，你赢了！')
        return True
    else:
        return False

# 定义游戏循环
running = True
while running:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 处理键盘事件
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player['y'] -= 5
    elif keys[pygame.K_s]:
        player['y'] += 5
    elif keys[pygame.K_a]:
        player['x'] -= 5
    elif keys[pygame.K_d]:
        player['x'] += 5
    elif keys[pygame.K_j]:
        player_attack()

    # 敌人自动攻击
    if random.randint(1, 100) <= 5:
        enemy_attack()

    # 绘制游戏界面
    screen.fill((255, 255, 255))
    draw_character((0, 0, 255), player['x'], player['y'])
    draw_character((255, 0, 0), enemy['x'], enemy['y'])
    draw_health()

    # 判断游戏是否结束
    if game_over():
        running = False

    # 更新游戏窗口
    pygame.display.flip()

# 退出 Pygame
pygame.quit()