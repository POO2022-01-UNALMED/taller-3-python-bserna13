
class TV():

    _numTV=0
    def __init__(self,marca,estado):
        self._marca=marca
        self._canal=1
        self._precio=500
        self._estado=estado
        self._volumen=1
        self._control=None
        TV._numTV+=1

    def setMarca(self,marca):
        self._marca=marca
    def getMarca(self):
        return self._marca

    def setCanal(self,canal):
        if self._estado:
            if 1<=canal<=120:
                self._canal=canal
    def getCanal(self):
        return self._canal

    def setControl(self,control):
        self._control=control
    def getControl(self):
        return self._control

    def setPrecio(self,precio):
        self._precio=precio
    def getPrecio(self):
        return self._precio

    def setVolumen(self,volumen):
        if self._estado:
            if 1<=volumen<=7:
                self._volumen=volumen
    def getVolumen(self):
        return self._volumen
    @staticmethod
    def getNumTV():
        return TV._numTV
    @staticmethod
    def setNumTV(numero):
        TV._numTV=numero
    
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    def getEstado(self):
        return self._estado

    def canalUp(self):
        if self._estado:
            if 1<=self._canal<120:
                self._canal+=1
    def canalDown(self):
        if self._estado:
            if 1<self._canal<=120:
                self._canal-=1

    def volumenUp(self):
        if self._estado:
            if 1<=self._volumen<7:
                self._volumen+=1
    def volumenDown(self):
        if self._estado:
            if 1<self._volumen<=7:
                self._volumen-=1

    

    






    
    




