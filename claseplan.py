
class PlanAhorro:
  def __init__ (self,codPlan,mod,vercVehic,valor,cantCudelplan,cantCulic):
    self.__codPlan= codPlan
    self.__mod= mod
    self.__vercVehic= vercVehic
    self.__valor= valor
    self.__cantCudelplan= cantCudelplan
    self.__cantCulic= cantCulic
  
  def getcod(self):
    return self.__codPlan

  def getmod(self):
    return self.__mod

  def getverc(self):
    return self.__vercVehic
  
  def getvalor(self):
    return self.__valor

  def getcuplan(self):
    return self.__cantCuplan
  
  def getculis(self):
    return self.__cantCulic

  def setvalor(self,v):
    self.__valor=v

  def mostrarDatos(self):
    print(f"Código de Plan: {self.__codPlan}")
    print(f"Modelo: {self.__mod}")
    print(f"Versión del vehículo: {self.__vercVehic}")
    print(f"Valor del vehículo: {self.__valor}")
    print(f"Cantidad de cuotas del plan: {self.__cantCudelplan}")
    print(f"Cantidad de cuotas a licitar: {self.__cantCulic}")
 