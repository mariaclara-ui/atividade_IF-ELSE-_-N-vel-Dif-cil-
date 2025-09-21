obstaculo = int(input("Qual e a distancia do obstaculo?"))

if obstaculo< 5:
    print("Freiar")
elif obstaculo<= 15:
    print("Reduzir velocidade")
else:
    print("Acelerar")