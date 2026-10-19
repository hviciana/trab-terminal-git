lista = ["pinza", "tijera", "pinza"]
recuentopinzas = 0
pinzasesperadas =2
for i in lista:
    if i == "pinza":
        recuentopinzas += 1
if recuentopinzas == pinzasesperadas:
    print("El número de pinzas es el esperado.")
else:
    print("El número de pinzas no es el esperado.")