n = int(input(""))

a = str(input(""))

a = a.replace(" ", "")

a = a.replace("," , "")

a = a.replace(".", "")

b = str(input(""))

b = b.replace(" ", "")

b = b.replace("," , "")

b = b.replace(".", "")


ad = sorted(a)

bd = sorted(b)

if ad == bd:
    print("S")
else:
    print("N")
