print("Choose a mode")
print("a) Encoding")
print("b) Decoding")
product = []
mode = input(">> ").lower()
print("_____")
if mode == "a": print("Encoding")
elif mode == "b": print("Decoding")
else: print("Please choose a mode"); quit()

word = list(input("\nWort: ").upper())
if word == "": print("Please enter a text"); quit()

v = int(input("Shift: "))
if v < 1 and str(v).isdigit == false: print("The shift has to be a number above 0"); quit()
v = v%26

for index in range(len(word)):
    x = word[index]
    if mode == "a":
        p = ord(x) + v
        if ord(x) > 64 and ord(x) < 91:
            if p < 91:
                product.append(chr(p))
            else:
                p-=26
                product.append(chr(p))
        else:
            product.append(x)
    if mode == "b":
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
print(f"Result: {product}")
