import pygame
import random

length = 640
width = 512


def grid(screen, color):
    for i in range(1, 20):
        pygame.draw.line(screen, color, (i*32,0), (i*32,width))
    for i in range(1, 16):
        pygame.draw.line(screen, color, (0,i*32), (length,i*32))

def change(screen, mole):
    x = random.randrange(0, 20)
    y = random.randrange(0, 16)
    mole_rect = mole.get_rect(topleft=(x * 32, y * 32))
    screen.fill("light green")
    grid(screen, "black")
    screen.blit(mole, mole_rect)
    pygame.display.update()
    return mole_rect[:2]

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        rect_mole = mole_image.get_rect()
        mole_rect = [0,0]
        screen = pygame.display.set_mode((length, width))
        pygame.display.set_caption("Whack a Mole!")
        clock = pygame.time.Clock()
        running = True
        screen.fill("light green")
        grid(screen, "black")
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if mole_rect[0] <= mx <= (mole_rect[0] + 32) and mole_rect[1] <= my <= (mole_rect[1] + 32):
                        mole_rect = change(screen, mole_image)


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print(change(screen, mole_image))

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
