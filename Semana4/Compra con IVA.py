#Algoritmo
#Pedir nombre del producto
#Pedir precio unitario
#Pedir cantidad
#Calcular subtotal = precio * cantidad
#Calcular IVA del 19%
#Calcular total = subtotal + IVA
#Si total > 50000 aplica descuento especial (True)
#Si no, no aplica (False)

#Pseudocodigo
#inicio
#leer nombre
#leer precio
#leer cantidad
#subtotal = precio*cantidad
#iva = subtotal*0.19
#total = subtotal+iva
#si total >50000
#escribir True
#si no
#escribir False

nombre=input("Digite el nombre del producto: ")
precio=int(input("Digite el precio: "))
cantidad=int(input("Digite la cantidad: "))

subtotal=precio*cantidad
iva=subtotal*0.19
total=subtotal+iva

print("Producto:",nombre)
print("Precio:",precio)
print("Cantidad:",cantidad)
print("Subtotal:",subtotal)
print("IVA (19%):",iva)
print("Total:",total)

if total>50000:
    print("Aplica descuento especial?: True")
else:
    print("Aplica descuento especial?: False")
