a = int(input(""))

b = int(input(""))

c = int(input(""))

d = int(input(""))

# A forma com C, B forma com D
if a <= b and c >= d:
    rt = (a + c) - (d + b)
    print(f"{rt}")

if a <= b and c <= d:
    rt = (a + d) - (b + c)
    print(f"{rt}")

if a >= b and c >= d:
    rt = (b + c) - (a + d)
    print(f"{rt}")

if a >= b and c <= d:
    rt = (a + c) - (b + b)
    print(f"{rt}")
