from PIL import Image

def create_image(image, filename):
    """ Creates an image from a coordinate list """
    img = Image.new('RGB', (256,256), "white")
    pixels = img.load()

    x = -1
    y = -1

    for stroke in image:
        for i in range(len(stroke[0])):
            if x != -1: 
                for point in get_line(stroke[0][i], stroke[1][i], x, y):
                    pixels[point[0],point[1]] = (0, 0, 0)
            pixels[stroke[0][i],stroke[1][i]] = (0, 0, 0)
            x = stroke[0][i]
            y = stroke[1][i]
        x = -1
        y = -1
    img.save(filename)

def get_line(x1, y1, x2, y2):
    """ Create a line using the given coordinates """
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    if rev:
        points.reverse()
    return points
