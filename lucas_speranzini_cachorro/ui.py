class ui:
    def __init__(self, cachorro):
        self.cachorro = cachorro
        self.comidas = [
                        {"nome": "biscoito", "valor": 10},
                        {"nome": "maca", "valor": 15},
                        {"nome": "salsicha", "valor": 8}
                        ]
                        
    def update(self):
        self.barrinha(10,50,self.cachorro.felicidade,color(255,255,0))
        
        self.barrinha(10,60,self.cachorro.fome)
        x = 400
        for comida in self.comidas:
            self.botao(x,350,self.cachorro.comer, arg = comida["valor"])
            x += 50
        
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
        
    def botao(self, x , y, callback, arg, cor = color(200,200,255)):
        stroke(30)
        strokeWeight(1)
        fill(cor)
        w = 50
        h = 50
        rect(x,y,w,h)
        dx = mouseX - x
        dy = mouseY - y
        
        if mousePressed :
            if dx >= 0 and dx <= w:
                if dy >= 0 and dy <= h:
                    callback(arg)