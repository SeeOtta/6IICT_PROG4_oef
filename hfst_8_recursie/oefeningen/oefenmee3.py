""" Bepaal de faculteit van een getal met behulp van een while-loop. """
number = 5
factorial = 1
counter = 1

while counter <= number:
    factorial *= counter
    counter += 1

print("De faculteit van", number, "is", factorial)
