from random import randint

bet = randint(100, 999)

print(f"The winning number is {bet}.")

while True:
    user = (input("Hatag Swertres Number (three-digit number) STRAIGHT/SCRAMBLE numbers: "))
    if user.isdigit() and len(user) == 3:
        break
    else:
        print("Bisan Tulo Ka Number Ra.")

if int(user) == bet:
    print("Congratulations! Daug ka sa Swertres.")
elif sorted(user) == sorted(str(bet)):
    print("Congratulations! Daug ka sa RAMBLE.")
else:
    print(f"Sorry, pildi ka. The winning number was {bet}.")