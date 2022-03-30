class TV:
    _numTV = 0
    def __init__(self,marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV._numTV += 1

    # Marca
    def setMarca(self,marca):
        self._marca = marca
    def getMarca(self):
        return self._marca
    
    # Control
    def setControl(self,control):
        self._control = control
    def getControl(self):
        return self._control

    # Precio
    def setPrecio(self,precio):
        self._control = precio
    def getPrecio(self):
        return self._precio
    
    # Volumen
    def setVolumen(self,volumen):
        self._volumen = volumen
    def getVolumen(self):
        return self._volumen
    
    # Canal
    def setCanal(self,canal):
        if ((self._estado) and (canal < 120)):
            self._canal = canal
    def getCanal(self):
        return self._canal
    
    @classmethod
    def setNumTV(cls,num):
        cls._numTV = num
    @classmethod
    def getNumTV(cls):
        return cls._numTV

    # Apagado-Encendido-Estado
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False
    
    # Estado
    def getEstado(self):
        return self._estado


    # CanalUp - CanalDown
    def canalUp(self):
        if ((self._estado) and (self._canal < 120)):
            self._canal += 1 
    def canalDown(self):
        if ((self._estado) and (self._canal>1)):
            self._canal -= 1
    
    # VolumenUp - VolumenDown
    def volumenUp(self):
        if ((self._estado) and (self._volumen < 7)):
            self._volumen += 1
    def volumenDo(self):
        if ((self._estado) and (self._volumen > 0)):
            self._volumen -= 1


    

    






    
    




