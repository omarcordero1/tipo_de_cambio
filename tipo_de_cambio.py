def exchanges(moneda,cantidad):
    result = 0
    # Pesos chilenos
    if moneda == 1:
        result = cantidad * 37.17
        print(f'Los {cantidad} pesos chilenos equivalen a {result} pesos mexicanos')
    # MonedPesosa colombianos
    elif moneda == 2:
        result = cantidad * 180.57
        print(f'Los {cantidad} pesos colombianos equivalen a {result} pesos mexicanos')
    # Pesos Argentinos
    elif moneda == 3:
        result = cantidad * 3.72
        print(f'Los {cantidad} pesos argentinos equivalen a {result} pesos mexicanos')
    # Dólares 
    elif moneda == 4:
        result = cantidad /0.048 
        print(f'Los {cantidad} Dólares equivalen a {result} pesos mexicanos')
    # Otro
    else:
        print('Ingresa solo un numero de la lista')
        


if __name__ == '__main__':
    try:
        moneda = int(input('''
        Ingresa el indice de la moneda que quieres convertira  dolar:
            [1] Moneda chilena a Dolar
            [2] Moneda colombiana a Dolar
            [3] Moneda argentida a Dolar
            [4] Moneda mexicana a Dolar
        Selecciona: '''))
        print('********************************')
        cantidad = int(input('Ingresa la cantidad que quieres convertir: '))
        exchanges(moneda,cantidad)
    except:
        print('* * * * * * E R R O R * * * * * *')
        print('Por favor, Ingresa solo valores numericos')