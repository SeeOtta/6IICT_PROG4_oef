""" Niveau 1 """
from functools import total_ordering


puntenlijst = [
    ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], # 1 punt
    ["D", "G"],                                         # 2 punten
    ["B", "C", "M", "P"],                               # 3 punten
    ["F", "H", "V", "W", "Y"],                          # 4 punten
    ["K"],                                              # 5 punten
    ["J", "X"],                                         # 6 punten
    ["Q","Z"]                                           # 7 punten
]
def scrabble():
    dic = {}
    for index,letters in enumerate(puntenlijst):
        for letter in letters:
            value = index+1
            dic[letter] = value
    dic = dict(sorted(dic.items()))
    return dic
print(scrabble())
""" Niveau 2"""
puntenlijst_en = [
    ["A", "E", "I", "O", "U", "L", "N", "S", "T"],      # 1 punt
    ["D", "G", "K"],                                    # 2 punten
    ["B", "M", "P", "Q", "R"],                          # 3 punten
    ["F", "H", "V", "W", "Y"],                          # 4 punten
    [],                                                 # 5 punten
    ["J", "X"],                                         # 6 punten
    ["C","Z"]                                           # 7 punten
]