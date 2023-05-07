from claseplan import PlanAhorro
from claselista import Lista
import csv

def actualizar(listaplan):
  for plan in listaplan:
    nuevo_valor = float(input(f"Ingrese el nuevo valor del vehículo para el plan {plan.getcod()}: "))
    plan.setvalor(nuevo_valor)
    print(f"Valor actualizado del vehículo para el plan {plan.getcod()}: {plan.getvalor()}")
  
def mostrar_planes_menor_cuota(listaplan, valor_cuota):
    for plan in listaplan:
        cuota_plan = plan.get_valor() / plan.get_cant_cuotas()
        if cuota_plan < valor_cuota:
            print("Código de Plan:", plan.get_cod())
            print("Modelo:", plan.get_mod())
            print("Versión del vehículo:", plan.get_ver_v())
            print("Valor del vehículo:", plan.get_valor())
            print("Cantidad de cuotas del plan:", plan.get_cant_cuotas())
            print("Cantidad de cuotas a licitar:", plan.get_cant_culis())
            print("Valor de la cuota:", cuota_plan)
            print("")

def montoLicitar(plan, cantCulic):
  importeCuota = plan.getvalor() / plan.getcuplan()
  montoTotal = cantCulic * importeCuota
  return montoTotal

def modificar_cant_culis(listaplan):
  codPlan = int(input("Ingrese el código del plan que desea modificar: "))
  plan = listaplan.buscarPlan(codPlan)
  if plan is None:
    print("No se encontró el plan con código {}.".format(codPlan))
  else:
    nueva_cant_culis = int(input("Ingrese la nueva cantidad de cuotas para licitar: "))
    plan.set_cant_culis(nueva_cant_culis)
    print("La cantidad de cuotas para licitar del plan {} ha sido actualizada a {}.".format(codPlan, nueva_cant_culis))
             
def menu (listaplan):
  print("1: actualizar el valor del vehiculoo de cada plan\n")
  print("2: ingrese un valor de cuota para mostrar los datos del plan cuyo valor es menor al ingresado\n")
  print("3: Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota\n")
  print("4: Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.\n")
  print("0: opcion 0 salir")
  print(" Ingrese una opcion\n")
  op=int(input(""))

 
  while op!=0:
    if op==1:
      actualizar(listaplan)
       
    elif op==2:
    
        valor_cuota = float(input("Ingrese el valor de la cuota: "))
  mostrar_planes_menor_cuota(listaPlan, valor_cuota)
    
    elif op==3:
      codPlan = int(input("Ingrese el código de plan: "))
      plan = listaplan.buscarPlan(codPlan)
        if plan is None:
      print("No se encontró el plan con código {}.".format(codPlan))
        else:
      cantCulic = int(input("Ingrese la cantidad de cuotas para licitar: "))
      monto = montoLicitar(plan, cantCulic)
      print("El monto total que se debe haber pagado para licitar el vehículo es: {}".format(monto))
     
    elif op == 4:
      modificar_cant_culis(listaplan)
    elif op==0:
      print("terminado")
  
#def test(plan):
  
if __name__ =='__main__':
  listaPlan= Lista()
  listaPlan.testListaplan()
  listaPlan.mostrarplan()
  menu(listaPlan)
  