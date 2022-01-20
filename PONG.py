import sys
sys.path.insert(0, 'lib')
from pygame_functions import *
from time import sleep
import pygame, math, random, pickle, time

screenSize(1200, 900)
setAutoUpdate(False)
pygame.display.set_caption('PONG - A game')
gameIcon = pygame.image.load('lib/sprites/atari.png')
pygame.display.set_icon(gameIcon)

winjingle = makeSound("lib/sounds/winsound.wav")
losejingle = makeSound("lib/sounds/losesound.wav")
backsong = makeMusic("lib/sounds/backsongwav.wav")
hit = makeSound("lib/sounds/hit.wav")
point = makeSound("lib/sounds/point.wav")

playMusic(99)

#menuSprites        
vsB = makeSprite("lib/sprites/1v2.png")
addSpriteImage(vsB,"lib/sprites/1v2over.png")
cpuB = makeSprite("lib/sprites/1vCPU.png")
addSpriteImage(cpuB,"lib/sprites/1vCPUover.png")
optionsB = makeSprite("lib/sprites/options.png")
addSpriteImage(optionsB,"lib/sprites/optionsover.png")
creditsB = makeSprite("lib/sprites/credits.png")
addSpriteImage(creditsB,"lib/sprites/creditsover.png")
leave = makeSprite("lib/sprites/leavemessage.png")
production = makeSprite("lib/sprites/production.png")
title = makeSprite("lib/sprites/title.png")
whocares = makeSprite("lib/sprites/whocares.png")

#game
paddleS1 = makeSprite("lib/sprites/paddle.png")
paddleS2 = makeSprite("lib/sprites/paddle.png")
paddleM1 = makeSprite("lib/sprites/paddle2.png")
paddleM2 = makeSprite("lib/sprites/paddle2.png")
paddleL1 = makeSprite("lib/sprites/paddle3.png")
paddleL2 = makeSprite("lib/sprites/paddle3.png")
ball = makeSprite("lib/sprites/ball.png")
net = makeSprite("lib/sprites/net.png")
borderTop = makeSprite("lib/sprites/border1.png")
borderBot = makeSprite("lib/sprites/border1.png")
borderLeft = makeSprite("lib/sprites/border2.png")
borderRight = makeSprite("lib/sprites/border2.png")
y1 = 450
y2 = 450
up = 1
score1 = 0
score2 = 0
scoreP1 = makeLabel(str(score1), 100, 50, 800, 'white', 'Upheaval TT(BRK)', "clear")
scoreP2 = makeLabel(str(score2), 100, 1100, 800, 'white', 'Upheaval TT(BRK)', "clear")
maxscore = 5
levelCPU = 1
paddleSize = 2
P1victory = makeSprite("lib/sprites/P1v.png")
P2victory = makeSprite("lib/sprites/P2v.png")
CPUvictory = makeSprite("lib/sprites/CPUv.png")

#options
prompts = makeSprite("lib/sprites/prompts.png")
maxOption = makeLabel(str(maxscore), 90, 980, 240, 'white', 'Upheaval TT(BRK)', "clear")
ballOption = makeLabel(str(up), 90, 980, 345, 'white', 'Upheaval TT(BRK)', "clear")
levelOption = makeLabel(str(levelCPU), 90, 980, 450, 'white', 'Upheaval TT(BRK)', "clear")
sizeOption = makeLabel(str(paddleSize), 90, 980, 555, 'white', 'Upheaval TT(BRK)', "clear")

r1 = makeSprite("lib/sprites/arrowRight.png")
r2 = makeSprite("lib/sprites/arrowRight.png")
r3 = makeSprite("lib/sprites/arrowRight.png")
r4 = makeSprite("lib/sprites/arrowRight.png")
l1 = makeSprite("lib/sprites/arrowLeft.png")
l2 = makeSprite("lib/sprites/arrowLeft.png")
l3 = makeSprite("lib/sprites/arrowLeft.png")
l4 = makeSprite("lib/sprites/arrowLeft.png")

stripes1 = makeSprite("lib/sprites/stripes.png")
stripes2 = makeSprite("lib/sprites/stripes.png")
done = makeSprite("lib/sprites/donemessage.png")

def checkAngle():

    global angleBall


def win(spr):

    global scoreP1
    global scoreP2
    hideAll()
    hideLabel(scoreP1)
    hideLabel(scoreP2)
    moveSprite(spr, 600, 450, True)
    showSprite(spr)
    if spr == P1victory or spr == P2victory:
        playSound(winjingle)
        print("win")
    elif spr == CPUvictory:
        playSound(losejingle)
        print("lose")
    while True:
        if keyPressed("enter"):
            menu()
            break
        updateDisplay()
        fps = tick(60)
    
def niceLabel():
    if score2 == 1:
        moveLabel(scoreP2, 1125, 800)
    elif score2 == 21 or score2 == 31 or score2 == 41 or score2 == 51 or score2 == 61 or score2 == 71 or score2 == 81 or score2 == 91:
        moveLabel(scoreP2, 1075, 800)
    elif score2 == 10:
        moveLabel(scoreP2, 1075, 800)
    elif score2 >= 12 and score2 < 20:
        moveLabel(scoreP2, 1075, 800)
    elif score2 >= 20:
        moveLabel(scoreP2, 1040, 800)
    else:
        moveLabel(scoreP2, 1100, 800)

def border():
    moveSprite(borderTop, 600, -10, True)
    showSprite(borderTop)
    moveSprite(borderBot, 600, 910, True)
    showSprite(borderBot)
    moveSprite(borderLeft, 50, 450, True)
    moveSprite(borderRight, 1150, 450, True)

def menu():

    global score1
    global score2
    hideAll()
    moveSprite(vsB, 600, 450, True)
    showSprite(vsB)
    moveSprite(cpuB, 600, 550, True)
    showSprite(cpuB)
    moveSprite(optionsB, 600, 650, True)
    showSprite(optionsB)
    moveSprite(creditsB, 600, 750, True)
    showSprite(creditsB)
    moveSprite(leave, 150, 885, True)
    showSprite(leave)
    moveSprite(production, 920, 885, True)
    showSprite(production)
    moveSprite(title, 600, 225, True)
    showSprite(title)
    pygame.mixer.music.set_volume(0.2)

    while True:

        mouse = pygame.mouse.get_pos()

        #mouseOver:
        if 388 < mouse[0] < 812 and 415 < mouse[1] < 485:
            changeSpriteImage(vsB, 1)
        else:
            changeSpriteImage(vsB, 0)
        if 350 < mouse[0] < 850 and 515 < mouse[1] < 585:
            changeSpriteImage(cpuB, 1)
        else:
            changeSpriteImage(cpuB, 0)
        if 363 < mouse[0] < 837 and 615 < mouse[1] < 685:
            changeSpriteImage(optionsB, 1)
        else:
            changeSpriteImage(optionsB, 0)
        if 363 < mouse[0] < 837 and 715 < mouse[1] < 785:
            changeSpriteImage(creditsB, 1)
        else:
            changeSpriteImage(creditsB, 0)

        if spriteClicked(vsB):
            score1 = 0
            score2 = 0
            if paddleSize == 3:
                vs(paddleS1,paddleS2,150,750)
            elif paddleSize == 2:
                vs(paddleM1,paddleM2,100,800)
            elif paddleSize == 1:
                vs(paddleL1,paddleL2,50,850)
            break
        elif spriteClicked(cpuB):
            score1 = 0
            score2 = 0
            if paddleSize == 3:
                CPU(paddleS1,paddleS2,150,750)
            elif paddleSize == 2:
                CPU(paddleM1,paddleM2,100,800)
            elif paddleSize == 1:
                CPU(paddleL1,paddleL2,50,850)
            break
        elif spriteClicked(optionsB):
            options()
            break
        elif spriteClicked(creditsB):
            dacredits()
            break

        if keyPressed("esc"):
            quit

        updateDisplay()
        fps = tick(60)

def options():

    global maxscore
    global up
    global levelCPU
    global paddleSize
    
    hideAll()
    moveSprite(prompts, 400, 450, True)
    showSprite(prompts)
    
    moveSprite(r1, 1125, 290, True)
    showSprite(r1)
    moveSprite(r2, 1125, 395, True)
    showSprite(r2)
    moveSprite(r3, 1125, 500, True)
    showSprite(r3)
    moveSprite(r4, 1125, 605, True)
    showSprite(r4)
    moveSprite(l1, 900, 290, True)
    showSprite(l1)
    moveSprite(l2, 900, 395, True)
    showSprite(l2)
    moveSprite(l3, 900, 500, True)
    showSprite(l3)
    moveSprite(l4, 900, 605, True)
    showSprite(l4)
    
    moveSprite(stripes1, 600, 100, True)
    showSprite(stripes1)
    moveSprite(stripes2, 600, 800, True)
    showSprite(stripes2)
    moveSprite(done, 600, 675, True)
    showSprite(done)
    
    showLabel(maxOption)
    showLabel(ballOption)
    showLabel(levelOption)
    showLabel(sizeOption)
    
    
    while True:
        
        if keyPressed("enter"):
            hideLabel(maxOption)
            hideLabel(ballOption)
            hideLabel(levelOption)
            hideLabel(sizeOption)
            menu()
            break

        if spriteClicked(r1):
            if 1 <= maxscore < 99:
                maxscore += 1
            elif maxscore == 99:
                maxscore = 1
            changeLabel(maxOption, str(maxscore))
        if spriteClicked(r2):
            if 1 <= up < 10:
                up += 1
            elif up == 10:
                up = 1
            changeLabel(ballOption, str(up))
        if spriteClicked(r3):
            if 1 <= levelCPU < 3:
                levelCPU += 1
            elif levelCPU == 3:
                levelCPU = 1
            changeLabel(levelOption, str(levelCPU))
        if spriteClicked(r4):
            if 1 <= paddleSize < 3:
                paddleSize += 1
            elif paddleSize == 3:
                paddleSize = 1
            changeLabel(sizeOption, str(paddleSize))
        if spriteClicked(l1):
            if 1 < maxscore <= 99:
                maxscore -= 1
            elif maxscore == 1:
                maxscore = 99
            changeLabel(maxOption, str(maxscore))
        if spriteClicked(l2):
            if 1 < up <= 10:
                up -= 1
            elif up == 1:
                up = 10
            changeLabel(ballOption, str(up))
        if spriteClicked(l3):
            if 1 < levelCPU <= 3:
                levelCPU -= 1
            elif levelCPU == 1:
                levelCPU = 1
            changeLabel(levelOption, str(levelCPU))
        if spriteClicked(l4):
            if 1 < paddleSize <= 3:
                paddleSize -= 1
            elif paddleSize == 1:
                paddleSize = 3
            changeLabel(sizeOption, str(paddleSize))

        updateDisplay()
        fps = tick(10)

def dacredits():

    hideAll()
    moveSprite(whocares, 600, 450, True)
    showSprite(whocares)

    while True:
        if keyPressed("enter"):
            hideLabel(maxOption)
            hideLabel(ballOption)
            hideLabel(levelOption)
            hideLabel(sizeOption)
            menu()
            break

        updateDisplay()
        fps = tick(60)

def vs(pad1,pad2,top1,top2):

    global up
    global score1
    global score2
    global y2
    global y1
    angles = [50,130,230,310]
    posBx = 600
    posBy = 450
    y1 = 450
    y2 = 450
    angleBall = random.choice(angles)
    speed = 10
    hideAll()
    moveSprite(pad1, 150, 450, True)
    showSprite(pad1)
    moveSprite(pad2, 1050, 450, True)
    showSprite(pad2)
    moveSprite(ball, 600, 450, True)
    showSprite(ball)
    moveSprite(net, 600, 450, True)
    showSprite(net)
    changeLabel(scoreP1, str(score1))
    changeLabel(scoreP2, str(score2))
    border()
    showLabel(scoreP1)
    showLabel(scoreP2)
    niceLabel()
    pygame.mixer.music.set_volume(0.1)
    pause(1000)
    
  
    while True:
            
        #paddleMovement:
        if keyPressed("w"):
            y1 -= 10
        if keyPressed("s"):
            y1 += 10
        if y1 <= top1:
            y1 = top1
        if y1 >= top2:
            y1 = top2
        if keyPressed("up"):
            y2 -= 10
        if keyPressed("down"):
            y2 += 10
        if y2 <= top1:
            y2 = top1
        if y2 >= top2:
            y2 = top2
        moveSprite(pad1, 150, y1, True)
        moveSprite(pad2, 1050, y2, True)

        posBx += math.sin(math.radians(angleBall))*speed
        posBy -= math.cos(math.radians(angleBall))*speed
        moveSprite(ball, posBx, posBy, True)

        #collisions:

        if touching(ball, borderTop):
            angleBall = 180-angleBall
            if angleBall < 0:
                angleBall += 360
            elif angleBall > 360:
                angleBall -= 360
            print(angleBall)
        if touching(ball, borderBot):
            angleBall = 180-angleBall
            if angleBall < 0:
                angleBall += 360
            elif angleBall > 360:
                angleBall -= 360
            print(angleBall)
        if touching(ball, borderLeft):
            score2 += 1
            playSound(point)
            changeLabel(scoreP2, str(score2))
            if paddleSize == 3:
                vs(paddleS1,paddleS2,150,750)
            elif paddleSize == 2:
                vs(paddleM1,paddleM2,100,800)
            elif paddleSize == 1:
                vs(paddleL1,paddleL2,50,850)
            break
        if touching(ball, borderRight):
            score1 +=1
            playSound(point)
            changeLabel(scoreP1, str(score1))
            if paddleSize == 3:
                vs(paddleS1,paddleS2,150,750)
            elif paddleSize == 2:
                vs(paddleM1,paddleM2,100,800)
            elif paddleSize == 1:
                vs(paddleL1,paddleL2,50,850)
            break
        if touching(ball, pad1):
            angleBall = 0-angleBall
            if angleBall < 0:
                angleBall += 360
            elif angleBall > 360:
                angleBall -= 360
            speed += up/2
            print(angleBall)
            playSound(hit)
        if touching(ball, pad2):
            angleBall = 0-angleBall
            if angleBall < 0:
                angleBall += 360
            elif angleBall > 360:
                angleBall -= 360
            speed += up/2
            print(angleBall)
            playSound(hit)

        if maxscore == score1:
            win(P1victory)
            break

        if maxscore == score2:
            win(P2victory)
            break
            
        if keyPressed("r"):
            hideLabel(scoreP1)
            hideLabel(scoreP2)
            menu()
            break

        updateDisplay()
        fps = tick(60)
        
def CPU(pad1,pad2,top1,top2):

    global score1
    global score2
    global y2
    global y1
    angles = [50,130,230,310]
    posBx = 600
    posBy = 450
    y1 = 450
    y2 = 450
    angleBall = random.choice(angles)
    speed = 10
    hideAll()
    moveSprite(pad1, 150, 450, True)
    showSprite(pad1)
    moveSprite(pad2, 1050, 450, True)
    showSprite(pad2)
    changeLabel(scoreP1, str(score1))
    changeLabel(scoreP2, str(score2))
    moveSprite(ball, 600, 450, True)
    showSprite(ball)
    moveSprite(net, 600, 450, True)
    showSprite(net)
    border()
    showLabel(scoreP1)
    showLabel(scoreP2)
    niceLabel()
    pygame.mixer.music.set_volume(0.1)
    pause(1000)
    
    while True:
        
        #paddleMovement:
        if keyPressed("w") or keyPressed("up"):
            y1 -= 10
        if keyPressed("s") or keyPressed("down"):
            y1 += 10
        if y1 <= top1:
            y1 = top1
        if y1 >= top2:
            y1 = top2

        moveSprite(pad1, 150, y1, True)
        
        posBx += math.sin(math.radians(angleBall))*speed
        posBy -= math.cos(math.radians(angleBall))*speed
        moveSprite(ball, posBx, posBy, True)

        #collisions:

        if touching(ball, borderTop):
            angleBall = 180-angleBall
            if angleBall < 0:
                angleBall += 360
            elif angleBall > 360:
                angleBall -= 360
            print(angleBall)
        if touching(ball, borderBot):
            angleBall = 180-angleBall
            if angleBall < 0:
                angleBall += 360
            elif angleBall > 360:
                angleBall -= 360
            print(angleBall)
        if touching(ball, borderLeft):
            score2 +=1
            playSound(point)
            changeLabel(scoreP2, str(score2))
            if paddleSize == 3:
                CPU(paddleS1,paddleS2,150,750)
            elif paddleSize == 2:
                CPU(paddleM1,paddleM2,100,800)
            elif paddleSize == 1:
                CPU(paddleL1,paddleL2,50,850)
            break
        if touching(ball, borderRight):
            score1 +=1
            playSound(point)
            changeLabel(scoreP1, str(score1))
            if paddleSize == 3:
                CPU(paddleS1,paddleS2,150,750)
            elif paddleSize == 2:
                CPU(paddleM1,paddleM2,100,800)
            elif paddleSize == 1:
                CPU(paddleL1,paddleL2,50,850)
            break
        if touching(ball, pad1):
            angleBall = 0-angleBall
            if angleBall < 0:
                angleBall += 360
            elif angleBall > 360:
                angleBall -= 360
            print(angleBall)
            speed += up/2
            playSound(hit)
        if touching(ball, pad2):
            angleBall = 0-angleBall
            if angleBall < 0:
                angleBall += 360
            elif angleBall > 360:
                angleBall -= 360
            print(angleBall)
            speed += up/2
            playSound(hit)
        
        if keyPressed("r"):
            hideLabel(scoreP1)
            hideLabel(scoreP2)
            menu()
            break
        
        if maxscore == score1:
            win(P1victory)
            break

        if maxscore == score2:
            win(CPUvictory)
            menu()
            break
#-----------------------------------------------------------
        if levelCPU == 1:
            if y2 < posBy:
                y2 += 10
            if y2 > posBy:
                y2 -= 10
            if y2 <= top1:
                y2 = top1
            if y2 >= top2:
                y2 = top2

        elif levelCPU == 2:
            if angleBall > 180:
                if y2 < 450:
                    y2 += 10
                elif y2 > 450:
                    y2 -= 10
            elif angleBall < 180:
                if y2 < posBy:
                    y2 += 10
                if y2 > posBy:
                    y2 -= 10
            if y2 <= top1:
                y2 = top1
            if y2 >= top2:
                y2 = top2
                
        elif levelCPU == 3:
            if angleBall > 180:
                if y2 < 450:
                    y2 += 10
                elif y2 > 450:
                    y2 -= 10
            elif angleBall == 50:
                if (y2 - 20) < posBy:
                    y2 += 10
                if (y2 - 20) > posBy:
                    y2 -= 10
            elif angleBall == 130:
                if (y2 + 20) < posBy:
                    y2 += 10
                if (y2 + 20) > posBy:
                    y2 -= 10
            if y2 <= top1:
                y2 = top1
            if y2 >= top2:
                y2 = top2
                    
        moveSprite(pad2, 1050, y2, True)
#-----------------------------------------------------------
        updateDisplay()
        fps = tick(60)
  
menu()
