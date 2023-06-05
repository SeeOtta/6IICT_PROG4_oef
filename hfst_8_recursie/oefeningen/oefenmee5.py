""" Niveau 1: los sommatie recursief op """
def draaiom(string):
    if len(string) <= 1:
        return string
    else:
        return draaiom(string[1:]) + string[0]

print(draaiom("Hallo"))       # ollaH
print(draaiom("Dag"))         # gaD
print(draaiom("f"))           # f
print(draaiom("Iedereen"))    # neeredeI


""" Niveau 2: los sommatie met while-loops op """
def draaiom(string):
    reversed_string = ""
    index = len(string) - 1
    
    while index >= 0:
        reversed_string += string[index]
        index -= 1
    
    return reversed_string

print(draaiom("Hallo"))       # ollaH
print(draaiom("Dag"))         # gaD
print(draaiom("f"))           # f
print(draaiom("Iedereen"))    # neeredeI
