# Este programa creara una serie de valores de transacciones bancarias de un usuario, las cuales se mostraran en un informe, detallando tambien la media de las mismas
'''
a = 20
b = -50
c = 30
d = -15.89
lista_comprobacion = [a, b, c, d]
suma = 0


for i in lista_comprobacion:
    if isinstance (i, int):
        suma += i
    if isinstance (i, float):
        suma += i

media = suma / len(lista_comprobacion)
print("La suma de las transacciones bancarias:", suma)
print("La media de las transacciones bancarias:", media)    '''



c = "si"
while c != "no":
         x = 0
    if num = int(input("Enter a number: ")):
        x == x + num
    if num = float(input("Enter a number: ")):
        x == x + num

    print("El total es: ", total)
    x = input("Quieres continuar? (si, no)")

x = [4, 6, 3, 8.5, 8]

suma = 0
for i in x:
    suma = suma + i

media = suma / len(x)

print("La media de las transacciones bancarias:", media)
