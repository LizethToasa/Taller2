import turtle
t=turtle.Pen()

n=int(input("Ingrese el numero de lados: "))
for x in range(n):
    t.forward(108)
    t.left((n-2)*180/n)
    t.left((n-2)*180/n)
