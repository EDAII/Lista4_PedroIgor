import pygame
from pygame.locals import *
from math import ceil
from src import numbers_gen
import copy
from src import sort_algs
from src import machine_game
import time
def start():
    pygame.init()

    screen_size = (1070, 650)
    start_music = pygame.mixer.Sound("snd/start.wav")
    #start_music.play(-1)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Sort the cards')

    w = 10
    card_pos = []
    # criando posições das cartas a serem ordenadas
    while w < 1060:
        card_pos.append((w, 50))
        w += 70
    print(len(card_pos))

    myfont = pygame.font.SysFont('bold', 48)
    title_texts = []
    title_texts.append(myfont.render("Vetor Original: ", False, (255,255,255)))
    title_texts.append(myfont.render("Max Heap: ", False, (255, 255, 255)))


    # criando superfície das cartas
    card_skin = pygame.Surface((60, 90))
    card_skin.fill((150, 65, 200))
    card_skin_first = pygame.Surface((60, 90))
    card_skin_first.fill((0,0,255))
    card_skin_second = pygame.Surface((60, 90))
    card_skin_second.fill((0,255,0))
    # criando fonte dos números das cartas

    first = []
    second = []
    dict = {}
    numbers = numbers_gen.numbers_gen()
    copy_numbers = copy.copy(numbers)
    sorted_numbers, heaps, sorts = sort_algs.heap_sort(copy_numbers)
    i = 0
    i_sort = 0
    while i < len(numbers):
        dict[card_pos[i]] = numbers[i]
        i+=1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        screen.fill((0, 0, 0))
        screen.blit(title_texts[0], (10, 10))
        screen.blit(title_texts[1], (10, 150))
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

        heap_parent = []
        heap_children = []
        heap_g_children = []
        heap_g_g_children = []
        if i_sort < len(heaps):
            print('heap')
            print(heaps[i_sort])
            heap_parent = heaps[i_sort][0]
            print('parent')
            print(heap_parent)
            screen.blit(card_skin, (500,180))
            number_surface = myfont.render(str(heap_parent), False, (255, 255, 255))
            screen.blit(number_surface, (502, 210))

            if len(heaps[i_sort]) > 1:
                if len(heaps[i_sort]) >= 3:
                    heap_children = heaps[i_sort][1:3]
                    screen.blit(card_skin, (780, 300))
                    number_surface = myfont.render(str(heap_children[1]), False, (255, 255, 255))
                    screen.blit(number_surface, (782, 330))
                else:
                    heap_children = heaps[i_sort][1]
                    if type(heap_children)!=list:
                        heap_children = [heap_children]

                print('children')
                print(heap_children)
                screen.blit(card_skin, (220, 300))
                number_surface = myfont.render(str(heap_children[0]), False, (255, 255, 255))
                screen.blit(number_surface, (222, 330))

            if len(heaps[i_sort]) > 3:
                if len(heaps[i_sort]) >= 7:
                    heap_g_children = heaps[i_sort][3:7]
                else:
                    heap_g_children = heaps[i_sort][3:len(heaps[i_sort])]
                print('g_children')
                print(heap_g_children)
                pos_x = 80
                h = 0
                for h in heap_g_children:
                    screen.blit(card_skin, (pos_x, 400))
                    number_surface = myfont.render(str(h), False, (255, 255, 255))
                    screen.blit(number_surface, (pos_x+2, 430))
                    pos_x+=280


            if len(heaps[i_sort]) > 7:
                heap_g_g_children = heaps[i_sort][7:len(heaps[i_sort])]
                print('g_g_children')
                print(heap_g_g_children)
                pos_x = 10
                for h in heap_g_g_children:
                    screen.blit(card_skin, (pos_x, 500))
                    number_surface = myfont.render(str(h), False, (255, 255, 255))
                    screen.blit(number_surface, (pos_x + 2, 530))
                    pos_x += 140
        i_sort+=1




        pygame.display.update()
        time.sleep(3)