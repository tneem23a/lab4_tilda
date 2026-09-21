def utskrift(lista):
    if len(lista) > 0:
        utskrift(lista[1:])
        print(lista[0])

utskrift([1,2,3,4,5])

#ifall print kommer efter rekursionen blir elementen i omvänd ordning
#därför att rekursionen sker innan printen, då utförs rekursionen, 
#elementen blir nedstoppade(vägen ner) i en stack, då följer den LIFO
#last in, first out - så när rekursionen är slut då printar den det sists
#som lader ner vilket var 5, sen 4, osv tills 1 


#förbättra söt-sur

#nod representerar ord i kedjan
#parent pekar på ordet före så vi kan gå bakåt i kedjan
class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word      # ordet i denna nod
        self.parent = parent  # pekare till föräldern (föregående ord)

#andände kön LinkedQ klassen 
from linkedQFile import LinkedQ

#specialundantag som kastas när hittat slutordet, låter oss avbryta BFS direkt 
class SolutionFound(Exception):
    pass


#läser in ordlistan och returnerar lista med alla ord
#BFS behöver veta vilka ord är tillåtna för använding 
def read_wordlist(filename):
    svenska = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            ordet = line.strip()
            if ordet:
                svenska.append(ordet)
    return svenska


#Skriver ut hela ordkedjan från startord till slutord.
# Detta görs rekursivt: först går vi bakåt till startordet,
# sedan skrivs orden ut på vägen upp ur rekursionen.
def writechain(node):
    # Rekursivt: gå bakåt till startordet, skriv sedan framåt
    if node.parent is not None: #om förälder finns, gå bakåt
        writechain(node.parent)
    print(node.word)    #skriv ut ordet när vi kommer upp 



def makechildren(node, q, slutord, svenska, gamla):
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
#generar alla barn till ett ord (1 tecken)
#gaml = ord som använts för att slippa dubletter 
#q = kön för BFS 
#node = parentnode + förälder 

    #går igenom varje position i ordet 
    for i in range(len(node.word)):
        for bokstav in alfabet:
            #byt ut en bokstav i taget -> genererar ord 1 steg bort
            nytt_ord = node.word[:i] + bokstav + node.word[i+1:]
            #endast ord som finns i ordlistan och inte redan använt är glitiga
            if nytt_ord in svenska and nytt_ord not in gamla:
                gamla.append(nytt_ord)  #markera som besökt 
                #skapa ord som pekar på sin förälder
                nytt_barn = ParentNode(nytt_ord, node)
                q.enqueue(nytt_barn)    #lägg barnet i BFS kön 

                if nytt_ord == slutord: #om det är ordet vi vill hitta 
                    writechain(nytt_barn)   #skriv ut kedjan
                    raise SolutionFound     #avbryt BFS 


def main():
    # Läs ordlista
    svenska = read_wordlist("word3.txt")

    #tar emot start- och slutord fråna nvändar, strip - bort extra mellanslag
    startord = input("Startord: ").strip()
    slutord = input("Slutord: ").strip()

    #kontrollerar samma längd för att jämföra bokstav för bokstav 
    if len(startord) != len(slutord):
        print("Orden måste ha samma längd.")
        return

    #kontrollerar båda orden finns i ordlistan 
    if startord not in svenska or slutord not in svenska:
        print("Båda orden måste finnas i ordlistan.")
        return
    #skapa BFS kö och gamla lista för ord som besökts 
    q = LinkedQ()
    gamla = []

    # Startnoden har ingen förälder
    start_node = ParentNode(startord, None)
    #lägg noden i kön, markera ord som besökt 
    q.enqueue(start_node)
    gamla.append(startord)

    try:
        #BFS fortsätter så länge kön inte är tom 
        while not q.isEmpty():
            node = q.dequeue()
            #genererar alla barn till noden, solutionfound om slutord hittas
            makechildren(node, q, slutord, svenska, gamla)
        #om kön är tom, inget slutord hittas    
        print("Ingen lösning hittades.")
    except SolutionFound:
        #om slutionfound kastat har kedjan hittats av write_chain()
        print("Kedja hittad!")

#kör main om filen körs
if __name__ == "__main__":
    main()
