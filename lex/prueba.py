
instrucciones = ["SAY TEXT" , "DRIVE" , "MOVE 10"]

prueba = []

def leer_instrucciones(lista):
    for i in instrucciones:
        prueba.append(i.split(' '))
    for x in prueba:
        try:
            print(x[0],x[1])
        except IndexError:
            print(x[0])



leer_instrucciones(prueba)