class Namas:
    def __init__(self, plotas, verte):
        self._plotas = plotas
        self.__verte = verte

    @property
    def verte(self):
        return self.__verte

    @verte.setter
    def verte(self, nauja_verte):
        if nauja_verte < 0:
            print("Vertė negali būti neigiama")
        else:
            self.__verte = nauja_verte

namas1= Namas(150, 200)
print(namas1.verte)

namas1.verte = 255
print(namas1.verte)

namas1.verte = -120

