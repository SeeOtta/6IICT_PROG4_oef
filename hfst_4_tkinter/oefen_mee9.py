import tkinter as tk

venster = tk.Tk()

label = tk.Label(master=venster, text="Welke website wil je bezoeken?", height=2)
label.grid(row=0, column=0, columnspan=2)

link_1 = tk.Entry(master=venster, width=33, font=("Helvetica",14),
                  border=10, borderwidth=5)
link_1.grid(row=1, column=0)

link_2 = tk.Entry(master=venster, width=33, font=("Helvetica",14), 
                  border=10, borderwidth=5)
link_2.grid(row=1, column=1)

# TODO: pas reset_links aan. Gebruik insert om de gevraagde elementen toe te voegen.
def hallo_toevoegen():
    link_1.insert(0, "www.")

    web_2 = link_2.get()
    link_2.insert(tk.END, ".com")

knop = tk.Button(master=venster, command=hallo_toevoegen, 
                 text="Reset input!", width=50)
knop.grid(row=2, column=0, columnspan=2)

venster.mainloop()