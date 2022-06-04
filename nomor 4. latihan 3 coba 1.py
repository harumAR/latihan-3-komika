
wavelength = int(input("Panjang gelombang cahaya :"))
if wavelength>=380 and wavelength<450:
    print("spektrum yang terlihat adalah Violet")
elif wavelength>=450 and wavelength<495:
    print("spektrum yang terlihat adalah Blue")
elif(wavelength>=495 and wavelength<570):
    print("spektrum yang terlihat adalah Green")
elif(wavelength>=570 and wavelength<590):
   print("spektrum yang terlihat adalah Yellow")
elif(wavelength>=590 and wavelength<620):
   print("spektrum yang terlihat adalah Orange")
elif(wavelength>=620 and wavelength<750):
   print("spektrum yang terlihat adalah Red")
else:
   print("Panjang gelombang yang dimasukkan berada di luar spektrum yang terlihat")