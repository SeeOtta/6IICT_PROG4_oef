""" Niveau 1 """
num_lijst = [ 100, 101, 0, "103", 104 ]
try:
    index = int( input( "Geef een index: " ) )
except TypeError:
    print("geef een correct en geheel getal op")
except IndexError:
    print("opgegeven getal is te groot")
except ZeroDivisionError:
    print("Je kan niet delen door 0.")
except ValueError:
    print("geef een geheel getal")
else:
    try:
        print( f"100 / {num_lijst[index]} = {100/num_lijst[index]}" ) 
    except TypeError:
        print("geef een correct en geheel getal op")
    except IndexError:
        print("opgegeven getal is te groot")
    except ZeroDivisionError:
        print("Je kan niet delen door 0.")
    except ValueError:
        print("geef een geheel getal")

# """ Niveau 3 (haal uit commentaar) """
finally:
    print( "Het programma is beëindigd." )