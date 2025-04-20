import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600, 550))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
snake = [405, 305, 205]
apple = 805
direction = 4
score = 0

font = pygame.font.Font(None, 50)
text_rect = pygame.Rect(50, 10, 0, 0)

def snake_move():
    global snake, direction
    for i in range(1, len(snake)):
        snake[len(snake) - i] = snake[len(snake) - i - 1]
    if direction == 1:
        snake[0] -= 1
    elif direction == 2:
        snake[0] -= 100
    elif direction == 3:
        snake[0] += 1
    elif direction == 4:
        snake[0] += 100

def apple_eat():
    global snake, apple, score
    if snake[0] == apple:
        snake.append(snake[len(snake) - 1])
        score += 1
        while True:
            apple = 100 * random.randint(1, 10) + random.randint(1, 9)
            if apple in snake:
                continue
            break
        return True
    return False

def check_win():
    if score == 87:
        print("Win!")
        return True
    return False

def check_lose():
    if snake[0] in snake[1:] or snake[0] // 100 < 1 or snake[0] // 100 > 10 or snake[0] % 100 < 1 or snake[0] % 100 > 9:
        print("Lose.")
        return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != 3 and direction != 1:
                direction = 1
                break
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != 4 and direction != 2:
                direction = 2
                break
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != 1 and direction != 3:
                direction = 3
                break
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != 2 and direction != 4:
                direction = 4
                break
            else:
                continue
    if check_win():
        break
    if check_lose():
        break
    apple_eat()
    snake_move()

    screen.fill((0, 0, 0))

    for i in range(1, 12):
        pygame.draw.rect(screen, (128, 128, 128), (50 * i - 1, 50, 2, 450))
    for i in range(1, 11):
        pygame.draw.rect(screen, (128, 128, 128), (50, 50 * i - 1, 500, 2))

    pygame.draw.circle(screen, (255, 0, 0), (25 + 50 * (apple // 100), 25 + 50 * (apple % 100)), 24)
    for i in range(0, len(snake)):
        pygame.draw.rect(screen, (0, 255, 0), (1 + 50 * (snake[i] // 100), 1 + 50 * (snake[i] % 100), 48, 48))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 600, 49))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 49, 550))
    pygame.draw.rect(screen, (0, 0, 0), (0, 501, 600, 49))
    pygame.draw.rect(screen, (0, 0, 0), (551, 0, 49, 550))

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(5)
pygame.quit()
