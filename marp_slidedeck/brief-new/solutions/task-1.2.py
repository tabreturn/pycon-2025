# setup
size(500, 500)           # canvas size
background('#FFFFFF')    # background colour
cx = width / 2           # canvas horizontal centre
cy = height / 2          # canvas vertical centre
no_fill()                # set fill to none
stroke_weight(5)         # set outline to 5-pixels-wide

# INSERT MISSING CODE HERE
for i in range(1, 10):
    if i % 2:
        stroke('#00FF00')
    else:
        stroke('#0000FF')
    circle(cx, cy, i * 50)

no_stroke()
fill('#FFFFFF')
rect(0, 200, 500, 100)
# INSERT MISSING CODE HERE
