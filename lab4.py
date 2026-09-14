#Kontrollera om det finns en väg mellan två ord
# genom att byta EN bokstav i taget, där varje mellanord finns i ordlistan.

# 1. Läs in ordlistan
# Här använder vi en fil som innehåller alla giltiga ord, t.ex. word3.txt.
# Varje rad i filen är ett ord.

with open("word3.txt", "r", encoding="utf-8") as f:
    words = [w.strip() for w in f if len(w.strip()) == 3]  # tar bara ord med 3 bokstäver

#Funktion som kontrollerar om två ord skiljer sig med exakt en bokstav
def differ_by_one_letter(w1, w2):
    # Om orden inte har samma längd kan de inte jämföras
    if len(w1) != len(w2):
        return False
    # Räknar hur många bokstäver som skiljer sig
    diff = sum(a != b for a, b in zip(w1, w2))
    # Returnerar True om skillnaden är exakt 1 bokstav
    return diff == 1

#Bygg grafen (grannlista)
#Varje ord är en nod, och det finns en kant mellan ord som skiljer sig med en bokstav.
neighbors = {w: [] for w in words}
for w1 in words:
    for w2 in words:
        if differ_by_one_letter(w1, w2):
            neighbors[w1].append(w2)

#Funktion som avgör om det finns en väg mellan start och mål
# Vi använder BFS (Breadth-First Search) för att söka igenom grafen.
def finns_väg(start, mål):
    # Om start eller mål inte finns i ordlistan → ingen väg
    if start not in words or mål not in words:
        return False

    # Lista över ord som ska besökas
    queue = [start]
    # Mängd över ord som redan besökts
    visited = set([start])

    # Så länge det finns ord att undersöka
    while queue:
        current = queue.pop(0)  # tar första ordet i kön
        if current == mål:
            return True  # hittade en väg!

        # Lägg till alla grannar som inte redan besökts
        for nxt in neighbors[current]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

    # Om kön blir tom utan att vi hittat målet → ingen väg
    return False

#Testa programmet
startord = "söt"
slutord = "sur"

if finns_väg(startord, slutord):
    print(f"Startord: {startord}")
    print(f"Slutord: {slutord}")
    print(f"Det finns en väg från {startord} till {slutord}.")
else:
    print(f"Startord: {startord}")
    print(f"Slutord: {slutord}")
    print(f"Det finns ingen väg från {startord} till {slutord}.")
