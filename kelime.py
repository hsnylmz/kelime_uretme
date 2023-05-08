import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import itertools
import os

def show_permutations():
    H1 = selected_option_h1.get()
    H2 = selected_option_h2.get()
    H3 = selected_option_h3.get()
    list1 = [H1, H2, H3]
    #list2 = ['e', 'i', 'u']
    list2 = ['ا', 'ي', 'ل']
    
    #dosya_adi = H1+H2+H3+'.html'
    dosya_adi = 'dosya'+'.html'
    
    folder_name="kelimeler"
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, dosya_adi)

    if not os.path.exists('kelimeler'):
        os.mkdir('kelimeler')
    
    #print(dosya_adi)
    
    with open(file_path, "w", encoding="utf-8") as f:
        
        #f = open(file_path, "w")
        f.write('<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Kelime</title></head><body>')
        # Tüm K, L, M permütasyonlarını oluştur
        perms = itertools.permutations(list1)
        # Her bir permütasyonu, a, b, c harflerinin tüm kombinasyonlarıyla birleştir
        result = []
        for perm in perms:
            for combo in itertools.product(list2, repeat=len(list2)):
                merged = [x for pair in zip(perm, combo) for x in pair]
                result.append(''.join(merged))
        # Tekrarlanan kelimeleri kaldır
        result = set(result)

        # Sonucu alfabetik olarak sırala ve ekrana yazdır
        for word in sorted(result):
            f.write('<span>Google\'da ara : </span><a href="https://www.google.com/search?q=')
            f.write(word)
            f.write('" target="_blank"><span style="font-size: 24px;">')
            f.write(word)
            f.write('</span></a>&nbsp;&nbsp;&nbsp;')
            #f.write('<br>')

            f.write('<span>Google translate\'de ara : </span><a href="https://translate.google.com/?source=gtx&sl=auto&tl=tr&text=')
            f.write(word)
            f.write('" target="_blank"><span style="font-size: 24px;">')
            f.write(word)
            f.write('</span></a>')
            f.write('<br>')

            #print(word)

        f.write('</body></html>')
        f.close()
        os.startfile(file_path)

window = ttk.Window(title="kelimeOluştur by hsnylmz", themename="darkly")
window.geometry("350x80")

# Açılır menüdeki seçenekleri belirleyin
options = ['ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ع','غ', 'ف', 'ق', 'ك', 'ل' ,'م' ,'ن' ,'و' ,'ه','ي']
options = [x for x in options]


# Seçeneği depolayacak bir değişken oluşturun
selected_option_h1 = tk.StringVar(window)
selected_option_h1.set(options[0])  # Varsayılan olarak ilk seçeneği ayarlayın

selected_option_h2 = tk.StringVar(window)
selected_option_h2.set(options[0])  # Varsayılan olarak ilk seçeneği ayarlayın

selected_option_h3 = tk.StringVar(window)
selected_option_h3.set(options[0])  # Varsayılan olarak ilk seçeneği ayarlayın


option_menu_font = ("Arial", 24)
button_font = ("Arial", 16)

# Açılır menüyü oluşturun
option_menu_h1 = tk.OptionMenu(window, selected_option_h1, *options)
option_menu_h1.config(font=option_menu_font)
option_menu_h1.pack(side='left', padx=5, pady=5)

option_menu_h2 = tk.OptionMenu(window, selected_option_h2, *options)
option_menu_h2.config(font=option_menu_font)
option_menu_h2.pack(side='left', padx=5, pady=5)

option_menu_h3 = tk.OptionMenu(window, selected_option_h3, *options)
option_menu_h3.config(font=option_menu_font)
option_menu_h3.pack(side='left', padx=5, pady=5)


# Kullanıcının seçim yapmasını bekleyin
def get_user_input():
    h1 = selected_option_h1.get()
    h2 = selected_option_h2.get()
    h3 = selected_option_h3.get()
    print("Kullanıcı seçimi:", h1, h2 ,h3)

button = tk.Button(window, text="Seçimi Onayla",command=show_permutations)
button.config(font=button_font)
button.pack(side='left', padx=5, pady=5)


window.mainloop()
