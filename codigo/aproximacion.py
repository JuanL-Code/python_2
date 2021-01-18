#encontrar cualquier raiz, asi sea aproximada
#epsilon : que tan exacto deseo ser
#paso : que tanto acercanos en cada iteracion
#respuesta : donde se guardara
objetivo = int(input("Escoge un numero: "))
# mas ceros, mas exacto
epsilon = 0.000001
paso = epsilon**2
respuesta = 0.0
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso


if abs(respuesta**2 - objetivo) >= epsilon:
    print(f"No se encontro raiz cuadrada de {objetivo}")
else:
    respuesta = round(respuesta, 3)
    print(f"la raiz cuadra de {objetivo} es {respuesta}")



