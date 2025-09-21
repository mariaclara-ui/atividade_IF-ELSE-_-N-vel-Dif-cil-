estado=(input("Qual e o estado do lote?")).lower()

if estado=="aprovado":
    print("Lote aprovado")
elif estado=="reprovado":
    print("Lote reprovado")
elif estado== "retrabalhado":
    print("Lote retrabalhado")
else:
    print("Lote necessida de uma analise manual")