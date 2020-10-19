import pygame
import time
import random

pygame.init()

#Size of the game area
display_width = 820
display_height = 660

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

#Main character
pacq_width = 80
orientation = "r"
speed = 1

#Global variable with the score
score = 0

#Map
mapa = [[1,0,1,1,1,1,0,1],
        [0,0,0,0,0,0,0,0],
        [1,0,1,1,1,1,0,1],
        [0,0,0,0,0,1,0,0],
        [1,0,1,0,0,1,0,1],
        [0,0,1,1,0,1,0,0],
        [1,0,0,0,0,0,0,1]]

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

def colisionesup(mapas,x,y,xx,yy):
  for cuadrante in reversed(mapas):
    if y == cuadrante[3]+1 and x >= cuadrante[0] and x <= cuadrante[1]:
      return True
    elif y == cuadrante[3]+1 and xx >= cuadrante[0] and xx <= cuadrante[1]:
      return True
  return False

def colisionesd(mapas,x,y,xx,yy):
  for cuadrante in mapas:
    if yy == cuadrante[2]+1 and x >= cuadrante[0] and x <= cuadrante[1]:
      return True
    elif yy == cuadrante[2]+1 and xx >= cuadrante[0] and xx <= cuadrante[1]:
      return True
  return False

def colisionesl(mapas,x,y,xx,yy):
  for cuadrante in reversed(mapas):
    if x == cuadrante[1]+1 and y >= cuadrante[2] and y <= cuadrante[3]:
      return True
    elif x == cuadrante[1]+1 and yy >= cuadrante[2] and yy <= cuadrante[3]:
      return True
  return False

def colisionesr(mapas,x,y,xx,yy):
  for cuadrante in reversed(mapas):
    if xx == cuadrante[0]+1 and y >= cuadrante[2] and y <= cuadrante[3]:
      return True
    elif xx == cuadrante[0]+1 and yy >= cuadrante[2] and yy <= cuadrante[3]:
      return True
  return False

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
  global speed
#  game_intro()
  global orientation
#Start position of the character?
  X = 0
  Y = 0

#The character movement
  x_change = 0
  y_change = 0

#Fantasmitas position
  f_startx = 0
  f_starty = 0
  f_speed = 3
  f_width = 80
  f_height = 80

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

  collisiones = []

  down_pressed = False

  fantaspos = False
  Distancia = 0
#Armar Mapa
  for F in range(len(mapa)):
      for C in range(len(mapa[F])):
          if mapa[F][C]:
            collisiones.append(((90*C)+lb_width,((90*C)+90)+lb_width,(90*F)+ub_height,((90*F)+90)+ub_height))
          else:
            if not fantaspos:
              f_startx = (90*C)+lb_width
              f_starty = (90*F)+ub_height
              fantaspos = True
            
            if Distancia > 3:
              X = (90*C)+lb_width
              Y = (90*F)+ub_height
            
            Distancia += 1

#PINTAR FONDO
  gameDisplay.fill(grey)
#PINTAR Marco
  pygame.draw.rect(gameDisplay, blue, [ub_startx, ub_starty, ub_width, ub_height])
  pygame.draw.rect(gameDisplay, blue, [lb_startx, lb_starty, lb_width, lb_height])

#PINTAR MAPA
  for cuadro in collisiones:
    pygame.draw.rect(gameDisplay, red, [cuadro[0], cuadro[2], pacq_width, pacq_width])

#LOOP PRINCIPAL DEL JUEGO
#LOOP PRINCIPAL DEL JUEGO
#LOOP PRINCIPAL DEL JUEGO
  while not gameexit:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          #down_pressed = True
          x_change = (0-speed)
          y_change = 0
          orientation = "l"
        elif event.key == pygame.K_RIGHT:
          #down_pressed = True
          x_change = speed
          y_change = 0
          orientation = "r"
        elif event.key == pygame.K_UP:
          #down_pressed = True
          y_change = (0-speed)
          x_change = 0
          orientation = "u"
        elif event.key == pygame.K_DOWN:
          #down_pressed = True
          y_change = speed
          x_change = 0
          orientation = "d"

      #if event.type == pygame.KEYUP:
      #  if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
      #    down_pressed = False
      #    x_change = 0
      #  elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
      #    down_pressed = False
      #    y_change = 0

#AVOID GOING AWAY FROM PLAYING AREA
#    if (X < 100) and down_pressed and orientation == "l":
#      x_change = 0
#    if (X > (display_width - (pacq_width + 3))) and down_pressed and orientation == "r":
#      x_change = 0
#    if (Y < 40) and down_pressed and orientation == "u":
#      y_change = 0
#    if (Y > (display_height - (pacq_width + 3))) and down_pressed and orientation == "d":
#      y_change = 0

    if orientation == "l":
      if (X <= 101):
        x_change = 0
      elif colisionesl(collisiones,X,Y,(X+pacq_width),(Y+pacq_width)):
        x_change = 0
    
    if orientation == "r":
      if (X >= (display_width - (pacq_width + 3))):
        x_change = 0
      elif colisionesr(collisiones,X,Y,(X+pacq_width),(Y+pacq_width)):
        x_change = 0

    if orientation == "u":
      if (Y <= 41):
        y_change = 0
      elif colisionesup(collisiones,X,Y,(X+pacq_width),(Y+pacq_width)):
        y_change = 0
    
    if orientation == "d":
      if (Y >= (display_height - (pacq_width + 3))):
        y_change = 0
      elif colisionesd(collisiones,X,Y,(X+pacq_width),(Y+pacq_width)):
        y_change = 0


    X += x_change
    Y += y_change

#PINTAR FONDO
#    gameDisplay.fill(grey)
#PINTAR Marco
#    pygame.draw.rect(gameDisplay, blue, [ub_startx, ub_starty, ub_width, ub_height])
#    pygame.draw.rect(gameDisplay, blue, [lb_startx, lb_starty, lb_width, lb_height])


#PINTAR PRIMERO LOS CUADRADOS POR DONDE PASO EL CARACTER, Y LUEGO PINTAR TODOS LOS CARACTERES EN PANTALLA
    #Pintar sobre donde estuvieron los characters para que no dejen un trail
    #    fantasmitas(t_startx, t_starty, t_width, t_height, black)
    pygame.draw.rect(gameDisplay, grey, [f_startx, f_starty, f_width, f_height])
    #    character(orientation,int(X),int(Y))
    pygame.draw.rect(gameDisplay, grey, [X-1, Y-1, pacq_width, pacq_width])
#ENEMIGOS
#Hay que reworkear esto
    fantasmitas(f_startx, f_starty, f_width, f_height, black)
#    t_starty = t_speed

#DIBUJADO DE PACQ
    character(orientation,X,Y)
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
