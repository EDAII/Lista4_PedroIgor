import pygame
from pygame.locals import *
from src import numbers_gen
import copy
from src import sort_algs
from src import first_screen

import time
def start():
    pygame.init()

    screen_size = (1070, 650)
    start_music = pygame.mixer.Sound("snd/start.wav")
    start_music.play(-1)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Heap Sort')

    w = 10
    card_pos = []
    # criando posições das cartas a serem ordenadas
    while w < 1060:
        card_pos.append((w, 50))
        w += 70

    myfont = pygame.font.SysFont('bold', 48)
    title_texts = []
    title_texts.append(myfont.render("Vetor Original: ", False, (255,255,255)))
    title_texts.append(myfont.render("Max Heap: ", False, (255, 255, 255)))
    title_texts.append(myfont.render("Vetor Ordenado: ", False, (255, 255, 255)))


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
    sorted_numbers = []
    heaps = []
    sorts = []
    sorted_numbers, heaps, sorts = sort_algs.heap_sort(copy_numbers, sorted_numbers, heaps,sorts)
    sorts+=[sorted_numbers]
    sorts = []+sorts
    heaps=heaps+[[]]

    start_font = pygame.font.SysFont('bold', 22)
    start_button_skin = pygame.Surface((50, 35))
    start_button_skin.fill((255, 255, 255))
    start_text_surface = start_font.render("NEXT", False, (0, 0, 255))

    i = 0
    i_sort = 0
    while i < len(numbers):
        dict[card_pos[i]] = numbers[i]
        i+=1
    next = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if mouse_position[0] >= 1000 and mouse_position[0] >= 10:
                    if mouse_position[1] <= 1050 and mouse_position[1] <= 45:
                        next = True

        screen.fill((0, 0, 0))
        screen.blit(title_texts[0], (10, 10))
        screen.blit(title_texts[1], (10, 150))
        screen.blit(title_texts[2], (10, 523))
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

        if i_sort < len(heaps):
            if heaps[i_sort] != []:
                heap_parent = heaps[i_sort][0]
                screen.blit(card_skin_second, (500,150))
                number_surface = myfont.render(str(heap_parent), False, (255, 255, 255))
                screen.blit(number_surface, (502, 180))

            if len(heaps[i_sort]) > 1:
                if len(heaps[i_sort]) >= 3:
                    heap_children = heaps[i_sort][1:3]
                    show = card_skin
                    if len(heaps[i_sort]) == 3:
                        show = card_skin_first
                    screen.blit(show, (780, 240))
                    number_surface = myfont.render(str(heap_children[1]), False, (255, 255, 255))
                    screen.blit(number_surface, (782, 270))
                else:
                    heap_children = heaps[i_sort][1]
                    if type(heap_children)!=list:
                        heap_children = [heap_children]
                show = card_skin
                if len(heaps[i_sort]) == 2:
                    show = card_skin_first
                screen.blit(show, (220, 240))
                number_surface = myfont.render(str(heap_children[0]), False, (255, 255, 255))
                screen.blit(number_surface, (222, 270))

            if len(heaps[i_sort]) > 3:
                if len(heaps[i_sort]) >= 7:
                    heap_g_children = heaps[i_sort][3:7]
                else:
                    heap_g_children = heaps[i_sort][3:len(heaps[i_sort])]
                pos_x = 80
                h = 0
                for h in heap_g_children:
                    show = card_skin
                    if h == heap_g_children[len(heap_g_children) - 1] and len(heaps[i_sort]) <= 7:
                        show = card_skin_first
                    screen.blit(show, (pos_x, 335))
                    number_surface = myfont.render(str(h), False, (255, 255, 255))
                    screen.blit(number_surface, (pos_x+2, 365))
                    pos_x+=280


            if len(heaps[i_sort]) > 7:
                heap_g_g_children = heaps[i_sort][7:len(heaps[i_sort])]
                pos_x = 10
                for h in heap_g_g_children:
                    show = card_skin
                    if h == heap_g_g_children[len(heap_g_g_children) - 1]:
                        show = card_skin_first
                    screen.blit(show, (pos_x, 430))
                    number_surface = myfont.render(str(h), False, (255, 255, 255))
                    screen.blit(number_surface, (pos_x + 2, 460))
                    pos_x += 140
            pos_x = 10
            if i_sort > 0:
                for s in sorts[i_sort-1]:
                    screen.blit(card_skin, (pos_x, 560))
                    number_surface = myfont.render(str(s), False, (255, 255, 255))
                    screen.blit(number_surface, (pos_x + 2, 590))
                    pos_x+=70
            if next:
                i_sort+=1
                next = False

        screen.blit(start_button_skin, (1000, 10))
        screen.blit(start_text_surface, (1005, 20))
        pygame.display.update()
        if i_sort == len(heaps):
            start_music.stop()
            first_screen.begin()