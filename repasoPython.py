def numero_mayor_lista(lista_numeros):

    m = 0
    for i in lista_numeros:
        if m < i:
            m = i
    return m

def numero_menor_lista(lista_numeros):

    me = 10000000000
    for i in lista_numeros:
        if me > i:
            me = i
    return me

def numero_promedio_lista(lista_numeros):

    p = 0
    suma_numeros = 0

    for i in lista_numeros:
        suma_numeros += i

    p = suma_numeros / len(lista_numeros)

    return p


lista_numeros = []
numero_mayor = 0
numero_menor = 0
numero_promedio = 0

while True:
    valor_recibido = input("Escriba un número a añadir a la lista, o escriba 'salir' para terminar: ")

    if valor_recibido.lower() == "salir":
        break

    try:
        numero = int(valor_recibido)
        lista_numeros.append(numero)
    except ValueError:
        print("El valor introducido no es un número válido. Inténtelo de nuevo.")

print(f"Estos son los números que has escrito: {lista_numeros}")

numero_mayor = numero_mayor_lista(lista_numeros)
numero_menor = numero_menor_lista(lista_numeros)
numero_promedio = numero_promedio_lista(lista_numeros)

print (f"Numero mayor de la lista: {numero_mayor}, Numero menor de la lista: {numero_menor}, Numero promedio de la lista: {numero_promedio}")

