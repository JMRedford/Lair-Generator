import pygame, time

pygame.init()

def updateModel():
  print('update model')

def updateView():
  print('update view')

pygame.display.set_mode([500,400],pygame.NOFRAME)

while(1):
  e = pygame.event.poll()
  if (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
    break
  if (e.type == pygame.KEYDOWN and e.key == pygame.K_PERIOD):
    updateModel()
    updateView()

pygame.quit()
