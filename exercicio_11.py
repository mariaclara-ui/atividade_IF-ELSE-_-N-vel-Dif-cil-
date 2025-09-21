bateria = int(input("Qual e o nivel de bateria?"))

if bateria<20:
    print("Retorno imediato")
elif bateria<60:
    print("Rcota curta")
else:
    print("Rota longa")