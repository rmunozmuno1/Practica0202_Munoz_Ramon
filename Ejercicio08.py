###Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
Precio = input('Escriba el precio del producto con dos decimales')
separar = Precio.split('.')
euros = separar[0]
centimos = separar[1]
print(f"el precio tiene {euros} euros y {centimos} céntimos")
