# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Vraag om de lievelingskleur van de gebruiker (rood, groen of blauw)
kleur = input("Wat is je favoriete kleur? ")

# Maak een lege GUI aan.
venster = tk.Tk()

# TODO: vertaal input van gebruiker naar het Engels
# TODO: maak functie aan die het label in de ingegeven kleur laat zien.
label = tk.Label(master=venster, text="JOJOJOJOJOJOJOJOJOJOJO")
def knop_klik():
    if kleur == "paars":
        labeltje = tk.Label(master=venster, text=f"{kleur} is mijn favoriete kleur", foreground='purple')
        labeltje.pack()

knop = tk.Button(master=venster, text="he he he jup!", command= knop_klik)
knop.pack()

# Maak de GUI zichtbaar op de computer.
venster.mainloop()