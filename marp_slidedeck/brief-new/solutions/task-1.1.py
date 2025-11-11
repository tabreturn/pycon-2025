# setup
size(500, 500)           # canvas size
background('#FFFFFF')    # background colour
cx = width / 2           # canvas horizontal centre
cy = height / 2          # canvas vertical centre

i = 1

while i < 10:
    no_fill()
    stroke_weight(5)
    # INSERT MISSING CODE HERE
    stroke('#FF0000')
    circle(cx, cy, i * 50)
    # INSERT MISSING CODE HERE
    i += 1
