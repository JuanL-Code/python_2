
nombre1 = input('Bienvenido usuario 1!, Escribe tu nombre: ')
nombre1_edad = int(input("Hola, cual es tu edad: "))
saludo_1 = f'Hola {nombre1}, es un placer conocerte!'


print ("Ahora usuario 2, pon los datos correspondientes")


nombre2 = input('Bienvenido usuario 2!, Escribe tu nombre: ')
nombre2_edad = int(input("Hola, cual es tu edad: "))
saludo_2 = f'Hola {nombre2}, es un placer conocerte!'

if nombre1_edad > nombre2_edad:
    print(f'¿Sabías que usuario 1 es mayor que usuario 2?')
elif nombre2_edad > nombre1_edad:
    print(f'¿Sabías que el mensaje usuario 2 es mayor que usuario 1')
else:
    print(f'¿Sabías que ambos tienen la misma edad')


