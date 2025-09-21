def new_func():
    energia = int(input("Qual é a porcentagem? "))

    if energia < 30:
        print("Modo econômico")
    elif energia <= 70:
        print("Modo normal")
    else:
        print("Modo turbo")

new_func()
