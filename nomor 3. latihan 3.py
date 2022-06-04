magnitude = float(input("Kekuatan gempa (Magnitude) ="))

if (magnitude <= 2.0):
    print("Gempa tersebut adalah gempa jenis micro")
elif (magnitude <= 3.0):
    print("Gempa tersebut adalah gempa jenis very minor")
elif (magnitude <= 4.0):
    print("Gempa tersebut adalah gempa jenis minor")
elif (magnitude <= 5.0):
    print("Gempa tersebut adalah gempa jenis light")
elif (magnitude <= 6.0):
    print("Gempa tersebut adalah gempa jenis moderate")
elif (magnitude <= 7.0):
    print("Gempa tersebut adalah gempa jenis strong")
elif (magnitude <= 8.0):
    print("Gempa tersebut adalah gempa jenis major")
elif (magnitude <= 10.0):
    print("Gempa tersebut adalah gempa jenis great")
elif (magnitude >= 10.0):
    print("Gempa tersebut adalah gempa jenis meteoric")