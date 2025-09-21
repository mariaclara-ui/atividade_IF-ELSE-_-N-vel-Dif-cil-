tempe = int(input("Quantos graus?"))

if tempe<0:
    print("Alerta congelamento")
elif tempe<40:
    print("normal")
else:
    print("Alerta superaquecimento")
    