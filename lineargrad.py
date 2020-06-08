import pygame
import time
import math
import random
pygame.init() #initializing the pygame
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("The game")
playerimg = pygame.image.load('D:/Download/person.png')
backimg = pygame.image.load('D:/Download/back.jpg')
heli = pygame.image.load('D:/Download/helicopter.png')
mont = pygame.image.load('D:/Download/mountains.png')
playerP = 380
playerP2 = 500
playerX = 380
playerY = 500
playerX_change = 0
playerY_change = 0
font = pygame.font.Font("freesansbold.ttf",22)
textX = 50
textY = 50
black = (0,0,0)
flag=0
error = 100
x = 700
y = 70
x_change = 100
y_change = 100
ch = round(math.sqrt(math.pow((playerX-x),2)+math.pow((playerY-y),2)),2)
dist = round(math.sqrt(math.pow((playerX-x),2)+math.pow((playerY-y),2)),2)
smallfont = pygame.font.SysFont('Corbel',25)
myfont = pygame.font.SysFont("monospace",25)
def end_funct():
	screen.blit(backimg,(0,0))
	t = font.render("You got the point with minimum error.",1, (255,255,255))
	t1 = font.render("This gradient decent concept is used in linear",1, (255,255,255))
	t2 = font.render("regression to find the value of slope and",1, (255,255,255))
	t3 = font.render("constant, so that drawn line will be at least",1, (255,255,255))
	t4 = font.render("distance from all the given points.",1, (255,255,255))
	t5 = font.render("Replay",1,(255,0,0))
	screen.blit(t,(50,50))
	screen.blit(t1,(50,80))
	screen.blit(t2,(50,110))
	screen.blit(t3,(50,140))
	screen.blit(t4,(50,170))
	pygame.draw.rect(screen,(0,0,0),[50,220,100,30])
	screen.blit(t5,(53,220))
	flag=0
def show_error():
	t = font.render("Error: "+str(round(error,2))+" Distance: "+str(dist),True,(0,0,0))
	screen.blit(t,(10,10))
def instruct():
	# render text
	text = font.render('Ok,got it!' , True , (255,0,0))
	label1 = font.render("Hello, Rescue Man.",1, (255,255,255))
	label2 = font.render("Over mountain some disaster victims are", 1, (255,255,255))
	label3 = font.render("trapped at different points.", 1, (255,255,255))
	label4 = font.render("Lets find the point from where all ", 1, (255,255,255))
	label5 = font.render('victims are at least distance.', 1, (255,255,255))
	label6 = font.render("Note:", 1, (255,255,255))
	label7 = font.render("Error meter is showing the error and ",1, (255,255,255))
	label8 = font.render('distance from that point.',1, (255,255,255))
	screen.blit(label1, (textX,textY))
	screen.blit(label2, (textX,80))
	screen.blit(label3, (textX,110))
	screen.blit(label4, (textX,140))
	screen.blit(label5, (textX,170))
	screen.blit(label6, (textX,200))
	screen.blit(label7, (textX,230))
	screen.blit(label8, (textX,260))
	screen.blit(text, (textX,290))
def player():
	screen.blit(playerimg,(playerP,playerP2))
running = True
while running:
	mouse = pygame.mouse.get_pos()
	if flag==0:
		screen.fill((0,255,255))
		screen.blit(backimg,(0,0))
		instruct()
		player()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if 50 <= mouse[0] <= 50+70 and 290 <= mouse[1] <= 290+25:
				flag = 1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -1
				#print("Left is pressed")
			if event.key == pygame.K_RIGHT:
				playerX_change = 1
				#print("right is pressed")
			if event.key == pygame.K_UP:
				playerY_change = -1
				#print("up is pressed")
			if event.key == pygame.K_DOWN:
				playerY_change = 1
				#print("down is pressed")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				playerX_change = 0
				playerY_change = 0
		if event.type == pygame.MOUSEBUTTONDOWN:
			if 50 <=mouse[0] <= 150 and 220 <= mouse[1] <= 250:
				x = random.randint(100,700)
				y = random.randint(80,520)
				# if y<450:
				# 	y = y+y_change
				# else:
				# 	y = 100
				print(x)
				print(y)
				flag=1
				#print("Key is released")
	
	if(flag==1):
		screen.fill((0,255,255))
		screen.blit(mont,(0,0))
		playerX+=playerX_change
		playerY+=playerY_change
		#playerY-=0.1
		if(playerX<=0):
			playerX =0
		if(playerX>=736):
			playerX = 736
		if(playerY<=0):
			playerY=0
		if(playerY>=536):
			playerY = 536
		screen.blit(heli,(playerX,playerY))
		dist = round(math.sqrt(math.pow((playerX-x),2)+math.pow((playerY-y),2)),2)
		error = ((dist - 10)/dist)*100
		show_error()
		# pygame.display.update()
		if(round(error)<=1):
			time.sleep(1)
			end_funct()
			playerX = 380
			playerY = 500
			flag=2
			player()
	pygame.display.update()