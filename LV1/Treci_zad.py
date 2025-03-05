brojevi=[]

def selectionSort(brojevi, size):
    for ind in range(size):
        min_index=ind
        for j in range(ind+1, size):
            if brojevi[j]< brojevi[min_index]:
                min_index=j
        (brojevi[ind], brojevi[min_index])=(brojevi[min_index], brojevi[ind])

while True:
    print("Unesi brojeve i kad završiš napiši done: ")
    unos = input()
    if unos.lower()=="done":
        break
    try:
        brojevi.append(int(unos))
    except ValueError:
        print("Unesite broj")
if brojevi:
    print("Broj unesenih brojeva:", len(brojevi))
    print("Srednja vrijednost:", sum(brojevi)/len(brojevi))
    print("Minimalna vriijednost:", min(brojevi))
    print("Maksimalna vrijednost:", max(brojevi))
    selectionSort(brojevi,len(brojevi))
    print("Sortirana lista: ", brojevi)

else:
    print("Nije broj")
