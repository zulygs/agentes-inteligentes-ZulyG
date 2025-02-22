import time
import random

class Agente_Semaforo:
    def __init__(self):
        self.estado = "Rojo"  
        self.tVerde = 10  
        self.tAmarillo = 3  
        self.tRojo = 5  

    def vehiculosDetectados(self):
        return random.randint(0, 25)

    def AjustesTVerde(self, cVehiculos):
        if cVehiculos < 5:
            self.tVerde = 5
        elif 5 <= cVehiculos < 15:
            self.tVerde = 10
        else:
            self.tVerde = 15

    def cambiarEstado(self):
        if self.estado == "verde":
            print(f"Cambiando a amarillo espere: {self.tAmarillo} segundos")
            self.estado = "amarillo"
            time.sleep(self.tAmarillo)
        elif self.estado == "amarillo":
            print(f"Cambiando a rojo espere: {self.tRojo} segundos")
            self.estado = "Rojo"
            time.sleep(self.tRojo)
        elif self.estado == "Rojo":
            CantidadV = self.vehiculosDetectados()
            self.AjustesTVerde(CantidadV)
            print(f"Detectados {CantidadV} vehículos. Tiempo en verde ajustado a {self.tVerde} segundos.")
            print(f"Cambiando a verde espere: {self.tVerde} segundos")
            self.estado = "verde"
            time.sleep(self.tVerde)

    def Iniciar(self):
        while True:
            print(f"Semaforo en: {self.estado}")
            self.cambiarEstado()

if __name__ == "__main__":
    semaforo = Agente_Semaforo()
    semaforo.Iniciar()