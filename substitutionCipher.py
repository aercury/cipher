print("Choose a mode")
print("a) Encoding")
print("b) Decoding")
alphabet = []
product = []

mode = input(">> ").lower()
print("_____")
if mode == "a": print("Encoding")
elif mode == "b": print("Decoding")
else: print("Please choose a mode"); quit()

word = input("\nWort: ").upper()
if word == "": print("Please enter a text"); quit()

password = input("Passwort: ").upper().replace(" ", "")
if password == "": print("Please enter a password"); quit()
elif len(password) < 26: print("The password is too short"); quit()


for i in range(26):
    alphabet.append(chr(i+65))

for letter in word:
    new = ""
    for i in range(26):
        if mode == "a":
            if letter == alphabet[i]:
                print(f"{alphabet[i]} ==> {password[i]}")
                new = letter.replace(alphabet[i], password[i])
        else:
            if letter == password[i]:
                print(f"{password[i]} ==> {alphabet[i]}")
                new = letter.replace(password[i], alphabet[i])
    product.append(new)
product = "".join(product)
print(f"Result: {product}")

