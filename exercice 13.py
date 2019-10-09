
print("-----------------------")
ww_file = open("ww1.txt", "a")
ww_file.write("\nCrack")

ww_file.close()





print("-----------------------")
ww_file = open("ww.txt", "r")
for ww in ww_file.readlines():
    print(ww)

ww_file.close()