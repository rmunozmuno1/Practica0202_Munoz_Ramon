#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extensión donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
print  ('Introduzca el prefijo de su telefono')
Telefono = input ('Numero completo')
diferenciar = Telefono.split('-')
Mostrar_Numero = diferenciar[1]
print (Mostrar_Numero)