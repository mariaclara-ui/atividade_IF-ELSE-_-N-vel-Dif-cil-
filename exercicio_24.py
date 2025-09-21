produto = int(input("Qual e a quantidade de produto?"))
if produto<10:
    print("reabastecer")
elif produto<30:
    print("alerta")
else:
    print("normal")