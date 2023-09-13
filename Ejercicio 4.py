#Vamos a crear un código que realice por pantalla un cálculo de variables, que nos permita sumar 
#restar y hacer operaciones para mostrar al final un resultado de cada operación y a su vez crear una tabla de
#la verdad y cada una de las operaciones usando "bool o usando and y or."

print ("Este programa no se debe hacer por chat gpt el que lo haga le bajo nota")

a = input ("Deme un número en pantalla    ")
b = input ("Deme un número mayor que el anteior     ")

a = int(a)
b = int(b)
print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a%b)

print ("Tabla de la verdad")
print (bool(a==a)) 
print (bool(a==a)) 
print (bool(a==b)) 
print (bool(a==b)) 

a = input ("Deme un número en pantalla    ")
b = input ("Deme un número mayor que el anteior     ")

a = int(a)
b = int(b)
print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a%b)

print ("Tabla de la verdad todo lo relacionado con O")
print ((str(a==a)) +  "O" + str (a==a) +  "--->" + str (a==a))
print ((str(a==a)) +  "O" + str (a==b) +  "--->" + str (a==a))
print ((str(a==b)) +  "O" + str (a==a) +  "--->" + str (a==a))
print ((str(a==b)) +  "O" + str (a==b) +  "--->" + str (a==b))