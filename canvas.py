import sys, pygame
import PIL
from PIL import Image
from pygame.locals import *
import json
import os.path as path
# - network.py example:
import network
def AllCanvas():
    
    pygame.init()

    ventana = pygame.display.set_mode((500,500))
    titulo = pygame.display.set_caption("Reconocimiento de numeros")

    ventana.fill((255,255,255))

    brush = pygame.image.load("dot.png")
    brush = pygame.transform.scale(brush,(16,16))
    pygame.display.update()
    clock = pygame.time.Clock()

    t = 0
    a = 1
    b = 1

    while 1:
        clock.tick(60)
        x,y = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == KEYDOWN:
                if (event.key == K_KP_ENTER or event.key == K_RETURN ) :
                    pygame.image.save(ventana,"prueba.png" )             
                    im = Image.open("prueba.png")
                    #toJS(im)
                    im = im.rotate(90)
                    #im.show()
                    im = im.resize((28, 28), PIL.Image.LANCZOS)
                    runarray = []
                    for a in range(0,28): #Ancho
                        #for b in range(0,28): #Largo
                        for b in range(27,-1,-1): #Largo
                            pix = im.load()
                            pix[a,b]
                            if pix[a,b] == (255, 255, 255):
                                runarray.append(0)
                            else:
                                runarray.append(1)
                    return runarray
                if event.key == K_BACKSPACE:
                    ventana.fill((255,255,255))
                    pygame.display.update()
                        
            elif event.type == MOUSEBUTTONDOWN:
                t = 1                                     
                
            elif event.type == MOUSEBUTTONUP:
                t = 0
                    
            if t == 1:
                ventana.blit(brush,(x-8,y-8))
                pygame.display.update()

def finalWindow(response):
    pygame.init()
 
    pygame.display.set_caption('El resultado es:')
    size = [400, 400]
    screen = pygame.display.set_mode(size)
     
    clock = pygame.time.Clock()
     
    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render(response, True, (255, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
     
    screen.fill((255, 255, 255))
    screen.blit(text, textrect)
     
    pygame.display.update()
     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
     
        clock.tick(20)
def toJS(im):
    im = im.rotate(90)
    #resize image
    imResize = im.resize((28, 28), PIL.Image.LANCZOS)
    runarrayResize = []
    for a in range(0,28): #Ancho
        runarrayResize.append([])
        for b in range(27,0,-1): #Largo
            pix = imResize.load()
            pix[a,b]
            if pix[a,b] == (255, 255, 255):
                runarrayResize[a].append(0)
            else:
                runarrayResize[a].append(1)
    data = {
        "ImageResize": [runarrayResize],      
    }
    with open('./imagenes.json', 'w') as outfile:
        json.dump(data, outfile)