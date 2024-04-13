# 165 248 94            346 299 73 198 221 313 137 205 87 336 110 186 69 223 213 216 216 177 138

# 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.

# Mod 37, Remainder

# 17   26   20 
# R     0   U

x = [165, 248, 94,346,299,73,198,221,313,137,205,87,336,110,186,69,223,213,216,216,177,138]

Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Digits = "0123456789"

for items in x:
    remainders = items % 37

    if 0 <= remainders <= 25:
        print(Alphabets[remainders])

    if 26 <= remainders <= 35:
        print(Digits[remainders-26])

    if remainders == 36:
        print("_")
