import time

class MaquinaHacerVelas:
    def __init__(self, derretir, insertar_color, verter_cera_molde):
        self.derretir = derretir
        self.color = insertar_color
        self.verter_cera = verter_cera_molde

    def derretir_cera(self):
        if self.derretir:
            for i in range(10, 80, 10):
                print(f"La máquina está calentando a {i} grados hasta que la cera se derrita...")
                time.sleep(1)
            return "La cera llegó a 80 grados, por lo cual se derritió por completo."
        else:
            return "La máquina no puede derretir la cera, controlar la temperatura."
        
    def insertar_color(self):
        if self.color == "rojo":
            return "El color que has insertado es rojo, por lo cual se puede continuar con el proceso."
        else:
            return "El color que has insertado no es el correcto, por lo cual no se puede continuar con el proceso."
   
    def verter_cera_molde(self):
        if self.verter_cera:
            return "Está listo para verter la cera en los moldes."
        else:
            return "No está listo para verter la cera al molde. Controlar si la cera está a temperatura correcta."

    def fabricar_vela(self):
        # Encapsulamiento del proceso completo de fabricación
        print("Comenzando el proceso de fabricación de velas...")
        time.sleep(1)

        print(self.derretir_cera())
        time.sleep(2)

        print(self.insertar_color())
        time.sleep(2)

        print(self.verter_cera_molde())
        time.sleep(2)

    def __str__(self):
        return ("Esta es una máquina para hacer velas con cera,para funcionar, tiene que llegar a 80 grados, el color que se le agrega debe ser rojo, y al derretirse por completo la cera, se puede verter en los moldes.")


# Creación de objetos
vela1 = MaquinaHacerVelas(True, "rojo", True)
vela2 = MaquinaHacerVelas(False, "azul", False)

# Proceso de fabricación de la primera vela (correcto)
print(vela1)
time.sleep(5)
print("--------------------------")
print("Proceso correcto, comienza el funcionamiento")
vela1.fabricar_vela()

# Proceso de fabricación de la segunda vela (fallo)
print("--------------------------")
print("Error: controlar el proceso")
vela2.fabricar_vela()
