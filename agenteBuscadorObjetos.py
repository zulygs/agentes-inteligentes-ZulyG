import random
import time

class AgenteBuscador:
    def __init__(self, tamaño=5):
        self.tamaño = tamaño
        self.matriz = [['⚪' for _ in range(tamaño)] for _ in range(tamaño)]

        self.AgenteFila, self.AgenteColumna = random.randint(0, tamaño - 1), random.randint(0, tamaño - 1)
        self.ObjFila, self.ObjColumna = random.randint(0, tamaño - 1), random.randint(0, tamaño - 1)

        while (self.AgenteFila, self.AgenteColumna) == (self.ObjFila, self.ObjColumna):
            self.ObjFila, self.ObjColumna = random.randint(0, tamaño - 1), random.randint(0, tamaño - 1)

    def verMatriz(self):
       
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                if i == self.AgenteFila and j == self.AgenteColumna:
                    print("👩", end=" ")
                elif i == self.ObjFila and j == self.ObjColumna:
                    print("💻", end=" ")
                else:
                    print("⚪", end=" ")
            print()
        print("\n")

    def moverAgente(self):
        while (self.AgenteFila, self.AgenteColumna) != (self.ObjFila, self.ObjColumna):
            self.verMatriz()
            time.sleep(1)  

            if self.AgenteFila < self.ObjFila:
                self.AgenteFila += 1
            elif self.AgenteFila > self.ObjFila:
                self.AgenteFila -= 1
            elif self.AgenteColumna < self.ObjColumna:
                self.AgenteColumna += 1
            elif self.AgenteColumna > self.ObjColumna:
                self.AgenteColumna -= 1

        print("Objeto encontrado por el agente!!")
        self.verMatriz()

if __name__ == "__main__":
    agente = AgenteBuscador()
    agente.moverAgente()
