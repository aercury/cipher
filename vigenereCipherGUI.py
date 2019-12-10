import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Vigenère Cipher')
root.geometry("500x300")

def copyToClipboard(value):
    root.clipboard_clear()
    root.clipboard_append(value)
    root.update()

def encode():
    global product
    product = []
    if (inputElement.get() != ""):
        word = inputElement.get().upper()
        password = list(passwordElement.get().upper())
        try: password[len(word)-1]
        except:
            messagebox.showerror("Error", "The password is too short")
            outputElement.config(textvariable="___")
        finally:
            for index in range(len(password)):
                password[index] = ord(password[index])%26
            for index in range(len(word)):
                v = password[index]
                x = word[index]
                p = ord(x) + v
                if ord(x) > 64 and ord(x) < 91:
                    if p < 91:
                        product.append(chr(p))
                    else:
                        p-=26
                        product.append(chr(p))
                else:
                    product.append(x)
            product = "".join(product).upper()
            outputElement.config(text=product)
            copyToClipboard(product)
            print(product)
    else:
        messagebox.showerror("Error", "Please enter a text")
        outputElement.config(text="____")


def decode():
    global product
    product = []
    if (inputElement.get() != ""):
        word = inputElement.get().upper()
        password = list(passwordElement.get().upper())
        try: password[len(word)-1]
        except:
            messagebox.showerror("Error", "The password is too short")
            outputElement.config(text="____")
        finally:
            for index in range(len(password)):
                password[index] = ord(password[index])%26
            for index in range(len(word)):
                v = password[index]
                x = word[index]
                p = ord(x) - v
                if ord(x) > 64 and ord(x) < 91:
                    if p > 64:
                        product.append(chr(p))
                    else:
                        p+=26
                        product.append(chr(p))
                else:
                    product.append(x)
            product = "".join(product).upper()
            outputElement.config(text=product)
            copyToClipboard(product)
            print(product)
    else:
        messagebox.showerror("Error", "Please enter a text")
        outputElement.config(text="____")


headerElement= Label(root, text="Vigenère Cipher")
inputElement= Entry(root, width=30)
passwordElement= Entry(root, width=30)
encodeButtonElement = Button(root, text="Encode", command=encode)
decodeButtonElement = Button(root, text="Decode", command=decode)
outputElement = Label(root, text="_____")

headerElement.pack(padx=5, pady=10, side=TOP)
inputElement.pack(padx=5, pady=10, side=TOP)
passwordElement.pack(padx=5, pady=10, side=TOP)
encodeButtonElement.pack(padx=5, pady=10, side=TOP)
decodeButtonElement.pack(padx=5, pady=10, side=TOP)
outputElement.pack(padx=5, pady=10, side=TOP)

inputElement.focus()
root.mainloop()
