import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    R = float(txtrusuk.get())
    
    Luas = 6 * (R * R)
    
    txtluas.delete(0,END)
    txtluas.insert(END,Luas)
    
def hitung_volume():
    R = float(txtrusuk.get())
    
    Volume = R * R * R
    
    txtvolume.delete(0, END)
    txtvolume.insert(END, Volume)
    
def hitung():
    hitung_luas()
    hitung_volume()
    
# Create tkinter object
app = tk.Tk()

#Tambahkan judul
app.title("Kalkulator Luas dan Volume Kubus")

#Windows
frame = Frame(app)
frame.pack(padx= 20, pady=20)

#Label Rusuk
rusuk= Label(frame, text="Rusuk:")
rusuk.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Textbox Rusuk
txtrusuk =Entry (frame)
txtrusuk.grid(row=0, column=1)

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

#Output Textbox Keliling
txtvolume = Entry (frame)
txtvolume.grid(row=3, column=1, sticky=W, padx=5, pady=5)

app.mainloop()