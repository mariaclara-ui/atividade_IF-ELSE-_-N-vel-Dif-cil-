defeitos = input("Qual e visibilidade dos defeitos?").lower()

if defeitos=="visivel":
    print("Nivel alto")
elif defeitos=="microscopio":
    print("Nivel medio")
elif defeitos==("ausente"):
    print("Nivel baixo")
else:
    print("sem defeitos")