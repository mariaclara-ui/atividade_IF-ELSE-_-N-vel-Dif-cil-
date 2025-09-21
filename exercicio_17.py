roboA = input("O robô A está funcionando? (sim/não): ").lower() == "não"
roboB = input("O robô B está funcionando? (sim/não): ").lower() == "não"

if roboA and roboB:
    print("Parar a linha") 
elif roboA and not roboB:
    print("Acionar robô B") 
else:
    print("Continuar a produção") 