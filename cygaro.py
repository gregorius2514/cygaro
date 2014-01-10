import pygame, sys, os, random, time
from pygame.locals import *

class Block:
	def __init__ (self, x, y):
		self.x = x
		self.y = y

	def draw (self):
		block = pygame.draw.rect(screen,(255,255,255),[[self.x, self.y],[50, 10]], 1)
		screen.fill(Color("yellow"), block)

pygame.init()
pygame.mouse.set_visible(False)

wWIDTH = 640
wHEIGHT = 480

y = 470
runX = runY = True
ballX = ballY = 10
startGame = "not start"

 #utworzenie okna
window = pygame.display.set_mode((wWIDTH,wHEIGHT))
pygame.display.set_caption('Gra cygaro')

screen = pygame.display.get_surface()
myFont = pygame.font.SysFont("ubuntu", 20)

def input(events):
	for event in events:
		if event.type == QUIT:
			sys.exit(0)
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				sys.exit(0)
			if event.key == K_LEFT:
				shipLocation[0] -= 1	
			if event.key == K_RIGHT:
				shipLocation[0] += 1
			if event.key == K_SPACE:
				th1 = threading.Thread(target = drawShot)
				th1.start()
				th1.join()
			if event.key == K_a:
				cursor = pygame.draw.circle(screen, (255, 255, 255), pygame.mouse.get_pos(), 50, 1)
				screen.fill(Color("white"),cursor)
				pygame.display.flip()
			else:	
				print event

def gameOverMessage():
	screen.fill((0, 0, 0))
	myFont = pygame.font.SysFont("ubuntu", 35)
	label2 = myFont.render("Game Over", 1, (255, 0, 0))
	screen.blit(label2, (250, screen.get_height() / 2))
	pygame.display.flip()

blocksArray = []

def drawBlocks():
	(x, y) = (0, 20)
	for i in range(1,100):
		block = Block(x, y)
		blocksArray.append(block)

		if x + 52 >= wWIDTH:
			x = 0
			y += 12
		else:
			x += 52

drawBlocks()
points = 0

while True	:
	if startGame != "game over":
		mouseX, mouseY = pygame.mouse.get_pos()
	if startGame == "not start":
		but1, but2, but3 = pygame.mouse.get_pressed()
	
	input(pygame.event.get())
	
	if mouseX+50 > wWIDTH:
		mouseX = wWIDTH - 50

	if ballX + 10 > wWIDTH:
		runX = False
	if ballY + 10 > wHEIGHT:
		gameOverMessage()
		startGame = "game over"
	if ballX - 10 < 0:
		runX = True
	if ballY - 10 < 0:
		runY = True
	if ballY + 10 >= y and ballY + 10 <= y + 10:
		if ballX + 10 >= mouseX and ballX - 10  <= mouseX + 50:
			runY = False

	if startGame == "not start":
		if but1:
		 	startGame = "started"
		if startGame == "not start":
		 	ballX, ballY = mouseX + 22, y - 7
	
	if startGame != "game over":
		if runX:
			ballX += 1
		else:
			ballX -= 1
			
		if runY:
			ballY += 1
		else:
			ballY -= 1
	
		screen.fill((0,0,0))
		ball = pygame.draw.circle(screen,(255,255,255),[ballX, ballY],10,1)
		# screen.fill((255,255,255), ball)

		desk = pygame.draw.rect(screen,(255,255,255),[[mouseX, y],[50,y+10]], 1)
		screen.fill(Color("red"), desk)

		#if not ((ballX > enemyX and ballX+10 < enemyX + 50) and (ballY > enemyY and ballY+10 < enemyY + 10):
		
		for item in blocksArray:
			item.draw()
			if ballX > item.x and ballX < item.x + 50 and ballY > item.y and ballY < item.y + 10:
				points += 1	
				try:
					blocksArray.remove(item)
				except:
					pass

		label2 = myFont.render("Punkty: " + str(points), 1, (255, 0, 0))
		screen.blit(label2, (0, 0))
		pygame.display.flip()

		time.sleep(0.007)
		pygame.time.Clock().tick()
