from mensagens import Mensageiro
from CACHORRO import Cachorro

caramelo = color(139, 87, 66)
dog = cachorro("basinga", 5, caramelo, "macho")
notif = Mensageiro(0,0)


def setup():
    global doglindo
    size(800,400)
    doglindo = loadImage("cachorro.png")

    
def draw():
    #background(255,128,128)
    image(doglindo, 0, 0, width, height)
    dog.update()
    notif.update()
    
def keyPressed():
    if key == ' ':
        dog.comer()
    