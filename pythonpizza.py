print("Welcome to Python Pizza Deliveries!")

bill = 0
size = input("What size pizza do you want? S, M or L: ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("you have chosen the wrong option.")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")


if pepperoni == "Y":
    pepperoni_size = input("What size of pepperoni do you want on pizza? S or L: ")
    if pepperoni_size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")