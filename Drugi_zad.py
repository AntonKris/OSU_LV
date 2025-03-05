print("Unesi broj između 0.0 i 1.0")
x=input()

if not type(x) is float:
    raise TypeError("Wrong type of information!!")

if x>1.0:
    raise Exception("Number bigger than 1.0")

if x>=0.9:
    print("A")
elif x>=0.8:
    print("B")
elif x>=0.7:
    print("C")
elif x>=0.6:
    print("D")
else:
    print("F")