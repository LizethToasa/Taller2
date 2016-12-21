import turtle
t=turtle.Pen()

tam=int(input("Ingrese el tamaño: "))
def cuadrado(n):
    for x in range(0,5):
        t.forward(tam)
        t.left(90)
cuadrado(tam)
