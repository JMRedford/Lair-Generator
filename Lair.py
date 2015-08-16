import pygame, time, random

xBlocks = 25
yBlocks = 20
blockSize = 20

GREY = (200,200,200)

pygame.init()
disp = pygame.display.set_mode([xBlocks*blockSize,yBlocks*blockSize],pygame.NOFRAME)

model = [];

for i in range(0,xBlocks):
  model.append([])
  for j in range(0,yBlocks):
    model[i].append([pygame.Rect(i*blockSize,j*blockSize,blockSize,blockSize),0])

model[12][18][1] = 1

def updateModel():
  print('update model')

def updateView():
  for i in range(0,25):
    for j in range(0,20):
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
