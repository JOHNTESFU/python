print("---------------------")

friends =["jim", "karen", "wolf"]

for index in range(5):
    if index ==0:
        print("first iteration")
    else:
        print("not first")



print("-----------------")

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,4))

print(2**3)




print("------------------------")
friends =["jim", "karen", "wolf"]

for index in range(len(friends)):
    print (friends[index])
    friends[2]