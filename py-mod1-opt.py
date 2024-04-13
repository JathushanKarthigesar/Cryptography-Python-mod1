import string

Characters = string.ascii_uppercase + string.digits + "_"

List = [165, 248, 94,346,299,73,198,221,313,137,205,87,336,110,186,69,223,213,216,216,177,138]

flag = ""

for items in List:

    flag += Characters[items % 37]


print("picoCTF{" + flag + "}")