class ui:
    def __init__(self, cachorro):
        self.cachorro = cachorro
        self.comidas = [
                        {"nome": "biscoito", "valor": 10},
                        {"nome": "maca", "valor": 15},
                        {"nome": "salsicha", "valor": 8}
                        ]
        self.elementos = []
        
        
        x = 400
        for comida in self.comidas:
            #self.Botao(x,350,self.cachorro.comer, arg = comida["valor"])
            b = Botao(x,350)
            self.elementos.append(b)
            x += 50
                        
    def update(self):
        self.barrinha(10,50,self.cachorro.felicidade,color(255,255,0))
        
        self.barrinha(10,60,self.cachorro.fome)
        
        for elemento in self.elementos:
            elemento.update()
    
    def mouseClicado(self):
        for elemento in self.elementos:
            dx = mouseX - elemento.x
            dy = mouseY - elemento.y
        
            if dx >= 0 and dx <= elemento.w:
                if dy >= 0 and dy <= elemento.h:
                    elemento.clicado()
        
    def barrinha(self, x, y, qtd,cor = color(255,0,0)):
        tamanho = 250
        grossura = 8
        pre = map(qtd,0,100,0,250)
        
        stroke(30)
        strokeWeight(1)
        fill(255)
        rect(x,y,tamanho,grossura)
        
        noStroke()
        fill(cor)
        rect(x,y,pre,grossura)
        
                    
class Botao:
    w = 50
    h = 50
    cor = color(200,200,200)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def definirCallback(self, func):
        self.callback = func
        
    def update(self):
        stroke(30)
        strokeWeight(1)
        fill(self.cor)
        rect(self.x, self.y, self.w, self.h)
        
    def clicado(self):
        if hasattr(self, 'callback'):
            self.callback()