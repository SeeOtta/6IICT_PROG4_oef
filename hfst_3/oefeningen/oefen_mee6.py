fruit_lijst = ["Appel", "Banaan", "Kers"]

try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )
except IndexError:
    print( "Te groot getal opgegeven" )  
except ValueError:
    print("De opgegeven waarde is niet correct.")
except ZeroDivisionError:
    print("0 is geen geldig gegeven")

print("Programma klaar")  
