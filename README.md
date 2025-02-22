# agentes-inteligentes-ZulyG

# Agente de Semaforo Inteligente

Descripcion
Este programa es un agente que actua como un semáforo inteligente reactivo
el cual controla el paso de vehiculos, el semaforo cambia de acuerdo al tiempo
establecido tomando en cuenta la cantidad de vehiculos en espera.

Ejemplo de Salida:
Semaforo en: Rojo  
Detectados 12 vehículos. Tiempo en verde ajustado a 10 segundos.  
Cambiando a verde espere: 10 segundos  
Semaforo en: Verde  
Cambiando a amarillo espere: 3 segundos  
Semaforo en: Amarillo  
Cambiando a rojo espere: 5 segundos

# Agente Buscador de Objetos (Basado en Objetivos)

Descripcion
Este agente se mueve en una matriz de 5x5 en busca de un objeto hasta encontrarlo.

Ejemplo de Salida:
⚪ ⚪ ⚪ ⚪ ⚪  
⚪ ⚪ 👩 ⚪ ⚪  
⚪ ⚪ ⚪ ⚪ ⚪  
⚪ ⚪ ⚪ 💻 ⚪  
⚪ ⚪ ⚪ ⚪ ⚪

⚪ ⚪ ⚪ ⚪ ⚪  
⚪ ⚪ ⚪ ⚪ ⚪  
⚪ ⚪ 👩 ⚪ ⚪  
⚪ ⚪ ⚪ 💻 ⚪  
⚪ ⚪ ⚪ ⚪ ⚪

Objeto encontrado por el agente!!

# Sistema Experto para Diagnóstico Simple (Basado en Conocimiento)

Descripcion
Este agente que proporciona un diagnostico basico basandose en los sintomas ingresados por el usuario, usa condiciones que definen
la sreglas del diagnostico e imprime la informacion que ha encontrado el agente.

Ejemplo de Salida:
Sistema Experto de Diagnóstico Médico  
Ingresa tus síntomas separados por comas (Ejemplo: fiebre, tos, dolor de cabeza, dolor de estómago, falta de aire, estornudos)

Síntomas: fiebre, tos, dolor de cabeza  
Iniciando Diagnóstico. Por favor, espere...

Posible diagnóstico: Resfriado.

# Agente de Recomendación de Películas (Basado en Aprendizaje)

Descripcion
Este agente recomienda una pelicula aleatoria basada en el genero que ha ingresado el usuario, tomando en
cuenta los generos que se han establecido por el agente.

Ejemplo de Salida:
Agente de Recomendacion de Peliculas  
Géneros disponibles: Infantil, Romance, Familiar, Aventura, Terror

Por favor, ingresa un género de películas: Aventura  
Iniciando búsqueda del género Aventura...

Película recomendada: 'Indiana Jones'

Tecnologias Usadas:
-Python
-Librerías: random, time
