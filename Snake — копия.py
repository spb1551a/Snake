import pygame
import sys
import random
pygame.init()

size_block=20
frame_color=(0,255,204)
White=(255,255,255)
Blue=(204,255,255)
red=(224,0,0)
HEADER_color=(0,204,153)
Snake_color=(0,102,0)
count_block=20
Header_margin=70
margin=1
size=[size_block*count_block+2*size_block+margin+count_block,size_block*count_block+2*size_block+margin+count_block+Header_margin]

print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')
timer=pygame.time.Clock()
courier=pygame.font.SysFont('courier', 36)

class SnakeBlock:
    def __int__(self, x,y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0<=self.x<count_block and 0<=self.y<count_block

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y
    def get_randon_empty_block(self):
        x = random.randint(0, count_block-1)
        y = random.randint(0, count_block - 1)
        empty_block=SnakeBlock(x,y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, count_block-1)
            empty_block.y = random.randint(0, count_block - 1)
        return empty_block
    def draw_block(color,row,column):
        pygame.draw.rect(screen,color,[size_block + column * size_block+margin*(column+1),
                                       Header_margin+size_block+row*size_block+margin*(row+1),
                                       size_block,
                                       size_block])
    def start_the_game():
        snake_block = [SnakeBlock(9,8),SnakeBlock(9,9), SnakeBlock(9,10)]
        apple= get_randon_empty_block()
        d_row=buf_row=0