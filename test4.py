'''x = ["hola", 4, 5]

print(type(x))
print(id(x))

x[0]= "agur"
print(id(x))    


inflacion = 3.765

print(id(inflacion))

inflacion= 3.7

print(id(inflacion))    


a = 4
b = 4.32
c = 3

suma =0

if isinstance(a, int):
    suma += a        #suma = suma + a
if isinstance(b, int):
    suma += b
if isinstance(c, int):
    suma += c

print(suma)                 

a = 4
b = 4.32
c = 3
lista_comprobacion = [a, b, c]
suma = 0


for i in lista_comprobacion:
    if isinstance (i, int):
        suma += i

print("La suma de los números enteros es:", suma)   

i = 0
while i < 10:    
    print("hola" + str(i))
    i = i +1
print ("END")                                               


i = 50
while i<=100:
    i = i+1
   
    print(i)                                            

i = 5
while i<=20:
    i = i+1
    if i !=12:
        print(i)
    else:
        print(i)                                    


while True:
  pwd1 = input("Introducir tu contraseña: ")
  pwd2 = input("Introducir de nuevo tu contraseña: ")
  if pwd1 == pwd2:
    print("Muy bien. Las contraseñas coinciden.")
    break
    print("Las contrseñas no coinciden. Hacerlo de nuevo.")   

x= 0
while x != 'q':
    print('numero')
    x = x + float(x)
    x = input("introducir numero, 'q' para quit")                   


total = 0
while total < 100:
    num = int(input("Enter a number: "))
    total = total + num
    print("The total is: ", total)                         

i = 100
while i >= 50:
    print(f"i con valor {i} es mayor o igual que 50")
    i = i - 1                                            '''



#valor_bancario = input (int("introduce el valor de tu transaccion bancaria: "))

#print(valor_bancario)

total = 0
while total < 1000:
    if sum == int(input("Enter a number: ")):
         total = total + sum
    if sum == float(input("Enter a number: ")):
         total = total + num

    print("The total is: ", total)





    

    


  



