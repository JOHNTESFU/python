print("---------------------")

secret_word = "Johnny"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guesses, you lose!")
else:
    print("you win!")

print("------------------")

i = 1
while i <= 10:
    print(i)
    i += 1

print("done with loop")




print("-------------------")

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
}
print(monthConversions.get("Ap", "Not a valid key"))


print("---------------------------")
num1 = float(input("enter first number: "))
op = input("enter operator: ")
num2 = float(input("enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-" :
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")

print("---------------------------")

