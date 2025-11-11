size(500, 500)
background('#FFFFFF')

# INSERT MISSING CODE HERE
no_fill()
stroke_weight(5)

stroke_color = "#FF0000"

for i in range(1, 10):
    for j in range(1, 10):
        stroke(stroke_color)
        circle(i * 50, j * 50, 20)
        if stroke_color == "#FF0000":
            stroke_color = "#00FF00"
        else:
            stroke_color = "#FF0000"

for i in range(1, 5):
    stroke('#000000')
    circle(width / 2, height / 2, i * 100)
# INSERT MISSING CODE HERE
