import tkinter as tk
from functools import partial # Importeer de functie partial!

venster = tk.Tk()

""" Slechts 1 functie nodig, deze wordt gelinkt aan alle knoppen. 
    Deze functie heeft 1 parameter: getal """
def knop_ingedrukt(getal): 
    global totaal
    totaal+=getal
    veld.delete(0, tk.END)
    veld.insert(0, totaal)

""" Inputveld voor totaal """
totaal = 0
veld = tk.Entry(master=venster, font=("Helvetica", 15), bg="white", borderwidth = 5)
veld.grid(row=0,column=0, columnspan=3)

""" Knop 1: gelinkt aan knop1_ingedrukt. 
    Dit is de functie knop_ingedrukt met het argument 1 eraan toegevoegd."""
knop1_ingedrukt = partial(knop_ingedrukt, 1)
knop_1 = tk.Button(master=venster, width=20, command=knop1_ingedrukt , text="1")
knop_1.grid(row=1, column=0, padx=2, pady=2)

""" Knop 2: gelinkt aan knop2_ingedrukt. 
    Dit is de functie knop_ingedrukt met het argument 2 eraan toegevoegd."""
knop2_ingedrukt = partial(knop_ingedrukt, 2)
knop_2 = tk.Button(master=venster, width=20, command=knop2_ingedrukt , text="2")
knop_2.grid(row=1, column=1, padx=2, pady=2)


knop3_ingedrukt = partial(knop_ingedrukt, 3)
knop_3 = tk.Button(master=venster, width=20, command=knop3_ingedrukt, text="3")
knop_3.grid(row=1, column=2, padx=2, pady=2)


knop4_ingedrukt = partial(knop_ingedrukt, 4)
knop_4 = tk.Button(master=venster, width=20, command=knop4_ingedrukt, text="4")
knop_4.grid(row=2, column=0, padx=2, pady=2)


knop5_ingedrukt = partial(knop_ingedrukt, 5)
knop_5 = tk.Button(master=venster, width=20, command=knop5_ingedrukt, text="5")
knop_5.grid(row=2, column=1, padx=2, pady=2)


knop6_ingedrukt = partial(knop_ingedrukt, 6)
knop_6 = tk.Button(master=venster, width=20, command=knop6_ingedrukt, text="6")
knop_6.grid(row=2, column=2, padx=2, pady=2)



knop7_ingedrukt = partial(knop_ingedrukt, 7)
knop_7 = tk.Button(master=venster, width=20, command=knop7_ingedrukt, text="7")
knop_7.grid(row=3, column=0, padx=2, pady=2)


knop8_ingedrukt = partial(knop_ingedrukt, 8)
knop_8 = tk.Button(master=venster, width=20, command=knop8_ingedrukt, text="8")
knop_8.grid(row=3, column=1, padx=2, pady=2)


knop9_ingedrukt = partial(knop_ingedrukt, 9)
knop_9 = tk.Button(master=venster, width=20, command=knop9_ingedrukt, text="9")
knop_9.grid(row=3, column=2, padx=2, pady=2)



venster.mainloop()