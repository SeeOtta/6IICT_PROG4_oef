from calendar import c


poll_talen = ["Lucas", "Maud", "Jan", "Dillan", 
              "Piet", "Joris"]

favorite_languages = {    
    "Jan": "python",    
    "Piet": "c",    
    "Joris": "ruby"}
for namen in poll_talen:
    if namen in favorite_languages:
        print(f"bedankt {namen} voor de deelname")
    else:
        print(f"zou {namen} kunnen deelnemen")
        antwoord = input(print("wat is je fav taal?"))
        if antwoord != '':
          favorite_languages[namen] = antwoord

print(favorite_languages)
