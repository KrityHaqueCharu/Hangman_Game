import pygame
import os 
import math
import random

#Setup Display 
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Welcome to Hangman Game!")

#fonts
FONTSS= pygame.font.SysFont('comicsans',40)
FONTSS1 = pygame.font.SysFont('comicsans',60)


#Load Images
imgs = []
for i in range(7):
    img =pygame.image.load("hangman"+ str(i)+ ".png")
    imgs.append(img)

#Button var
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) *13)/2)
starty=400
A=65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13 ) * (GAP + RADIUS * 2))
    letters.append([x,y,chr(A+i), True])

def draw():
    win.fill(OFF_WHITE)
    #draw title()
    text = FONTSS.render("GUESS A COUNTRY",1,BLACK)
    win.blit(text,(WIDTH/2-text.get_width()/2,20))


    #draw word
    display_word=""
    for letter in word:
        if letter in guess:
            display_word += letter + " "
        else:
            display_word +="_ "
    text= FONTSS1.render(display_word,1,BLACK)
    win.blit(text,(400,200))
    
    #draw buttons
    for letter in letters:
        x,y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK , (x,y), RADIUS, 3)
            text = FONTSS.render(ltr,1,BLACK)
            win.blit(text,(x - text.get_width()/2,y-text.get_width()/2))

    
    win.blit(imgs[hangman_status],(150,100))
    pygame.display.update()
    

#game variable
hangman_status = 0
words=["INDIA", "BANGLADESH", "PORTUGAL", "BHUTAN", "PAKISTAN","AUSTRALIA","ARGENTINA","BRAZIL","RUSSIA","UKRAIN","IRAN","IRAQ","EGYPT","SPAIN","GERMANY","ENGLANG","IRELAND","FINLAND","NORWAY","NEPAL","SERIA","ITALY","COLOMBIA","NIGERIA","MEXICO","CANADA","ESTONIA","LYBIA","SRILANKA","MALAYSIA","NORWAY","AUSTRIA","AFGANISTHAN","BELGIUM","NETHELAND","CHINA","JAPAN","KOREA","CROATIA","DENMARK","POLAND","SERBIA","FRANCE","GREECE","HAITI","GEORGIA","KENYA","PERU","YEMEN","ZAMBIA","MONACO"]
word= random.choice(words)
guess=[]

#colors
OFF_WHITE = (255,255,220)
BLACK= (0,0,0)

#Game Loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    #so that while loop run at the FPS's speed
    clock.tick(FPS)

    draw()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y= pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible =letter
                if visible:
                    dis = math.sqrt((x-m_x)**2+ (y-m_y)**2)
                    if dis < RADIUS:
                        letter[3]= False
                        guess.append(ltr)
                        if ltr not in word:
                            hangman_status +=1
    draw()                        
    won= True
    for letter in word:
        if letter not in guess:
            won = False
            break 
    if won:
        pygame.time.delay(1500)
        win.fill(OFF_WHITE)
        text= FONTSS1.render("YOU WON!", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2-text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break

    if hangman_status==6:
        text = FONTSS.render(word,1,BLACK)
        win.blit(text,(WIDTH/2-text.get_width()/2,70))
        pygame.display.update()
        pygame.time.delay(2000)
        win.fill(OFF_WHITE)
        text= FONTSS1.render("YOU LOST!", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2-text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break
                

pygame.quit()
        