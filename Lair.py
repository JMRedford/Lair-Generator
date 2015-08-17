import pygame, time, random, math

random.seed()

xBlocks = 50
yBlocks = 40
blockSize = 10

GREY = (200,200,200)

pygame.init()
disp = pygame.display.set_mode([xBlocks*blockSize,yBlocks*blockSize],pygame.NOFRAME)

model = []
probs = [[1,0,0,0],[0.5,0.22,0.06,0.22],[0.45,0.23,0.09,0.23],[0.4,0.23,0.14,0.23],[0.35,0.23,0.19,0.23],[0.3,0.24,0.22,0.24],[0.25,0.25,0.25,0.25]]

for i in range(0,xBlocks):
  model.append([])
  for j in range(0,yBlocks):
    model[i].append([pygame.Rect(i*blockSize,j*blockSize,blockSize,blockSize),0])

model[xBlocks/2][yBlocks-2][1] = 1

def updateModel():
  pos = (xBlocks/2,yBlocks-2)
  lastDir = (0,-1)
  while model[pos[0]][pos[1]][1] > 0:
    randNum = random.random()
    if randNum < probs[min(yBlocks-2-pos[1],6)][0]:
      lastDir = (0,-1)
      pos = (pos[0],pos[1]-2)
    elif randNum < probs[min(yBlocks-2-pos[1],6)][0] + probs[min(yBlocks-2-pos[1],6)][1]:
      lastDir = (1,0)
      pos = (pos[0]+2,pos[1])
    elif randNum < probs[min(yBlocks-2-pos[1],6)][0] + probs[min(yBlocks-2-pos[1],6)][1] + probs[min(yBlocks-2-pos[1],6)][2]:
      lastDir = (0,1)
      pos = (pos[0],pos[1]+2)
    else:  
      lastDir = (-1,0)
      pos = (pos[0]-2,pos[1])
  model[pos[0]][pos[1]][1] = 1
  model[pos[0]-lastDir[0]][pos[1]-lastDir[1]][1] = 1
  print('update model')

def updateView():
  for i in range(0,xBlocks):
    for j in range(0,yBlocks):
      if model[i][j][1] == 1:
        surf = pygame.Surface((blockSize,blockSize))
        surf.fill(GREY)
        disp.blit(surf,model[i][j][0])
  pygame.display.flip()

while(1):
  e = pygame.event.poll()
  if (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
    break
  if (e.type == pygame.KEYDOWN and e.key == pygame.K_PERIOD):
    updateModel()
    updateView()

pygame.quit()
