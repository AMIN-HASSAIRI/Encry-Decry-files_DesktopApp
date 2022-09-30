from cryptography.fernet import Fernet
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

global filepath
global Key
global keypath


# function to encrypt files
def EncryptFiles():
    messagebox.showinfo("", "Select a file with key")
    # user select a file with a key
    keypath = filedialog.askopenfilename()
    # open key file
    with open(keypath, "rb") as fileKey:
        key = fileKey.read()

    global fernet
    fernet = Fernet(key)

    messagebox.showinfo("", "Select files to encrypt")
    # user select a file to encrypt
    filepath = filedialog.askopenfilenames()
    # for each file in the list encrypts that file
    for x in filepath:
        # open each file in filepath
        with open(x, "rb") as file:
            original = file.read()

        # encrypt that file
        global encrypted
        encrypted = fernet.encrypt(original)

        # open the file in write mode and encrypts the data in it
        with open(x, "wb") as encrypted_file:
            encrypted_file.write(encrypted)

    messagebox.showinfo("", "Files was encrypted successfully!")


# function to decrypt files
def DecryptFiles():
    messagebox.showinfo("", "Select a key")
    # user select a file with a key
    keypath = filedialog.askopenfilename()
    # open key file
    with open(keypath, "rb") as filekey:
        key = filekey.read()

    messagebox.showinfo("", "Select files to decrypt")
    # user select a file to decrypt
    filepath = filedialog.askopenfilenames()
    # for each file in the list decrypt that file
    for x in filepath:
        with open(x, "rb") as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        # open the file in write mode and decrypt the file
        with open(x, "wb") as dec_file:
            dec_file.write(decrypted)

        messagebox.showinfo("", "Files was decrypted successfully!")


top = Tk()
# window size
top.geometry("300x200")
# buttons to run a function when pressed
button = Button(top, text="EncryptFiles", command=EncryptFiles, font=200, bg='#fc034a')
button.place(x=50, y=80)
button = Button(top, text="DecryptFiles", command=DecryptFiles, font=200, bg='#03fcb1')
button.place(x=170, y=80)
# loops gui window
top.mainloop()
