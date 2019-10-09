def  say_hi(name, age):
     print("hello " + name, "you are " + str(age))

say_hi("john" ,  33)
say_hi("mike" , 23)

print("--------------------------")

def cube(num):
    return num*num*num

result= cube(10*10)
print(result)


print("----------------------------")
is_male = True
is_tall = True

if is_male and is_tall:
    print("you are a tall male")

elif is_male and not(is_tall):
    print("you are a short male")

elif not (is_male) and is_tall:
    print("you are a not a male but are tall")

else:
    print("you are not a male and not tall")


print("---------------------")

def max_num(num1, num2,num3) :
    if num1 >= num2 and num1>=num3:
        return num1
    elif num2>= num1 and num2 >=num3:
        return num2
    else:
        return num3

print(max_num(3,3,5))


print("---------------")




