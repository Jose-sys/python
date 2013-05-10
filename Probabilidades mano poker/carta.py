class carta():
    
    def __init__(self,color,valor):
        self.color = color # 0 - 3
        self.valor = valor # 0 - 12

    def pasaravalor(self):
        if 0<= self.valor and self.valor <=8:
            return str(self.valor+2)
        if self.valor == 9:
            return "J"
        if self.valor == 10:
            return "Q"
        if self.valor == 11:
            return "K"
        if self.valor == 12:
            return "A"

    def pasaracolor(self):
        if self.color == 0:
            return "H"
        if self.color == 1:
            return "D"
        if self.color == 2:
            return "S"
        if self.color == 3:
            return "C"

    def __repr__(self):
        return (self.pasaravalor()+self.pasaracolor())
