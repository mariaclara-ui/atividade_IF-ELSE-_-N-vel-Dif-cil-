energia = int(input("Qual e a porcentagem de energia solar sobrando?"))

if energia<30:
    print("usar rede eletrica")
elif energia<=70:
    print("hibrido")
else:
    print("usar solar")