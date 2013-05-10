from carta import carta
import random


class hand():
    def __init__(self):
        self.lista = [carta(num%4,num//4) for num in random.sample(range(52),5)]

    def __str__(self):
        return str(self.lista)

    def pareja(self):
        valores = {carta.pasaravalor() for carta in self.lista}
        return len(valores) == 4

    def doblepareja(self):
        valores = [carta.pasaravalor() for carta in self.lista]
        setvalores = set(valores)
        return [valores.count(i) for i in setvalores].count(2) == 2
    
    def trio(self):
        valores = [carta.pasaravalor() for carta in self.lista]
        rep = [valores.count(x) for x in set(valores)]
        return 3 in rep and 2 not in rep

    def escalera(self):
        valores = [carta.valor for carta in self.lista]
        valores.sort()
        for i in range(len(valores)-1):
            if valores[i+1] != valores[i] + 1:
                return False
        return True

    def color(self):
        colores = {carta.pasaracolor() for carta in self.lista}
        return len(colores) == 1

    def full(self):
        valores = [carta.pasaravalor() for carta in self.lista]
        norep = set(valores)
        repeti = [valores.count(x) for x in norep]
        return repeti.count(2) == 1 and repeti.count(3) == 1

    def poker(self):
        valores = [carta.pasaravalor() for carta in self.lista]
        for i in valores:
            if valores.count(i) == 4:
                return True
        return False

    def esccolor(self):
        valores = [carta.valor for carta in self.lista]
        if self.color() and self.escalera() and min(valores) < 8:
            return True
        return False

    def florimperial(self):
        valores = [carta.valor for carta in self.lista]
        if self.color() and self.escalera() and min(valores) >= 8:
            return True
        return False
    
    def quees(self):
        if self.esccolor():
            return "Escalera de color"
        if self.florimperial():
            return "Flor imperial"
        if self.pareja():
            return "Pareja"
        if self.doblepareja():
            return "Doble pareja"
        if self.trio():
            return "Trio"
        if self.escalera():
            return "Escalera"
        if self.full():
            return "Full"
        if self.poker():
            return "Poker"
        if self.color():
            return "Color"
        
        
        else:
            return "Nada"

