#Hagamos un ejercicio en donde el usuario ingresa una variable númerica y por ---
#medio de una secuencia lógica me permita validar si un resultado es correcto.

print ("Mi tercer programa de combinación de variables")

num = float (input ("Ingrese un número de tres cifras:       "))

if num < 500:
    print ("¡Estuviste cerca!")
else: 
    num > 500
    print ("¡Rayos, pasaste el número indicado!")

if num == 500:
    print ("¡Correcto! Atinaste al número indicado")
else: 
    num < 500
    print ("¡Estuviste cerca! Sigue intentando")

print ("Tu resultado fue"  , num)