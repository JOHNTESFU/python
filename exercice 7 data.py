IDD = input("write here")

import random

class ID:
    def number(self):
        a = random.randint(1000000, 9999999)
        return a
ID = ID()
identification = ID.number()

import array
ID = array.array('i',[1,2,3])
print(ID)
ID.extend([int(identification)])
print(ID)
print(identification)