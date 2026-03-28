estudiante=input("¿eres estudiante? (si/no)")
total=int(input("ingrese total de tu compra en pesos"))
if estudiante=="si" or total >= "2000000":
    print("descuento aplicado del 15%!")

else:
    print("Sin descuento. Total: $', total ")
