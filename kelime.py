import itertools
import os
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *



def limit_entry_to_one_char(entry):
    def on_validate(text):
        if len(text) > 1:
            entry.bell() # hata bildirimi
            return False
        else:
            return True
    entry['validate'] = 'all'
    entry['validatecommand'] = (entry.register(on_validate), '%P')

def check_input():
    if not word_entry_H1.get() or not word_entry_H2.get() or not word_entry_H3.get():
        messagebox.showwarning("Uyarı", "Lütfen tüm harf kutularını doldurun!")
    else:
        show_permutations()

def clear_entries():
    word_entry_H1.delete(0, END)
    word_entry_H2.delete(0, END)
    word_entry_H3.delete(0, END)

def show_permutations():
    H1=(word_entry_H1.get()).upper()
    H2=(word_entry_H2.get()).upper()
    H3=(word_entry_H3.get()).upper()
    list1 = [H1, H2, H3]
    list2 = ['e', 'i', 'u']
    dosya_adi = H1+H2+H3+'.txt'
    
    folder_name="kelimeler"
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, dosya_adi)

    if not os.path.exists('kelimeler'):
        os.mkdir('kelimeler')
    
    #print(dosya_adi)
    
    f = open(file_path, "w")
    # Tüm K, L, M permütasyonlarını oluştur
    perms = itertools.permutations(list1)
    # Her bir permütasyonu, a, b, c harflerinin tüm kombinasyonlarıyla birleştir
    result = []
    for perm in perms:
        for combo in itertools.product(list2, repeat=len(list2)):
            merged = [x for pair in zip(perm, combo) for x in pair]
            result.append(' '.join(merged))
    # Tekrarlanan kelimeleri kaldır
    result = set(result)

    # Sonucu alfabetik olarak sırala ve ekrana yazdır
    for word in sorted(result):
        f.write(word)
        f.write('\n')
        #print(word)

    f.close()
    os.startfile(file_path)

# Tkinter penceresini oluşturun
#window = Tk(className='Kelime Oluştur by hsnylmz')
window = ttk.Window(title="kelimeOluştur by hsnylmz", themename="yeti")
window.geometry("550x80")
#windowBackground = '#ADD8E6'
#window.configure(bg=windowBackground)
window.resizable(False,False)
try:
    window.iconbitmap('elif.ico')
except:
    pass
    


yazi=Label(window, text="Harfleri Giriniz ", font=('Helvetica bold',18))
yazi.pack(side='left', padx=5, pady=5)

word_entry_H1 = Entry(window, width=3, justify='center')
word_entry_H1.config(font=('Helvetica bold',18))
word_entry_H1.pack(side='left', padx=5, pady=5)


word_entry_H2 = Entry(window, width=3, justify='center')
word_entry_H2.config(font=('Helvetica bold',18))
word_entry_H2.pack(side='left', padx=5, pady=5)

word_entry_H3 = Entry(window, width=3, justify='center')
word_entry_H3.config(font=('Helvetica bold',18))
word_entry_H3.pack(side='left', padx=5, pady=5)

# Kelime girişi yaptıktan sonra sıralamaları göstermek için bir düğme oluşturun
permute_button = ttk.Button(window, text="OLUŞTUR", command=check_input, width=10, bootstyle=SUCCESS)
permute_button.pack(side='left', padx=5, pady=5)

clear_button = ttk.Button(window, text="TEMİZLE", command=clear_entries, width=10, bootstyle=DANGER)
clear_button.pack(side='left', padx=5, pady=5)

word_entry_H1.focus_set()
limit_entry_to_one_char(word_entry_H1)
limit_entry_to_one_char(word_entry_H2)
limit_entry_to_one_char(word_entry_H3)
window.mainloop()
