from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
from googletrans import Translator

class Translate:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("600x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Masukkan teks:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Terjemahan:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtSumber = Entry(mainFrame, width=50)
        self.txtSumber.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50)
        self.txtHasil.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        # Pasang Button
        self.btnTranslateEn = Button(mainFrame, text='Translate to English',
            command=lambda: self.onTranslate('en'))
        self.btnTranslateEn.grid(row=1, column=0, padx=5, pady=5)

        self.btnTranslateNl = Button(mainFrame, text='Translate to French',
            command=lambda: self.onTranslate('fr'))
        self.btnTranslateNl.grid(row=1, column=1, padx=5, pady=5)

        self.btnTranslateCn = Button(mainFrame, text='Translate to Korean',
            command=lambda: self.onTranslate('ko'))
        self.btnTranslateCn.grid(row=1, column=2, padx=5, pady=5)

        self.btnTranslateAr = Button(mainFrame, text='Translate to Russian',
            command=lambda: self.onTranslate('ru'))
        self.btnTranslateAr.grid(row=1, column=3, padx=5, pady=5)

    def onTranslate(self, dest_lang):
        # membuat instance object
        penterjemah = Translator()

        # menterjemahkan
        hasil = penterjemah.translate(self.txtSumber.get(), dest=dest_lang)

        # menghapus isi textbox hasil sebelumnya
        self.txtHasil.delete(0, END)

        # menampilkan hasil terjemahan
        self.txtHasil.insert(END, hasil.text)

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = Translate(root, "Program Translator")
    root.mainloop()
