'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Katie Chiu
Final
Version .1
Last updated 28 May 2019
'''
import pygame, sys
global posx,posy,count,window_height,window_width
pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((640, 480))
surface = pygame.Surface((50,50))
change=5
begin=0
posx=200
posy=200
count=0
window_height=480
window_width=640

DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
direction=DOWNLEFT
MOVESPEED = 4

BLUE=(61,89,171)
WHITE = (255, 255, 255) #colors
GREEN=(69,139,0)
RED=(220,20,60)
BLACK=(0,0,0)
GREY=(128,138,135)
YELLOW=(255,215,0)
color=BLUE
colorcircle=GREEN

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class Paddle(Entity):
    def __init__(self, x, y, width, height):
        super(Paddle, self).__init__(x, y, width, height)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)

class Corner(Entity):
    def __init__(self, x, y, width, height):
        super(Corner, self).__init__(x, y, width, height)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)


def circlemove():
    global posx,posy,count
    if count==10:
        posx+=-1
        posy+=1
        count=0
    if posx>=0:
        posx+=-1
    if posx<=640:
        posx+=1
    if posy<=430:
        posy+=1
    if posy>=70:
        posy+=-1

all_sprites_list = pygame.sprite.Group()
paddle = Paddle(320, 20, 200, 4)
rect=Corner(540,380,100,100)
all_sprites_list.add(paddle)
all_sprites_list.add(rect)

font = pygame.font.SysFont('arial', 18) #fonts
titlefont = pygame.font.SysFont('arial', 30)
text = font.render(str("CHANGE"), True, WHITE, BLACK)  # shows score
textbox = text.get_rect()
textbox.center = (600, 40)

while True: #keeps pygame running
    mouseClicked=False
    if begin == 0: #menu
        screen.fill(BLACK)
        title = titlefont.render(str("CLICK TO START"), True, WHITE) #display for menu
        titlerect = title.get_rect()
        titlerect.center = (320, 150)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]: #if spacebar pressed, starts game
            begin = 1
        if key[pygame.K_h]:
            begin=5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #if enter pressed, goes to instructions
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:  # assigns where the user clicked
                mousex, mousey = event.pos
                mouseClicked = True
        screen.blit(title, titlerect)
        if mouseClicked:
            begin=2
    if begin==2:
        count = count + 1
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #if program closes
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #if enter pressed, goes to instructions
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:  # assigns where the user clicked
                mousex, mousey = event.pos
                mouseClicked = True
        if mouseClicked:
            if color==BLUE:
                color=YELLOW
            if color==YELLOW:
                color=BLACK
            if color==BLACK:
                color=GREY
            if color==GREY:
                color=BLUE
        screen.fill(color)
        surface.fill(color)
        circle = pygame.draw.circle(surface, colorcircle, (25, 25), 25)
        circlemove()

        paddle.rect.x+=change
        if paddle.rect.x<=0:
            change=5
        elif paddle.rect.x+200>=640:
            change=-5
        screen.blit(surface,(posx,posy))

        for ent in all_sprites_list:
            ent.update()
        all_sprites_list.draw(screen)
        screen.blit(text, textbox)

    pygame.display.update()
