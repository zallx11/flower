import turtle as tr

layar = tr.Screen()

tr.setup(800, 800)
layar.bgcolor('#262626')
tr.pencolor('#540d6e')
tr.speed(0)
tr.tracer(100)
tr.pensize(1)

warna_bunga = ("#3B22C7", '#3B22C7', '#3B22C7', '#3B22C7')

for i in range(3):
    for n in range(400):
        tr.color(warna_bunga[n % 4])
        tr.circle(190 - n / 2, 90)
        tr.left(90)
        tr.circle(190 - n / 2, 90)
        tr.color(warna_bunga[n % 4])
        
    tr.left(30)

layar.exitonclick()