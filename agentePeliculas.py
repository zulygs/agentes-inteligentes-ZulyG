import random
import time

def agenteRecomendaciones():
    peliculasG = {
        "Infantil": ["Bebe en Pañales", "matilda", "Shrek", "Kun fu Panda", "Pie pequeño","Hotel Transilvania"],
        "Romance": ["Bajo la misma estrella", "La La Land", "El diario de Noha", "Yo despues de ti", "Orgullo y prejuicio"],
        "Familiar": ["Jumanji", "Dora", "Spider-Man", "Patos", "Los Locos Adams","Petter Rabbit"],
        "Aventura": ["Indiana Jones", "King Kong", "SOnic 3", "La momia", "La mascara del zorro"],
        "Terror": ["La llorona", "Anabelle", "IT", "El exoscismo de Emili Rouse", "Terrifier"]
    }
    
    print("Agente de Recomendacion de Peliculas")
    print("Géneros disponibles: Infantil, Romance, Familiar, Aventura, Terror")
    
    genero = input("Por favor, ingresa un genero de Peliculas: ").capitalize() 
    print(f"Iniciando busqueda del genero {genero}")
    time.sleep(5)
    
    if genero in peliculasG:
        pRecomendada = random.choice(peliculasG[genero])
        print(f"Peliculas Recomendadas:  '{pRecomendada}'")
    else:
        print("Género no válido. Por favor, elige un genero que se encuentra en la lista.")

agenteRecomendaciones()