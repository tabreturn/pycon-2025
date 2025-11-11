size(500, 500)
background('#FFFFFF')
rotate(0.1)  # rotates the entire drawing space by ~6 degrees

line_1_x = 300
line_2_x = 400

# draw two grey lines
stroke_weight(5)
stroke('#999999') # grey
line(300, 0, line_1_x, height)
line(400, 0, line_2_x, height)
no_stroke()

# loop for blue dots
# INSERT MISSING CODE HERE
for i in range(20, 800, 20):
    fill('#0000FF') # blue
    circle(i, 125, 15)

# loop for red dots
# INSERT MISSING CODE HERE
for i in range(20, 800, 20):
    if i >= line_1_x:
        break
    fill('#FF0000') # red
    circle(i, 250, 15)

# loop for green dots
# INSERT MISSING CODE HERE
for i in range(20, 800, 20):
    if i >= line_1_x and i <= line_2_x:
        continue
    fill('#00FF00') # green
    circle(i, 375, 15)
