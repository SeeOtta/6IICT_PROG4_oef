""" Schrijf een recursieve functie die controleert of een lijst geordend is. """

def geordend(lst):
    if len(lst) <= 1:
        return True
    else:
        return lst[0] <= lst[1] and geordend(lst[1:])

print(geordend([1, 2, 3, 4]))    # True
print(geordend([5, 2, 8, 4]))    # False
print(geordend([9]))             # True
print(geordend([0, 1, 2, 4, 3, 5]))  # False