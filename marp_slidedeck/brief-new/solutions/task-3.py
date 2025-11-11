size(800, 500)
background('#FFFFFF')
stroke('#000000')
stroke_weight(5)

# ... INSERT MISSING CODE HERE ...

# Left pattern
for i in range(28):
    line(50, 100 + i * 13,
         200, 50 + i * 13)

# Middle pattern
translate(325, 0)

distance = 28
for i in range(28):
    line(0, 20 + distance, 150, 65 + distance)
    distance *= 1.101

# Right pattern
translate(275, 0)

for i in range(28):
    if i % 2 > 0:
        line(0, 85 + 13 * i,
             75, 60 + 13 * i)
    else:
        line(75, 60 + 13 * i,
             150, 85 + 13 * i)