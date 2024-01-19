class Numero:
    def __init__(self):
        pass

    def ordenar_contar(self):
        lista = []
        for i in range(10):
            numero = int(input("número:"))
            lista.append(numero)

        lista_ordenada = sorted(lista) 

        cantidad_pares = 0
        cantidad_impares = 0
        lista_pares = []
        lista_impares = []

        for numero in lista_ordenada:

            if numero % 2 == 0:
                cantidad_pares += 1
                if numero not in lista_pares:
                    lista_pares.append(numero)
            else:
                cantidad_impares += 1
                if numero not in lista_impares:
                    lista_impares.append(numero)

        print("Lista ordenada:", lista_ordenada)
        print("Pares:", cantidad_pares, lista_pares)
        print("Impares:", cantidad_impares, lista_impares)

def main():
    obj = Numero()
    obj.ordenar_contar()

if __name__ == "__main__":
    main()
