produção = int(input("Quantas peças foram produzidas por hora?"))

if produção<50:
    print("baixo desempenho")
elif produção<100:
    print("regular")
else:
    print("otimo")