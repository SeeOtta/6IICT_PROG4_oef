# Maak een GUI met minstens drie aparte labels:
# inhoud van labels is: Hallo, Klas en 6IICT.
import tkinter as tk
venster = tk.Tk()
label = tk.Label(master=venster, text="Hallo")
label2= tk.Label(master=venster, text="Klas")
label3= tk.Label(master=venster, text="6IICT")
label.pack()
label2.pack()
label3.pack()
venster.mainloop()
