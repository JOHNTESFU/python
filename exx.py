exx = input("here")
exx2 = input("here again")


ww_file = open("ww1.txt", "a")
ww_file.write(exx)
ww_file.write(f"\n{exx2}")
ww_file.close()

