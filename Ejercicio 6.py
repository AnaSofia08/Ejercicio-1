#Este programa va a tener como finalidad mezclar varios elementos que pueda solicitar el usuoario o 
#vamos a colocar diferentes metodos para poder realizar actividades simples o secuenciasles
#del mismo modo permitira realizar salidad de información sujetas a condiciones lógicas

#print ("-----------------------------------Inicio del programa-------------------------------------------")

#Edad1 = int(input("¿Cuál es tu edad?")) 

#if Edad1 < 18:
#    print ("Eres menor de edad")
#else:
#    print ("¿Ya sacaste tu cédula?")

#print ("----------------------------------------Módulo de seguridad--------------------------------------")

#Acá el usuario una vez se establece si es mayor de edad, le vamos a solicitar una contraseña

#print ("Su contraseña fue enviada exitosamente a su correo")
#Clave_mayor_edad = "Contraseña"
#password = input("Ingrese la contraseña que fue enviada a su correo")

#if Clave_mayor_edad == password.lower (): 
#    print ("Contraseña correcta")
#else:
#    print ("Contraseña incorrecta")

#print ("--------------------------------------Módulo de interacción-------------------------------------")

#print ("Escriba una frase o palabra para seguir adelante en la autenticación")

#frase = input ("Introduce una frase")

#si desea reemplazar la contraseña, solicite al usuario escribir en diferentes letras o números 
#la nueva contraseña o simplemente solicite u parametro de validación

#vocal = input ("Introduzca una vocal en minuscula")
#print (frase.replace(vocal, vocal.upper))

#print ("Usted a completado los tres módulos de autenticación / puede seguir adelante con el pago")


print ("--------------------------------------Inicio programa 2---------------------------------")

Año_nacimiento = int(input("¿En que año naciste?")) 

if Año_nacimiento > 2005:
    print ("Eres menor de edad")
else:
    print ("Eres mayor de edad")

print ("----------------------------------------Módulo de seguridad--------------------------------------")

#Acá el usuario una vez se establece si es mayor de edad, le vamos a solicitar una contraseña

print ("Cree una nueva contraseña")
Clave_mayor_edad = "Contraseña"
password = input("Ingrese una contraseña en letras mayusculas sin espacios")

if Clave_mayor_edad == password.capitalize (): 
    print ("Contraseña correcta")
else:
    print ("Contraseña incorrecta")

print ("--------------------------------------Módulo de interacción-------------------------------------")

print ("Escriba su deporte favorito para seguir adelante en la autenticación")

frase = input ("Ingresa tu deporte favorito")
color = input ("Ingresa tu color favorito")

#si desea reemplazar la contraseña, solicite al usuario escribir en diferentes letras o números 
#la nueva contraseña o simplemente solicite u parametro de validación


print (frase.replace (color, ))

print ("Usted a completado los tres módulos de autenticación / puede seguir con los cursos de la plataforma")
