print("Hello and welcome to Card Information Holder.")

print("Please enter your card information")
numCard = str(input("Card Number: "))
while len(numCard) != 16:
    print("Please enter a valid card number.")
    numCard = str(input("Card Number: "))
month, year = input("Expiration Date: ").split("/")
m = int(month)
y = int(year)
while (m > 12) or (y < 20):
    print("Please enter a valid date.")
    month, year = input("Expiration Date: ").split("/")
    m = int(month)
    y = int(year)
cvv = str(input("CVV Number: "))
while len(cvv) != 3:
    print("Please enter a valid CVV Number")
    cvv = str(input("CVV Number: "))
print("This is your card information")
print("Last four of card number: {}".format(numCard[-4:]))
print("Expiration Date: {}/{}".format(m, y))
print("CVV Number: {}".format(cvv))