#Como listas pero no accedemos por index, lo hacemos por valores de {}
#No tienen orden interno
#mutables

my_dict = {
    "David" : 35,
    "Erika" : 32,
    "Juan" : 50,
}

print (my_dict["David"])


#Retorname jairo, si no existe, mandame un 10
my_dict.get("jairo" , 10)


#reasignar 
my_dict["juan"] = 20
print (my_dict)


#borrar
del my_dict ["juan"]
print (my_dict)


#iterar por llaves
for llaves in my_dict.keys():
    print(llaves)


#iterar por valores
for valores in my_dict.values():
    print(valores)


#iterar por ambos
for llave, valor in my_dict.items():
    print(llave, valor)
    

#saber si esta booleano
print ("David" in my_dict)