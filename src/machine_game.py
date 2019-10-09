import pygame
from pygame.locals import *
import time
from src import result_screen

def start(numbers, machine_steps, machine_swaps, user_swaps):
    pygame.init()
    start_music = pygame.mixer.Sound("snd/start.wav")
    start_music.play(-1)
    screen_size = (710, 512)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Sort the cards')

    w = 10
    card_pos = []
    # criando posições das cartas
    while w < 705:
        card_pos.append((w, 200))
        w += 70
    # criando superfície das cartas
    card_skin = pygame.Surface((60, 90))
    card_skin.fill((150, 65, 200))
    card_skin_first = pygame.Surface((60, 90))
    card_skin_first.fill((0,0,255))
    card_skin_second = pygame.Surface((60, 90))
    card_skin_second.fill((0,255,0))
    # criando fonte dos números das cartas
    myfont = pygame.font.SysFont('bold', 48)
    first = []
    second = []
    dict = {}
    i = 0

    while i < len(numbers):
        dict[card_pos[i]] = numbers[i]
        i+=1
    step = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        screen.fill((0, 0, 0))

        first, second = machine_steps[step]
        step+=1

        i = 0
        while i < len(card_pos):
            show = card_skin
            if i == first:
                show = card_skin_first
            elif i == second:
                show = card_skin_second
            screen.blit(show, card_pos[i])

            i += 1

        for pos in card_pos:
            number_surface = myfont.render(str(dict[pos]), False, (255, 255, 255))
            screen.blit(number_surface, (pos[0] + 2, pos[1] + 30))
        pygame.display.update()
        time.sleep(3)



        if second != [] and first != []:
            pos_a = ()
            pos_b = ()
            a = 0
            b = 0
            for i in dict:
                if a == first:
                    pos_a = i
                elif b == second:
                    pos_b = i
                a+=1
                b+=1
            dict[pos_a], dict[pos_b] = dict[pos_b], dict[pos_a]
            numbers[first], numbers[second] = numbers[second], numbers[first]
        if step == len(machine_steps):
            start_music.stop()
            result_screen.begin(machine_swaps, user_swaps)

