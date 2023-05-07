from claseplan import PlanAhorro
import csv
class Lista:
  __planes= []

  def __init__(self):
   self.__planes=[]
  
  def agregarPlan(self,unplan):
   self.__planes.append(unplan)

  def mostrarplan(self):
    for plan in self.__planes:
     plan.mostrarDatos()

  def testListaplan(self):
     archivo= open('planes.csv')
     reader= csv.reader (archivo,delimiter= ';')
     for fila in reader:
      codPlan= int(fila[0])
      mod= fila[1]
      verVehic= fila[2]
      valor= fila[3]
      cantCudelplan= fila[4]
      cantCulic= fila[5]
      unplan= PlanAhorro(codPlan,mod,verVehic,valor,cantCudelplan,cantCulic)
      self.agregarPlan(unplan)
     
  def __iter__(self):
    return iter(self.__planes)
