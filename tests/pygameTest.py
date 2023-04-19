import pygame, sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([640,480])
base_font = pygame.font.Font(None, 26)
user_text = ''

input_rect = pygame.Rect(200,200,140,32)
color = pygame.Color('lightskyblue3')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                print(user_text)
                user_text = ''
            elif event.unicode.isprintable():
                user_text += event.unicode

    screen.fill((0,0,0))

    pygame.draw.rect(screen, color, input_rect, 2)

    text_surface = base_font.render(user_text, True, (255,255,255))
    screen.blit(text_surface,(input_rect.x + 5, input_rect.y +5))

    input_rect.w = max(200, text_surface.get_width() + 10)

    pygame.display.flip()
    clock.tick(60)