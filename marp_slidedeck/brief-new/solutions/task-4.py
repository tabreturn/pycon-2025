size(500, 500)
background('#FFFFFF')
no_stroke()
fill('#000000')

tile_size = 25

# single blue tile demonstration
fill('#0000FF')
triangle(
    tile_size, 0,          # point 1 x-y coord
    tile_size, tile_size,  # point 2 x-y coord
    0, tile_size           # point 3 x-y coord
)

for i in range(10):
    print(random())        # ten random values 

# ... INSERT MISSING CODE HERE ...

for col in range(0, 500, tile_size):
    for row in range(0, 500, tile_size):
        r = random()
        if r >= 0.75:
            fill('#0000FF') # blue
            triangle(col + tile_size, row,
                     col + tile_size, row + tile_size,
                     col, row + tile_size)
        elif r >= 0.5:
            fill('#FF0000') # red
            triangle(col, row,
                     col, row + tile_size,
                     col + tile_size, row + tile_size)
        elif r >= 0.25:
            fill('#00FF00') # green
            triangle(col, row,
                     col, row + tile_size,
                     col + tile_size, row)
        else:
            fill('#000000') # black
            triangle(col, row,
                     col + tile_size, row,
                     col + tile_size, row + tile_size)
