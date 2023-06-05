""" Niveau 1: los sommatie recursief op """

def sommatie(n):
    if n == 1:
        return 1
    else:
        return n + sommatie(n-1)

print(sommatie(1))   # 1
print(sommatie(2))   # 3
print(sommatie(3))   # 6
print(sommatie(4))   # 10
print(sommatie(5))   # 15
print(sommatie(100)) # 5050

""" Niveau 2: los sommatie met while-loops op """

def sommatie(n):
    total = 0
    counter = 1
    
    while counter <= n:
        total += counter
        counter += 1
    
    return total

print(sommatie(1))   # 1
print(sommatie(2))   # 3
print(sommatie(3))   # 6
print(sommatie(4))   # 10
print(sommatie(5))   # 15
print(sommatie(100)) # 5050
