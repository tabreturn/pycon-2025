# setup
size(500, 500)           # canvas size
background('#FFFFFF')    # background colour
cx = width / 2           # canvas horizontal centre
cy = height / 2          # canvas vertical centre

stroke_weight(5)         # set outline to 5-pixels-wide

# draw rectangle
stroke('#FF0000')        # set outline to red
fill('#00FF00')          # set fill to green
rect(100, 50, 120, 340)  # draw rectangle

# draw circle
no_fill()                # set fill to none
stroke('#0000FF')        # set outline to blue
circle(cx, cy, 200)      # draw circle

# labels
no_stroke()
text_size(15)
fill('#F00')
text("(100, 50)", 85, 35)
circle(100, 50, 15)
text("height: 340", 20, 220)
text("width: 120", 123, 415)
fill('#00F')
text("(cx, cy)", 238, 232)
circle(250, 250, 15)
text("diameter: 200", 355, 300)
