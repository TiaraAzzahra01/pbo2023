import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    jarijari = float(txtjarijari.get())
    
    luas = 4*3.14*jarijari**2
    
    txtluas.delete(0,END)
    txtluas.insert(END,luas)

    
def hitung_volume():
    jarijari = float(txtjarijari.get())
    
    Volume = 4/3*3.14*jarijari**3
    
    txtvolume.delete(0, END)
    txtvolume.insert(END, Volume)
    
def hitung():
    hitung_luas()
    hitung_volume()
    
# Create tkinter object
app = tk.Tk()

#Tambahkan judul
app.title("Kalkulator Luas dan Volume Bola")

#Windows
frame = Frame(app)
frame.pack(padx= 20, pady=20)

#Label Jari Jari
jarijari= Label(frame, text="Jarijari:")
jarijari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Textbox Jari Jari
txtjarijari =Entry (frame)
txtjarijari.grid(row=0, column=1)

#Button 
hitung_button = Button (frame, text="Hitung", command=hitung)
hitung_button.grid(row=1, column=1, sticky=W, padx=5, pady=5)

#Output Label Luas
luas = Label(frame, text="Luas:")
luas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Output Label Volume
volume = Label(frame, text="Volume:")
volume.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#Output Textbox Luas
txtluas = Entry (frame)
txtluas.grid(row=2, column=1, sticky=W, padx=5, pady=5)

#Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=3, column=1, sticky=W, padx=5, pady=5)

app.mainloop()