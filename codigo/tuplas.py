# Las tuplas no se pueden modificar a diferencia de las listas
# puede contener cualquier tipo de dato
# se puede devolver varios valores en una funcion

my_tuple = ()
type(my_tuple)
my_tuple = (1, "dos" , True)
print (my_tuple [0])

# sin coma no se crea de tipo tupla
my_tuple = (1,)
my_other_tuple = (2,3,4)
my_tuple += my_other_tuple
print (my_tuple)


#desenpaquetar
x, y, z = my_other_tuple
print (x,y,z)


