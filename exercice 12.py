print("---------------------")


try:
    answer = 10/0
    number = int(input("enter a number:"))
    print(number)
except ZeroDivisionError as err:
 print(err)
except ValueError:
    print("invalid input")
print("---------------------")
'''
dsfsf

'''
#this progeram is cool.

print("comments are fun")

print("---------------------")

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("enter phrase")))


print("---------------------")