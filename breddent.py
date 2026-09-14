#Breddenförstsökning, del 1

# Läs in ordlistan (svenska ord med tre bokstäver)
with open("word3.txt", "r", encoding="utf-8") as f:
    svenska = [w.strip() for w in f if len(w.strip()) == 3]

# Lista för ord som redan använts (dumbarn)
gamla = []


#Funktion som skapar alla barn till ett ord
def makechildren(startord):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    barn = []

    # Gå igenom varje position i ordet
    for i in range(len(startord)):
        for bokstav in alfabet:
            # Byt ut en bokstav i taget
            nytt_ord = startord[:i] + bokstav + startord[i+1:]
            # Om ordet finns i ordlistan och inte redan använts
            if nytt_ord in svenska and nytt_ord not in gamla:
                barn.append(nytt_ord)
                gamla.append(nytt_ord)
                print(nytt_ord)  # skriv ut barnet

    return barn

# Huvudprogram
startord = input("Startord: ")
slutord = input("Slutord: ")

# Skapa barn till startordet
makechildren(startord)



#Breddenförstsökning, del 2
from linkedQ import LinkedQ  # importera din köklass från labb 2

with open("word3.txt", "r", encoding="utf-8") as f:
    svenska = [w.strip() for w in f if len(w.strip()) == 3]

gamla = []  # lista över redan besökta ord

# makechildren() – skapar barn till ett ord och lägger dem i kön
def makechildren(ordet, q, slutord):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

    for i in range(len(ordet)):
        for bokstav in alfabet:
            nytt_ord = ordet[:i] + bokstav + ordet[i+1:]
            if nytt_ord in svenska and nytt_ord not in gamla:
                gamla.append(nytt_ord)
                q.enqueue(nytt_ord)  # lägg barnet sist i kön
                if nytt_ord == slutord:
                    print("Det finns en väg till", slutord)
                    return True
    return False

# Huvudprogram
startord = input("Startord: ")
slutord = input("Slutord: ")

q = LinkedQ()
q.enqueue(startord)
gamla.append(startord)

# Breddenförstsökning
found = False
while not q.isEmpty() and not found:
    word = q.dequeue()
    found = makechildren(word, q, slutord)

if not found:
    print("Ingen väg hittades mellan", startord, "och", slutord)
