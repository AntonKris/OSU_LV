print("Unesi broj radnih sati: ")
brojRadnihSati=float(input())
print("Unesi broj zarade u eurima po satu: ")
euraPoSatu=float(input())

def total_euro():
    ukupno=brojRadnihSati*euraPoSatu
    print("Radni sati:",brojRadnihSati,"h")
    print("eura/h",euraPoSatu)
    print("Ukupno:",ukupno,"eura")

total_euro()