pesos = input("Cuántos pesos mexicanos tienes?: ")
pesos =float(pesos)
valor_dolar = 20.96
dolares = pesos/ valor_dolar
dolare = round(dolares, 2)
dolares = str(dolares)
print("Tienes $ " + dolares + " dólares")
