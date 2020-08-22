import pygame
import time
import random

pygame.init()

#Size of the game area
display_width = 800
display_height = 600

#Colors for use in backgrounds or buttons
black = (0,0,0)
white = (255,255,255)
grey = (160,160,160)
darkgrey = (80,80,80)
red = (200,0,0)
green = (0,200,0)
bred = (255,0,0)
bgreen = (0,255,0)
blue = (0,0,200)

#Size of the main character
pacq_width = 80
orientation = "r"

#Global variable with the score
score = 0

#Map
mapa = [[0,0,0,0,0,0,0,0],[0,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

#Set the size of the game area.
gameDisplay = pygame.display.set_mode((display_width,display_height))

#Caption for the name of the Window.
pygame.display.set_caption('Pac-Q')

#The timer to make the world move
reloj = pygame.time.Clock()

#The different faces of the character
pacq_up = (pygame.image.load('Assets/pacquc.png'),pygame.image.load('Assets/pacqua.png'))
pacq_down = (pygame.image.load('Assets/pacqdc.png'),pygame.image.load('Assets/pacqda.png'))
pacq_left = (pygame.image.load('Assets/pacqlc.png'),pygame.image.load('Assets/pacqla.png'))
pacq_right = (pygame.image.load('Assets/pacqrc.png'),pygame.image.load('Assets/pacqra.png'))

#The enemies
fantasmita = pygame.image.load('Assets/fantasmitav.png')

#To exit the game.
def quitgame():
  pygame.quit()
  quit()

#Function to create buttons on screen
def button(msg,x,y,w,h,ic,ac,action=None):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()

  if (x + w) > mouse[0] > x and (y+h) > mouse[1] > y:
    pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
    if click[0] == 1 and action != None:
      action()
  else:
    pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

  smalltext = pygame.font.Font('freesansbold.ttf',20)
  TextSurf, TextRect = text_objects(msg, smalltext)
  TextRect.center = ((x+(w//2)),(y+(h//2)))
  gameDisplay.blit(TextSurf, TextRect)

#Function to display the score
def scored():
  global score
  font = pygame.font.SysFont(None, 25)
  text = font.render("Last Score: "+str(score), True, black)
  gameDisplay.blit(text, (0, 0))

#Enemy in screen
def fantasmitas(tx, ty, tw, th, tc):
#  pygame.draw.rect(gameDisplay, tc, [tx, ty, tw, th])
  gameDisplay.blit(fantasmita,(tx,ty))

#Character to the screen dependig orientation
def character(orientation,x,y):
  if orientation == "u":
    gameDisplay.blit(pacq_up[random.randint(0, 1)],(x,y))
  elif orientation == "d":
    gameDisplay.blit(pacq_down[random.randint(0, 1)],(x,y))
  elif orientation == "l":
    gameDisplay.blit(pacq_left[random.randint(0, 1)],(x,y))
  elif orientation == "r":
    gameDisplay.blit(pacq_right[random.randint(0, 1)],(x,y))

#Function to draw test
def text_objects(text,font):
  textSurface = font.render(text, True, black)
  return textSurface, textSurface.get_rect()

#Function to display a message
def message_display(text):
  largetext = pygame.font.Font('freesansbold.ttf',115)
  TextSurf, TextRect = text_objects(text, largetext)
  TextRect.center = ((display_width//2),(display_height//2))
  gameDisplay.blit(TextSurf, TextRect)
  pygame.display.update()
#  pygame.quit()

#Wait
  time.sleep(2)

#Game Over!
def gameover():
  global score
  message_display("Game over!" + str(score))
  game_intro()

#Intro Screen
def game_intro():
  global score
  intro = True
  while intro:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    gameDisplay.fill(white)
    largetext = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Pac-Q", largetext)
    TextRect.center = ((display_width//2),(display_height//2))
    gameDisplay.blit(TextSurf, TextRect)

    button("Start!",150,450,100,50,green,bgreen,game_loop)
    button("Exit",550,450,100,50,red,bred,quitgame)

    scored()

    pygame.display.update()
    reloj.tick(15)

#GameLogic
def game_loop():
#  game_intro()
  global orientation
#Start position of the character?
  X = int(display_width * 0.45)
  Y = int(display_height * 0.8)

#The character movement
  x_change = 0
  y_change = 0

#Fantasmitas position
  t_startx = 100
  t_starty = 100
  t_speed = 6
  t_width = 80
  t_height = 80


#Upper and Left Bar.
  ub_startx = 0
  ub_starty = 0
  ub_width = display_width
  ub_height = 40
  
  lb_startx = 0
  lb_starty = 0
  lb_width = 100
  lb_height = display_height
  
#Flag to know if the game loop should exit
  gameexit = False


#Pintar Mapa
#for F in range(len(matriz)):
#    for C in range(len(matriz[0])):
#        print(matriz[F][C],end = ' ')
#    print(' ')

#PINTAR FONDO
  gameDisplay.fill(grey)
#PINTAR Marco
  pygame.draw.rect(gameDisplay, blue, [ub_startx, ub_starty, ub_width, ub_height])
  pygame.draw.rect(gameDisplay, blue, [lb_startx, lb_starty, lb_width, lb_height])


#LOOP PRINCIPAL DEL JUEGO
#LOOP PRINCIPAL DEL JUEGO
#LOOP PRINCIPAL DEL JUEGO
  while not gameexit:

    #Pintar sobre donde estuvieron los characters para que no dejen un trail
    #    fantasmitas(t_startx, t_starty, t_width, t_height, black)
    pygame.draw.rect(gameDisplay, grey, [t_startx, t_starty, t_width, t_height])
    #    character(orientation,int(X),int(Y))
    pygame.draw.rect(gameDisplay, grey, [int(X), int(Y), (int(X)+80), (int(Y)+80)])


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          down_pressed = True
          x_change = -4
          y_change = 0
          orientation = "l"
        elif event.key == pygame.K_RIGHT:
          down_pressed = True
          x_change = 4
          y_change = 0
          orientation = "r"
        elif event.key == pygame.K_UP:
          down_pressed = True
          y_change = -4
          x_change = 0
          orientation = "u"
        elif event.key == pygame.K_DOWN:
          down_pressed = True
          y_change = 4
          x_change = 0
          orientation = "d"

      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          down_pressed = False
          x_change = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
          down_pressed = False
          y_change = 0

#AVOID GOING AWAY FROM PLAYING AREA
    if (X < 100) and down_pressed and orientation == "l":
      x_change = 0
    if (X > (display_width - (pacq_width + 3))) and down_pressed and orientation == "r":
      x_change = 0
    if (Y < 40) and down_pressed and orientation == "u":
      y_change = 0
    if (Y > (display_height - (pacq_width + 3))) and down_pressed and orientation == "d":
      y_change = 0

    X += x_change
    Y += y_change

#PINTAR FONDO
#    gameDisplay.fill(grey)
#PINTAR Marco
#    pygame.draw.rect(gameDisplay, blue, [ub_startx, ub_starty, ub_width, ub_height])
#    pygame.draw.rect(gameDisplay, blue, [lb_startx, lb_starty, lb_width, lb_height])


#PINTAR PRIMERO LOS CUADRADOS POR DONDE PASO EL CARACTER, Y LUEGO PINTAR TODOS LOS CARACTERES EN PANTALLA

#ENEMIGOS
#Hay que reworkear esto
    fantasmitas(t_startx, t_starty, t_width, t_height, black)
#    t_starty = t_speed

#DIBUJADO DE PACQ
    character(orientation,int(X),int(Y))
#    scored(score)

#LOGIC
#COLISIONES

#COLISIONES


#VIejo codigo, si el enemigo paso toda la pantalla sin chocar sumaba uno al score
#
#    if (t_starty > display_height):
#      t_starty = 0 - t_height
#      t_startx = random.randrange(150,(display_width-232))
#      score += 1


#    if (Y < (t_starty + t_height)):
#      if (X > t_startx) and (X < (t_startx + t_width)) or ((X + pacq_width) > t_startx) and ((X + pacq_width) < (t_startx + t_width)):
#        gameover()
#        time.sleep(2)
#        gameexit = True

    pygame.display.update()
    reloj.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
