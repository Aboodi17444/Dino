import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Trex spel")

game_font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)

ground = pygame.image.load("assets/ground.png")

ground_rect = ground.get_rect(center=(640, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("white")

    screen.blit(ground, ground_rect)

    pygame.display.update()
    clock.tick(120)