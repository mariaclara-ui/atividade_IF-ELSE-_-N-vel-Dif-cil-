erro = input("Qual tipo de erro ouve na produção?")
if erro==critico:
    print("parar linha")
elif erro==moderado:
    print("acionar manutenção")
else:
    print("continuar produçã")
