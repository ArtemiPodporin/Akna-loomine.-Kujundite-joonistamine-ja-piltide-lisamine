import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((300,300))
ekraani_pind.fill((11,230,255))
pygame.display.set_caption("Esimene aken")

ristkülik=pygame.Rect(95,20,121,261)
pygame.draw.rect(ekraani_pind,(14,35,44),ristkülik)

zz=pygame.Rect(120,200,70,70)
pygame.draw.ellipse(ekraani_pind,(88,161,34),zz)
  
zz=pygame.Rect(120,115,70,70)
pygame.draw.ellipse(ekraani_pind,(255,229,11),zz)

zz=pygame.Rect(120,30,70,70)
pygame.draw.ellipse(ekraani_pind,(161,34,34),zz)

ristkülik=pygame.Rect(140,280,30,60)
pygame.draw.rect(ekraani_pind,(14,35,44),ristkülik)


"""
import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((0,0,0))
pygame.display.set_caption("Esimene aken")

pilt=pygame.image.load("cc.png")
ekraani_pind.blit(pilt,(640,480))

pilt=pygame.image.load("zzzz.png")
ekraani_pind.blit(pilt,(80,180))
"""


pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()