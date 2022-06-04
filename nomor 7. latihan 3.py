line = int(input("masukkan usia ="))

total = 0
while line!= "":
    umur = int(line)
    
    if umur <= 2 :
        total = total + 0
    elif umur >= 3 and umur <= 12:
        total = total + 14
    elif umur >= 13 and umur <= 64:
        total = total + 23
    else :
        total = total + 18
    n = input( "masukkan usia =")
print ("biaya masuk adalah ${:.2f}".format(total))