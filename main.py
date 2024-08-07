from tkinter import *
from tkinter import messagebox
import onetimepad

def center_window(width=350, height=650):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


window = Tk()
window.title("Secret Notes")
window.config(bg="light gray", pady=20)
center_window()


def save_encrypt_button_clicked():
    file_path = "/Users/alperen/PycharmProjects/secretNotes/secret.txt"  # Belirli dosya yolu
    title = title_key_entry.get().strip()  # Başlığı al ve boşlukları temizle
    note = secret_text.get('1.0', END).strip()  # Notu al ve boşlukları temizle
    master_key = master_key_entry.get().strip()  # Anahtarı al ve boşlukları temizle
    if title and note and master_key:  # Başlık, not ve anahtar boş değilse
        try:
            encrypted_note = onetimepad.encrypt(note, master_key)  # Metni şifrele
            with open(file_path, 'a') as file:  # Notları ekleme modunda aç
                file.write(f"Title: {title}\n{encrypted_note}\n\n")  # Başlığı ve şifreli notu dosyaya ekle
                messagebox.showinfo("Information", f"Note saved to: {file_path}")
                title_key_entry.delete(0, END)  # Başlık alanını temizle
                secret_text.delete('1.0', END)  # Not alanını temizle
                master_key_entry.delete(0, END)  # Anahtar alanını temizle
        except Exception as e:
            messagebox.showerror("showerror", f"Error: {str(e)}")

    else:
        messagebox.showwarning("showwarning", "Title, note, and master key are required!")


def decrypt_button_clicked():
    encrypted_note = secret_text.get('1.0', END).strip()  # Şifreli metni al
    master_key = master_key_entry.get().strip()  # Anahtarı al ve boşlukları temizle

    if encrypted_note and master_key:
        try:
            decrypted_note = onetimepad.decrypt(encrypted_note, master_key)  # Şifreyi çöz
            secret_text.delete('1.0', END)  # Mevcut metni temizle
            secret_text.insert('1.0', decrypted_note)  # Çözülmüş metni ekle
        except Exception as e:
            messagebox.showerror("showeorror", f"Error: {str(e)}")

    else:
        messagebox.showwarning("showwarning", "Encrypted text and master key are required!")


# IMAGE
logo = PhotoImage(file="secretNotes.png")
logo_label = Label(image=logo, bg="light gray")
logo_label.pack()

# Title label
title_label = Label(text="Enter your title")
title_label.config(bg="light gray", fg="black")
title_label.place(x=122, y=140)

# Title entry
title_key_entry = Entry(width=20, bg="white", fg="black")
title_key_entry.focus()
title_key_entry.place(x=80, y=170)

# Secret label
secret_label = Label(text="Enter your note")
secret_label.config(bg="light gray", fg="black")
secret_label.place(x=122, y=200)

# Secret text
secret_text = Text(width=40, height=15, bg="white", fg="black")
secret_text.place(x=33, y=230)

# Master key label
master_key_label = Label(text="Enter Master Key")
master_key_label.config(bg="light gray", fg="black")
master_key_label.place(x=122, y=440)

# Master key entry
master_key_entry = Entry(width=20, bg="white", fg="black", show="*")
master_key_entry.place(x=82, y=470)

# Save & encrypt button
save_encrypt_button_button = Button(text="Save & Encrypt", command=save_encrypt_button_clicked)
save_encrypt_button_button.place(x=110, y=510)

# Decrypt button
decrypt_button = Button(text="Decrypt", command=decrypt_button_clicked)
decrypt_button.place(x=130, y=550)

window.mainloop()
