permissao = input("Qual é o seu cargo? ").lower()
if permissao == "operador basico":
    print("Acesso restrito")
elif permissao == "supervisor":
    print("Acesso parcial")
elif permissao == "engenheiro":
    print("Acesso total")
else:
    print("Cargo não reconhecido")
