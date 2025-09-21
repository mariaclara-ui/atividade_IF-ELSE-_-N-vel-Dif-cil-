defeitos = int(input("Qual e a porcentagem de defeitos?"))
if defeitos<10:
    print("aprovar")
elif defeitos<20:
    print("trabalho")
else:
    print("reprovar")