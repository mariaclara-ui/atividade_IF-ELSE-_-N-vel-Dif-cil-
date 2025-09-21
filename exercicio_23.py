rede = int(input("Qual e a porcentagem de trafego suspeito?"))
if rede<30:
    print("normal")
elif rede<70:
    print("alerta")
else:
    print("bloquear acesso")