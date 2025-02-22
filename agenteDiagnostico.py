import time

def agenteDiagnostico():
    print("Sistema Experto de Diagnóstico Médico")
    print("Ingresa tus síntomas separados por comas (Ejemplo: fiebre, tos, dolor de cabeza,dolor de estomago, falta de aire, estornudos)")

    Sintomas = input("🔍 Síntomas: ").lower().split(",")
    Sintomas = [s.strip() for s in Sintomas]
    print("Iniciando Diagnostico. Por favor, espere...")
    time.sleep(5)

    if "fiebre" in Sintomas and "tos" in Sintomas and "dolor de cabeza" in Sintomas:
        print("Posible diagnóstico: Resfriado.")
    elif "dolor de pecho" in Sintomas and "falta de aire" in Sintomas:
        print("Posible diagnóstico: Problemas cardiacos.")
    elif "dolor de estomago" in Sintomas and "nauseas" in Sintomas:
        print("Posible diagnóstico: Infeccion estomacal.")
    elif "estornudos" in Sintomas and "picazon en ojos" in Sintomas:
        print("Posible diagnóstico: Alergia.")
    else:
        print("No se encontró un diagnóstico preciso. Por favor, ingresa descripciones mas claras.")


agenteDiagnostico()
