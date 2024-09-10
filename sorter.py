import random
import pygame as pg
from time import sleep
import sys

class Sorter:
    arr = []
    size = 0

    def handleInputs(self):
        for key in pg.event.get():
            if key.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def swap(self, x, y, screen):
        self.arr[x], self.arr[y] = self.arr[y], self.arr[x]
        self.lastSwapped = [x,y]
        self.draw(screen, [x, y])

    def cmp(self, x, y, screen):
        self.draw(screen, [x, y])
        return self.arr[x] < self.arr[y]


    def swapRandom(self):
        x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
        self.arr[x], self.arr[y] = self.arr[y], self.arr[x]

    def shuffle(self):
        for i in range(3*self.size):
            self.swapRandom()

    def draw(self, screen, highlight):
        scr_width, scr_height = pg.display.get_surface().get_size()
        if(scr_height < 100): scr_height = 100
        if(scr_width < 100): scr_width = 100
        screen.fill((0, 0, 0))
        for i in range(len(self.arr)):
            color = (0, 255, 0)
            if i in highlight:
                color = (255, 255, 255)
            
            pg.draw.rect(
                screen, 
                color, 
                pg.Rect(
                    50 +i*(scr_width-100)//self.size,
                    scr_height-50 - ((scr_height-100)/self.size)*self.arr[i], 
                    (scr_width-100)/self.size - 1, 
                    ((scr_height-100)/self.size)*self.arr[i]
                )
            )

        pg.display.flip()

        sleep(0.01)
        self.handleInputs()
        self.lastSwapped = []


    def bubbleSort(self, screen):
        for i in range(self.size):
            for j in range(self.size - i - 1):
                if self.cmp(j+1, j, screen):
                    self.swap(j, j+1, screen)


    def quickSortHelper(self, screen, minIdx, size):
        if size <= 0:
            return
        minPtr, maxPtr = minIdx, minIdx + size - 1
        while True:
            while minPtr < maxPtr and not self.cmp(minIdx, minPtr, screen):
                minPtr += 1
            while minPtr < maxPtr and not self.cmp(maxPtr, minIdx, screen):
                maxPtr -= 1

            self.swap(minPtr, maxPtr, screen)

            if minPtr >= maxPtr:
                if self.cmp(minIdx, minPtr, screen):
                    minPtr -= 1
                else:
                    maxPtr += 1
                self.swap(minIdx, minPtr, screen)
                self.quickSortHelper(screen, minIdx, minPtr-minIdx)
                self.quickSortHelper(screen, maxPtr, size - maxPtr + minIdx)
                return

    def quickSort(self, screen):
        self.quickSortHelper(screen, 0, self.size)

    def __init__(self, size):
        self.size = size
        self.arr = [i+1 for i in range(size)]
        self.shuffle()

    