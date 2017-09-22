class cachorro:
    patas = 4
    
    def __init__(self, nome, idade, cor, sexo, patas = 4, fome = 0):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.sexo = sexo    
        self.patas = patas
        self.fome = fome
        self. felicidade = 100
        self.sono = 0
        
    def __repr__(self):
        return "Este eh o cachorro" + self.nome +  ".Ele tem " + str(self.idade) + " anos."
    
    def comer(self):
        if self.fome > 0:
            self.fome -= 20
            self.fome = constrain(self.fome, 0, 100)
            print (self.nome + " está mais feliz ")
        else:
            print (self.nome + " não quer comer...")
            
    def update(self):
        global height, width
        x = width/2
        y = height/2
        w = 10 * self.idade
        h = w * 2\3
        fill(self.cor)
        ellipse(x,y,w,h)
        rectMode(CENTER)

        
        self.fome += 0.01
        rect(x,y-h,self.fome,5)
        
        self.felicidade -= 0.01
        rect(x,y-h-15,self.felicidade,5)
 
caramelo = color(139, 87, 66)
dog = cachorro("basinga", 5, caramelo, "macho")



def setup():
    size(600,400)
    loadImage()

    
def draw():
    background(255,128,128)
    dog.update()
    
def keyPressed():
    if key == ' ':
        dog.comer()
    