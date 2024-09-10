import pygame as pg
import random, sys
from sorter import Sorter


SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000

def main():
    pg.init()
    random.seed(1234)

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.RESIZABLE)
    #pg.display.set_caption('ABC')

    clock = pg.time.Clock()
    timeElapsed = 0

    font = pg.font.Font('freesansbold.ttf', 16)

    cntr = 0
    text = font.render("0 fps", True, (255, 255, 255))
    textRect = text.get_rect()


    pg.mouse.set_visible(False)

    s = Sorter(100)
        

    while True:
        for key in pg.event.get():
            if key.type == pg.QUIT:
                pg.quit()
                sys.exit()
        

        s.shuffle()
        s.heapSort(screen)
        s.shuffle()
        s.quickSort(screen)
        s.shuffle()
        s.bubbleSort(screen)






main()