cracha_valido = input("Crachá válido? (sim/não): ").lower() == "sim"
capacete = input("Usa capacete de segurança? (sim/não): ").lower() == "sim"
horario_turno = input("Está no horário do turno? (sim/não): ").lower() == "sim"

if cracha_valido and capacete and horario_turno:
    print("Acesso permitido")
else:
    print("Acesso negado")
