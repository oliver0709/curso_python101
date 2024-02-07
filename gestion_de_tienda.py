


message = int(input("Bienvenidos a mi tienda. Para comprar nuestros productos introduce una tecla, siendo 1 manzanas, 2 zumos y 3 leche  "))

productos = [{"manzanas":10}, {"zumos":15}, {"leche":20}]

'''for i in productos:
    print(i + " vale 20 eur")    '''

if message ==1:
    print("quieres comprar manzanas")
    productos[0]
    #pass
    
elif message ==2:
    print("quieres comprar zumos")
    productos[1]
   #pass
elif message ==3:
    print("quieres comprar leche")
    productos[2]
    #pass
else: print("no tenemos esa opcion")


'''
elif accion==2:
    compra= input("que quieres comprar")
    if compra in listaderopa:
        #pedir al usuario dinero
        dinero= float(input("cuesta20 euros. Cuanto tienes"))
        print(f"gracias, devolvemos ${dinero-20:.2f}")
else: print("no tenemos eso")   '''




