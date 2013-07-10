#-*- coding: utf-8 -*-
from PIL import Image, ImageDraw

coordinate = {
    "x": [0, 0],
    0: [-100, 0],
    1: [70, 4],
    2: [210, 4],
    3: [350, 4],
    4: [490, 4]
}
first_pos = {
    1: ()
}


# создаем апликатуру
def aplicatura(spisok):
    # Рисуем палец
    finger = Image.new("RGBA", (35, 35), (0, 0, 0, 0))
    draw = ImageDraw.Draw(finger)
    draw.ellipse((0, 0, 35, 35), fill="red", outline="red")

    # рисуем бэре
    bere = Image.new("RGBA", (75, 245), (0, 0, 0, 0))
    draw = ImageDraw.Draw(bere)
    draw.ellipse((25, 0, 50, 245), fill="red", outline="red")

    # рисуем cross
    cross = Image.new("RGBA", (35, 35), (0, 0, 0, 0))
    draw = ImageDraw.Draw(cross)
    draw.line((0, 0, 35, 35), fill="red", width=7)
    draw.line((35, 0, 0, 35), fill="red", width=7)

    aplic = Image.open("Grif.png")
    draw = ImageDraw.Draw(aplic)
    spisok = list(spisok)
    min_lad = min(spisok)
    for i, lad in enumerate(spisok):
        lad -= (min_lad - 1)
        x = coordinate[lad][0]
        y = coordinate[lad][1] + 203.5 - i * 41.5
        if lad == 'x':
            draw.bitmap((x, y), cross, fill="red")
        else:
            draw.bitmap((x, y), finger, fill="red")
        aplic.save("aplicatura.png", "PNG")
    del draw
        # aplic.save(sys.stdout, "JPEG")

aplicatura(spisok=(2, 3, 2, 4, 5, 3))
