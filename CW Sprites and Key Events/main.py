
import pygame

pygame.init()

screen = pygame.display.set_mode((700,600))
pygame.display.set_caption("Sprites and Key Events")

WIDTH = 700
HEIGHT = 600

class Squishmallow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # - CALLING the init function that is in the SPRITE class
        self.image = pygame.image.load("squishmallow.png")
        self.rect = self.image.get_rect()
    def update(self, keysPressed):
        if keysPressed[pygame.K_UP]:
            self.rect.move_ip((0,-5))
        if keysPressed[pygame.K_DOWN]:
            self.rect.move_ip((0,5))
        if keysPressed[pygame.K_LEFT]:
            self.rect.move_ip((-5,0))
        if keysPressed[pygame.K_RIGHT]:
            self.rect.move_ip((5,0))
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# - creating a group for all sprites

spriteGroup = pygame.sprite.Group()

def controlGame():
    squishmallow = Squishmallow()
    spriteGroup.add(squishmallow)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        keysPressed = pygame.key.get_pressed()
        squishmallow.update(keysPressed)
        screen.blit(pygame.image.load("bg.jpg"), (0,0))
        screen.fill("light blue")
        spriteGroup.draw(screen)

        pygame.display.update()

controlGame()