products = []
print("Caesar Reverse")
print("")
x = list(input("Word: ").upper())
if x != "":
    for v in range(1,26):
        product = []
        for i in x:
            p = ord(i) - v
            if ord(i) > 64 and ord(i) < 91:
                if p > 64:
                    product.append(chr(p))
                else:
                    p+=26
                    product.append(chr(p))
            else:
                product.append(i)
        products.append(product)

print("\nPotential Results:\n")
for i in products:
    print("".join(i).upper())
