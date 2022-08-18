#Level 3
""" Un sitio web requiere que los usuarios ingresen el nombre de usuario
y la contraseña para registrarse. Escriba un programa para verificar la
validez de la contraseña ingresada por los usuarios.

Los siguientes son los criterios para verificar la contraseña:
1. Al menos 1 letra entre [a-z]
2. Al menos 1 número entre [0-9]
1. Al menos 1 letra entre [A-Z]
3. Al menos 1 carácter de [$#@]
4. Longitud mínima de la contraseña de transacción: 6
5. Longitud máxima de la contraseña de transacción: 12
Su programa debe aceptar una secuencia de contraseñas separadas por comas
y las verificará de acuerdo con los criterios anteriores. Las contraseñas
que coincidan con los criterios deben imprimirse, cada una separada por una coma.

Ejemplo
Si se dan las siguientes contraseñas como entrada al programa:
ABd1234@1,a F1#,2w3E*,2We3345
Entonces, la salida del programa debe ser:
ABd1234@1

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer
que se trata de una entrada de consola. """

#solution
import re
value = []
items = [x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(','.join(value))

""" if len(p) >= 6 and len(p) <= 12:
if any(char.isdigit() for char in p):
if any(char.isupper() for char in p):
if any(char.islower() for char in p):
if any(char in '$#@' for char in p):
value.append(p) """

#Geovanny E. Villa Sánchez
#KikeViS