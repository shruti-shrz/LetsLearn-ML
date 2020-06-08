import pygame
import time
import random 
import math
pygame.init() #initializing the pygame
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Test")
playerimg = pygame.image.load('D:/Download/person.png')
playerX = 730
playerY = 480
font = pygame.font.Font("freesansbold.ttf",15)
font2 = pygame.font.Font("freesansbold.ttf",20)
textX = 380
textY = 400
black = (0,0,0)
color_light = (170,170,170) 
graphimg = pygame.image.load('D:/Download/graph.png')
# dark shade of the button 
color_dark = (100,100,100)
width = 760
height = 920
smallfont = pygame.font.SysFont('Corbel',20)
myfont = pygame.font.SysFont("monospace", 15)

#pixAr = pygame.PixelArray(screen)
def drawline(s1,s2,e1,e2):
	pygame.draw.line(screen,(255,255,0),(s1,s2),(e1,e2),6)
def instruct():
	# render text
	text = font.render('Ok,got it!' , True , (255,0,0))
	label1 = font.render("Hello, for given points you have to draw",1, (0,0,0))
	label2 = font.render("straight line in such a way it passes through ", 1, (0,0,0))
	label3 = font.render("most of the points ", 1, (0,0,0))
	screen.blit(label1, (textX,textY))
	screen.blit(label2, (textX,420))
	screen.blit(label3, (textX,440))
	screen.blit(text , (textX,460))
	#alpha_surf = pygame.Surface(label1.get_size(), pygame.SRCALPHA)
	#screen.blit(text , (width/2+50,height/2))
	#inst = font.render('',True,black)
	#screen.blit(inst,(textX,textY))
flag=0
s=0
replay = 0
done =0
ch_x = 80
ch_y = 80
_x = 0
_y = 600 
def getslope():
	global replay
	s = abs(replay-(600-replay))/(500-0)
	return s
step = math.ceil(500/ch_x)
def graph():
	global _x,_y,replay
	screen.blit(graphimg,(0,0))
	s = getslope()
	if s ==0:
		s = 1
		replay =0
		_x =0
	for j in range(step+1):
		for m in range(10):
			pygame.draw.circle(screen, (0,0,0), (random.randint(_x, _x+ch_x), random.randint(600-(s*(_x+ch_x)+replay),600-(s*_x+replay))), 6)
		if(_x+ch_x>500):
			_x = 500
		else:
			_x = _x+ch_x
def try_again():
	#screen.fill((192,192,192))
	global _x,_y,done,replay
	t1 = font2.render("Try again line is not in", True , (0,0,0))
	t2 = font2.render("acceptable range", True , (0,0,0))
	screen.blit(t1, (textX,textY))
	screen.blit(t2, (textX,420))
	pygame.display.update()
	time.sleep(1)
	_x = 0
	screen.fill((255,255,255))
	graph()
	done =0
def end_fun():
	global done,flag,_x,_y,replay
	screen.fill((0,255,255))
	t1 = font2.render('Yepee!!! You got the linear rigression' , True , (0,0,0))
	t2 = font2.render('You have drawn the line which is at least distance' , True , (0,0,0))
	t3 = font2.render('from all the points.' , True , (0,0,0))
	t4 = font2.render("Replay", True , (255,0,0))
	screen.blit(t1,(50,80))
	screen.blit(t2,(50,110))
	screen.blit(t3,(50,140))
	pygame.draw.rect(screen,(0,0,0),[50,170,100,30])
	screen.blit(t4,(53,170))
	if replay >= 600:
		replay = 0
		
	else:
		replay = replay + 100
		
	_x = 0
	
	done=-1
	flag =-1
def player():
	screen.blit(playerimg,(playerX,playerY))
#game Loop
k=0
l=0
a = 0
b=0

running = True
while running:
	mouse = pygame.mouse.get_pos()
	if flag==0:
		screen.fill((0,255,255))
		instruct()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if flag==0:
				if width/2 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+25:
					flag = 1
		if event.type == pygame.MOUSEBUTTONDOWN:
			if flag==2 and done ==1:
				if 0 <=mouse[0]<=600 and 0 <=mouse[1] <=600:
					a = mouse[0]
					b = mouse[1]
					done =2
		if event.type == pygame.MOUSEBUTTONDOWN:
			if flag==2 and done==0:
				if 0 <=mouse[0]<=600 and 0 <=mouse[1] <=600:
					k = mouse[0]
					l = mouse[1]
					done =1
		if event.type == pygame.MOUSEBUTTONDOWN:
			if flag==-1 and done == -1:
				if 50 <=mouse[0]<=150 and 170 <=mouse[1] <=200:
					flag=1
					done =0
		
	if done == 2:
		drawline(k,l,a,b)
		slope = abs((l-b)/(k-a))
		const = abs(l-b)
		s = getslope()
		if s==0:
			s = 1
		print(slope)
		print(const)
		print(600-replay)
		if s-0.1 <=slope<= s+ 0.1 :
			pygame.display.update()
			time.sleep(1)
			end_fun()
		else:
			try_again()
		
					# print("check")
					# time.sleep(1)
					# slope = (443-l)/(k-100)
					# print(slope)
					# 
					# 	
					# else:
					# 	try_again()
		
							
	if flag==1:
		screen.fill((255,255,255))
		graph()
		flag=2
	#if flag == 2:
		#


	#
	# if width/2 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+25:
	# 	pygame.draw.rect(screen,color_light,[width/2,height/2,70,25])
	# else:
	# 	pygame.draw.rect(screen,color_dark,[width/2,height/2,70,25])
		# mouse = pygame.mouse.get_pos()
		# if 
		# drawline(660,20,660,500)
	player()
	pygame.display.update()
