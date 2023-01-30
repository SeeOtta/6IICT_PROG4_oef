import tkinter as tk                                        #importeer tkinter in var tk

venster = tk.Tk()                                           #venster wordt een functie

label = tk.Label(master=venster, text="Geef naam op: ", width=15, height=2,  #maak een venster waarin staat "Geef naam op" die 15 breed is en 2 hoog is met een zwarte achtergrond
                 highlightthickness=2, highlightbackground="black")
label.grid(row=0, column=0)                                                  #zet dit op de eerste plaats in de grid

veld = tk.Entry(master=venster, width=50, fg="red")                          #maak een blok aan van 50 breed met foreground kleur rood
veld.grid(row=0, column=1)                                                   #zet dit op tweede plaats in de grid 

def display_naam():                                                          #maak functie display_name
    tekst = f"Hallo, mijn naam is {veld.get()}!"                             #print dit
    label_naam = tk.Label(master=venster, text=tekst, width=50, height=2)    #maak dit tekst vak 50 breed en 2 groot
    label_naam.grid(row=2, column=0, columnspan=2)                           #zet dit onder de eerste en tweede plaats

knop = tk.Button(master=venster, command=display_naam, text="Voer in!", width=50) #maak een knop die de functie display_naam uitvoert met de tekst "voer in"
knop.grid(row=1, column=0, columnspan=2)                                     #zet deze knop boven de functie blok plaats

venster.mainloop()                        #toon het venster
