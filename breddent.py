#Breddenförstsökning, del 1
# Läs in ordlistan (alla med tre bokstäver läggs in i svenska --> utgör noderna)
with open("word3.txt", "r", encoding="utf-8") as f:
    svenska = [w.strip() for w in f if len(w.strip()) == 3]

# Lista för ord som redan använts för att förhindra dubletter
gamla = []


#Funktion som skapar alla barn till ett ord
def makechildren(startord):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
    barn = []
#BFS - hitta alla ord på nivå 1 

    # Gå igenom varje position i ordet
    for i in range(len(startord)):
        for bokstav in alfabet:
            # Byt ut en bokstav i  vilket genererar alla möjliga ord 1 steg bort
            nytt_ord = startord[:i] + bokstav + startord[i+1:]
            # Om ordet finns i ordlistan och inte redan använts
            if nytt_ord in svenska and nytt_ord not in gamla:
            #endast ord som finns i ordlistan och inte använts räknas som barn
                barn.append(nytt_ord)
                gamla.append(nytt_ord)
                print(nytt_ord)  # skriv ut barnet, detta är nivå 1 

    return barn

# Huvudprogram
startord = input("Startord: ")
slutord = input("Slutord: ")

# Skapa barn till startordet
makechildren(startord)


#Breddenförstsökning, del 2
from linkedQFile import LinkedQ  # importera köklass

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
                q.enqueue(nytt_ord)  # lägg barnet sist i kön - BFS 
                if nytt_ord == slutord: #om slutordet hittas 
                    print("Det finns en väg till", slutord)
                    return True
    return False #om slutordet inte hittades bland barnen 

# Huvudprogram
startord = input("Startord: ")
slutord = input("Slutord: ")

q = LinkedQ() 
q.enqueue(startord)
gamla.append(startord)
#startordet läggs i kön och markeras som besökt 

# Breddenförstsökning
found = False
while not q.isEmpty() and not found:
    word = q.dequeue()
    #tar ut första ordet, skapa barnet, lägg det sist i kön
    #fortsätt tills slutordet hittats 
    found = makechildren(word, q, slutord)

if not found:
    #om BFS avslutas utan att hitta slutordet finns ingen väg ut 
    print("Ingen väg hittades mellan", startord, "och", slutord)
