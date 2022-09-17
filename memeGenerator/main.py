from random import randint
import pygame


def translate(text):
    vowels = {'p': 'b', 't': 'd', 'k': 'g', 'f': 'w', 's': 'z',
              'ś': 'ź', 'sz': 'ż', 'c': 'dz', 'ć': 'dź', 'cz': 'dż'}

    for vow1, vow2 in vowels.items():
        text = text.replace(vow1, vow2)

    return f"{text} :{'D' * randint(1, 6)}"


def display(label_text):
    pygame.init()
    window = pygame.display.set_mode((720, 700))
    spurdo = pygame.image.load("spurdo.jpg")
    save_btn = pygame.image.load("download.png")
    save_hitbox = pygame.Rect(0, 0, *save_btn.get_size())

    label = pygame.font.Font.render(
        pygame.font.SysFont("", 96),
        label_text,
        True,
        (0, 0, 0)
    )
    center = (720 - label.get_width()) // 2

    run = True
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if save_hitbox.collidepoint(*pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed(3)[0]:
                pygame.image.save(window, "meme.png")

        window.fill((255, 255, 255))
        window.blit(spurdo, (0, 0))
        window.blit(save_btn, save_hitbox)
        window.blit(label, (center, 600))
        pygame.display.update()

    pygame.quit()


def main():
    text = input()
    display(translate(text))


main()
