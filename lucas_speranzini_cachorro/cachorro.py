#coding: utf-8
from random import randint

class cachorro:
    def __init__(self, nome, idade, cor, sexo, notif, patas = 4, fome = 0):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.sexo = sexo    
        self.patas = patas
        self.fome = fome
        self. felicidade = 100
        self.sono = 0
        self.notif = notif
        
    def __repr__(self):
        return "Este eh o cachorro" + self.nome +  ".Ele tem " + str(self.idade) + " anos."
    
    def comer(self, valor):
        if self.fome > valor:
            self.fome -= valor
            self.notif.novaMsg(self.nome + " adora essa comida ")
        else:
            self.notif.novaMsg(self.nome + " não quer comer...")
            
    def carinho(self):
        chance = randint(0,1)
        if chance == 1:
            self.felicidade += 10
            self.notif.novaMsg(self.nome + " nao ta afim de carinho seu babaca ")
            
    def mouseover(self):
        x = width/2
        y = height * 3/4
        d = ((mouseX - x)**2 + (mouseY - y)**2)**0.5
        r = 60
        if d < r:
            return True
        else:
            return False
        
                    
    def update(self):
        global height, width
        x = width/2
        y = height * 3/4
        w = 120
        h = 120
        fill(self.cor)
        ellipse(x,y,w,h)
        fill(255,0,255)
        ellipse(x+w/4,y,40,50)
        ellipse(x+w/4,y,20,25)
        ellipse(x-w/4,y,40,50)
        fill(255,0,255)
        ellipse(x-w/4,y,20,25)
        fill(0)
        ellipse(x+60,y,10,30)
        ellipse(x-60,y,10,30)
        
        fill(255,0,0)
        inicio = radians(-135)
        final = radians(-45)
        
        arc(x,y,w,h, inicio, final, CHORD)
        noFill()
        arc(x,y,w+15,h+15, radians(-180),radians(0))

        self.fome += 0.01
        self.fome = constrain(self.fome,0,100)
       
        self.felicidade -= 0.01
        self.felicidade = constrain(self.felicidade,0,100)