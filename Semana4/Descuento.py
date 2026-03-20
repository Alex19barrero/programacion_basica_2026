#Algoritmo
#Pedir valor del producto
#Si el valor es mayor >80.000 tiene descuento del 10%
#calcular 80.000*0.90
#Si el valor es menor a <80.000 no tiene descuento
#80.000 exacto no tiene descuento

#Pseudocodigo
#inicio
#leer valor del producto
#resultado producto>80.000*0.90
#escribir "tiene descuento del 10%"
#resultado <80.000
#escribir "no tiene descuento"

precio_producto=int(input("Digite el valor del producto"))
if precio_producto>80000:
    descuento=precio_producto*0.10
    precio_final=precio_producto-descuento
    print(f"tiene descuento del 10%:$",descuento)
    print(f"precio final:$",precio_final)
else:
    print("precio final:$",precio_producto,"(no aplica descuento)")
