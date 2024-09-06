
import time
class Maquina_hacer_velas():
    def __init__(self, derretir, insertar_color, verter_cera_molde):
        self.derretir = derretir
        self.color = insertar_color
        self.verter_cera = verter_cera_molde
    
    

    def derretir_cera(self):
        if self.derretir == True:
            for i in range(10, 80, 10):
                print(f"La maquina esta calentando a {i} grados hasta que la cera se derrita...")
                time.sleep(1)
            return "La cera llego a 80 grados, por lo cual se derritio y esta lista para ser vertida en el molde"
        elif self.derretir == False:
            print("La maquina no puede derretir la cera, controlar la temperatura")
        
    def insertar_color(self):
        if self.color == "rojo":
           print( "El color que has insertado es rojo, por lo cual se puede continuar con el proceso.")
        else:
            print( f"El color que has insertado no es rojo, por lo cual no se puede continuar con el proceso.")
   
    def verter_cera_molde(self):
        if self.verter_cera == True:
            print("Esta listo para verter la cera al molde ")
        elif self.verter_cera == False:
            print("No esta listo para verter la cera al molde, controlar si se encuentra la cera en el molde.")
            
    def __str__(self):
        return "Esta es una maquina para hacer velas con cera, para funcionar, tiene que llegar a 80 grados, el color que se le agrega debe ser rojo, y al derretirse por completo la cera, se puede verter en los moldes."
    
    
vela1 = Maquina_hacer_velas(True, "rojo", True)
vela2 = Maquina_hacer_velas(False,"azul", False)

print(vela1.__str__())
time.sleep(5)
print("--------------------------")
print("Proceso correcto, comienza el funcionamiento")
time.sleep(2)
#En este caso la prueba es correcta y va bien encaminada
print(vela1.derretir_cera())
vela1.insertar_color()
vela1.verter_cera_molde()
time.sleep(3)
print("--------------------------")
#En este caso la prueba falla porque la maquina no puede derretir la cera
print("Error: controlar el proceso")
time.sleep(2)
print(vela2.derretir_cera())
vela2.insertar_color()
vela2.verter_cera_molde()



# PRUEBAS UNITARIAS 
import unittest