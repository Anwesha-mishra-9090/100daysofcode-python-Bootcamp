print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

# Initialize bill
bill = 0

# Determine base price based on size
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("You have chosen an invalid size.")
    exit()  # Exit if invalid size is provided

# Add cost for pepperoni
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

# Add cost for extra cheese
if extra_cheese == "y":
    bill += 1

# Output the final bill amount
print(f"Your final bill is: ${bill}.")
