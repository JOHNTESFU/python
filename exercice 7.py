print("-------------------------------------")
print("Hello User")
first = input("Type 'Join' if u want to join our club, \nType 'user' if you have joined "
              "and \n'Exit' if you want to leave:_ ")
first2 = (first.upper())

if first2 == "JOIN":

    print("-------------------------------------")
    print("-------------Welcome-----------------")
    print("Please fill in the required information to join our club")

    first_name = input("Enter your First name:_ ")
    last_name = input("Enter your Last name :_ ")
    place = input("Where Do You Currently Live:_ ")

    age = str(input("Enter your age:_"))

    if age > "100":
        age = str(input("Enter your real age:_"))

    Un_encrypted_Password = input("Enter in a 6 Character Password:_ ")

    if len(Un_encrypted_Password) < 6:
        print("Please Enter a 6+ Character Password")
        Un_encrypted_Password = input("Enter in a Password:_ ")


    def translate(password):
        translation = ""
        for letter in password:

            # BELOW HERE ARE LETTER ENCRYPTION KEYS
            # abcdefghijklmnopqrstuvwxyz

            if letter.upper() in "A":
                translation = translation + "!"         # vowel A
            if letter.upper() in "B":
                translation = translation + "1"
            if letter.upper() in "C":
                translation = translation + "<"
            if letter.upper() in "D":
                translation = translation + "2"
            if letter.upper() in "E":
                translation = translation + "@"         # vowel E
            if letter.upper() in "F":
                translation = translation + "3"
            if letter.upper() in "G":
                translation = translation + ">"
            if letter.upper() in "H":
                translation = translation + "4"
            if letter.upper() in "I":
                translation = translation + "#"         # vowel I
            if letter.upper() in "J":
                translation = translation + "5"
            if letter.upper() in "K":
                translation = translation + "="
            if letter.upper() in "L":
                translation = translation + "("
            if letter.upper() in "M":
                translation = translation + ")"
            if letter.upper() in "N":
                translation = translation + "6"
            if letter.upper() in "O":
                translation = translation + "$"         # vowel O
            if letter.upper() in "P":
                translation = translation + "7"
            if letter.upper() in "Q":
                translation = translation + "+"
            if letter.upper() in "R":
                translation = translation + "^"
            if letter.upper() in "S":
                translation = translation + "*"
            if letter.upper() in "T":
                translation = translation + "8"
            if letter.upper() in "U":
                translation = translation + "%"         # vowel U
            if letter.upper() in "V":
                translation = translation + "9"
            if letter.upper() in "W":
                translation = translation + "&"
            if letter.upper() in "X":
                translation = translation + "%"
            if letter.upper() in "Y":
                translation = translation + ":"
            if letter.upper() in "Z":
                translation = translation + "0"

            # below are number encryption keys
            # 1234567890

            if letter in "0":
                translation = translation + "A"
            if letter in "1":
                translation = translation + "B"
            if letter in "2":
                translation = translation + "C"
            if letter in "3":
                translation = translation + "D"
            if letter in "4":
                translation = translation + "E"
            if letter in "5":
                translation = translation + "F"
            if letter in "6":
                translation = translation + "Z"
            if letter in "7":
                translation = translation + "Y"
            if letter in "8":
                translation = translation + "X"
            if letter in "9":
                translation = translation + "W"
            else:
                translation = translation
        return translation

    Un_encrypted_identification2 = str(Un_encrypted_Password)
    encrypted_password = (translate(Un_encrypted_identification2))

    print("-------------------------------------")
    print("Welcome Thank you for Choosing us")
    print("HI your name is " + first_name + " " + last_name)
    print("You are " + age + " years old.")
    print("And currently living in " + place + ".")

    if age < "18":
        print("And you are under 18 years old")
        print("you can not join our club")
        ww_file = open("ww1.txt", "a")
        ww_file.write("\n\nDeclined")
        ww_file = open("exercice 14.py", "a")
        ww_file.write("\n\nDeclined")
        ww_file.close()

    elif age >= "35":
        print("Sorry, You have to be older than 17 and younger than 35 to join.")
        ww_file = open("ww1.txt", "a")
        ww_file.write("\n\nDeclined")
        ww_file = open("exercice 14.py", "a")
        ww_file.write("\n\nDeclined")
        ww_file.close()
    else:
        print("*** You are an adult.   ***")
        print("***You can join our club***")
        print("Thank you for coming ")
        ww_file = open("ww1.txt", "a")
        ww_file.write("\n\nAccepted")
        ww_file = open("exercice 14.py", "a")
        ww_file.write("\n\nAccepted")
        ww_file.close()

    import random

    class ID:
        def number(self):
            a = random.randint(1000000, 9999999)
            return a
    ID = ID()
    identification = ID.number()

    def translate(identifications):
        translation = ""
        for letter in identifications:
            if letter in "1":
                translation = translation + "M"
            if letter in "2":
                translation = translation + "o"
            if letter in "3":
                translation = translation + "Q"
            if letter in "4":
                translation = translation + "s"
            if letter in "5":
                translation = translation + "U"
            if letter in "6":
                translation = translation + "w"
            if letter in "7":
                translation = translation + "Y"
            if letter in "8":
                translation = translation + "a"
            if letter in "9":
                translation = translation + "C"
            if letter in "0":
                translation = translation + "e"
            else:
                translation = translation
        return translation
    Un_encrypted_identification = str(identification)
    translated_ID = (translate(Un_encrypted_identification))

    print("Here is Your Personal ID: " + Un_encrypted_identification + ".")
    ww_file = open("ex15.py", "a")
    ww_file.write(translated_ID + "=('" + first_name + "')")
    ww_file.close()
    # #23jfsdha = ("name of user")
    # asewYeM = ('das
    ww_file = open("exercice 14.py", "a")
    ww_file.write(f"\nIdentification Number : #{Un_encrypted_identification}")
    ww_file.write(f"\nIdentification Number ENC: #{translated_ID}")
    ww_file.write(f"\nFirst Name: {first_name}")
    ww_file.write(f"\nSecond Name: {last_name}")
    ww_file.write(f"\nAge: {age}")
    ww_file.write(f"\nPlace Living: {place}")
    ww_file.write(f"\nPassword: {Un_encrypted_Password}")
    ww_file.write(f"\nPassword ENC: {encrypted_password}")
    ww_file.close()

    ww_file = open("ww1.txt", "a")
    ww_file.write(f"\nIdentification Number ENC: #{translated_ID}")
    ww_file.write(f"\nFirst Name: {first_name}")
    ww_file.write(first_name)
    ww_file.write(f"\nSecond Name: {last_name}")
    ww_file.write(f"\nAge: {age}")
    ww_file.write(f"\nPlace Living: {place}")
    ww_file.write(f"\nPassword ENC: {encrypted_password}")
    ww_file.close()
    '''
    #writing data on to the exercice 7 data only user names
    ww_file = open("exercice 7 data.py", "a")
    ww_file.write(f"\n'First Name': '{first_name}',")
    ww_file.close()

    # this is the username dictionary
    User_name={
        "John": "123446",
        }
    User_name[first_name] = identification

    print(User_name.get(first_name))
    
    print(User_name)
    '''

elif first2 == "USER":

    print("Welcome Back")

    identification_number = input("Enter Identification Number To Log In:_ ")

    place_conversions = {
        "0947505599": "John",
        "0911385836": "Sami",
        "0911217858": "Gete",
         }

    IDD = (place_conversions.get(identification_number, "Sorry can't find the Identification Number you entered."))

    print("Welcome " + IDD)

elif first2 == "EXIT":
    print("thank you for coming")

elif first2 == "DEV.DEVELOPER":
    print("Welcome To The Developers Section")

    command = input("Type in a Command:_")
    command1 = (command.upper())
    ww_file = open("ww1.txt", "r")
    try:
        if command1 == "PRINT.USER":
            print(ww_file.read())
            print("-------------------------------------")
        ww_file = open("ww1.txt", "a")
        if command1 == "WRITE.NOTE":
            note = input("Write Notes:_")
            ww_file.write(f"\n#NOTES: {note}")
            print("-------------------------------------")
        if command1 == "HELP":
            print("Command Library \nPRINT.USER \nWRITE.NOTE")

    except:
        print("PLEASE FILL IN A VALID COMMAND")

    ww_file.close()

else:
    print("PLEASE FILL IN A VALID COMMAND")

print("-------------------------------------")
