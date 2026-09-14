
#förbredningsuppgift 1
import itertools

#lista av ord som ska ingå i grafen 
words = ["tre", "öre", "tri", "tro", "trä", "trå"]

#funktion som kontroller om 2 ord skiljer sig åt med exakt en bokstav
def differ_by_one_letter(w1, w2):
    if len(w1) != len(w2):  #olika längd kan ej jämföras 
        return False
    diff = sum(a != b for a, b in zip(w1, w2)) #räknar hur många bokstäver som skiljer sig 
    return diff == 1    #returnar True om skillnaden = 1

# Skapa kanter mellan ord som skiljer sig med exakt en bokstav
edges = [(w1, w2) for w1, w2 in itertools.combinations(words, 2) if differ_by_one_letter(w1, w2)]

# Hörn = antal ord
vertices = len(words)

# Kanter = antal par som skiljer sig med en bokstav
num_edges = len(edges)

# Grannmatrisens fyllnadsgrad
fill_ratio = num_edges / (vertices * (vertices - 1) / 2)

print("Hörn:", vertices)
print("Kanter:", num_edges)
print("Fyllnadsgrad:", round(fill_ratio, 2))
print("Grannlista:")
for w in words:
    #hittar alla ord som är kopplade till w (grannar)
    neighbors = [v for u, v in edges if u == w] + [u for u, v in edges if v == w]
    print(f"{w}: {neighbors}")


#förbredningsuppgift 2 
#Vi använder samma princip som i uppgift 1, men nu ska grafen vara riktad.
# Det betyder att varje kant har en riktning: från ett ord till ett annat.

# Lista med alla ord som ska vara hörn (noder) i grafen
words = ["arg", "ärg", "agg", "alg", "ark", "arm", "art", "arv"]

#funktion som avgör om två ord skiljer sig 
def differ_by_one_letter(w1, w2):
    # Om orden inte har samma längd kan de inte jämföras bokstav för bokstav
    if len(w1) != len(w2):
        return False
    
    # Räknar hur många positioner där bokstäverna skiljer sig
    diff = sum(a != b for a, b in zip(w1, w2))
    
    # Returnerar True endast om skillnaden är exakt 1 bokstav
    return diff == 1


# Skapa riktade kanter där varje kant går från w1 → w2 om de skiljer sig med en bokstav
edges = [(w1, w2) 
         for w1 in words 
         for w2 in words 
         if w1 != w2 and differ_by_one_letter(w1, w2)]


#Antal hörn (noder) i grafen = antal ord
vertices = len(words)

# Antal riktade kanter = antal par där differ_by_one_letter är True
num_edges = len(edges)

# Fyllnadsgrad för riktad graf:
# Möjliga riktade kanter = n * (n - 1)
# Fyllnadsgrad = faktiska kanter / möjliga kanter
fill_ratio = num_edges / (vertices * (vertices - 1))

print("Hörn:", vertices)
print("Kanter:", num_edges)
print("Fyllnadsgrad:", round(fill_ratio, 2))

# Skapa grannlista (riktad)
# neighbors är en dictionary där varje ord har en lista av sina grannar
print("\nGrannlista (riktad):")

# Skapar en dictionary där varje ord får en tom lista
neighbors = {w: [] for w in words}
# Fyller dictionaryn med riktade grannar
for u, v in edges:
    neighbors[u].append(v)

# Skriver ut grannlistan
for w in words:
    print(f"{w} → {neighbors[w]}")

# Hitta riktiga cykler i grafen
# En cykel är en väg som börjar och slutar på samma ord

cycles = set()  # set() används för att undvika dubbletter

# DFS-funktion som söker efter cykler
def dfs(start, current, visited):
    # Gå igenom alla grannar till det aktuella ordet
    for nxt in neighbors[current]:
        
        # Om vi kommer tillbaka till startordet och vägen är längre än 1 → cykel hittad
        if nxt == start and len(visited) > 1:
            cycle = tuple(visited + [start])  # gör cykeln till en tuple så den kan sparas i set()
            cycles.add(cycle)
        
        # Om nästa ord inte redan är besökt → fortsätt söka
        elif nxt not in visited:
            dfs(start, nxt, visited + [nxt])

# Starta DFS från varje ord
for w in words:
    dfs(w, w, [w])

# Skriv ut alla riktiga cykler
print("\nRiktiga cykler i grafen:")
for c in cycles:
    print(" → ".join(c))

print("\nAntal Cykler:", len(cycles))
