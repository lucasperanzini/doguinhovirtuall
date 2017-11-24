from mensagens import Mensageiro
from cachorro import cachorro
from ui import ui

caramelo = color(139, 87, 66)
notif = Mensageiro(0,0)
dog = cachorro("spot", 5, caramelo, "macho", notif)
interface = ui(dog)


def setup():
    global doglindo
    size(600,400)
    doglindo = loadImage("cachorro.png")

    
def draw():
    #background(255,128,128)
    image(doglindo, 0, 0, width, height)
    dog.update()
    notif.update()
    interface.update()
    
def keyPressed():
    if key == ' ':
        dog.comer()

def mouseClicked():
    if dog.mouseover():
        dog.carinho()