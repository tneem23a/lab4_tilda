class Node:
    def __init__(self, value, next = None):
        self.__value = value        #värdet i kön
        self.__next = next     #pekare till nästa node 


class LinkedQ:                  #kö som använder länkade noder
    def __init__(self):
        self.__first = None     #första noden i kön
        self.__last = None      #sista noden i kön 

    def isEmpty(self):
        return self.__first is None 

    
#lägg till värde sist i kön 
    def enqueue(self, value):
        new_node = Node(value)  #skapa ny nod med värdet 

        if self.__last is None:     #om kön är tom
            self.__first = new_node     #både first och last pekar på samma node 
            self.__last = new_node
        else:                           #om kön inte är tom 
            self.__last._Node__next = new_node #koppla ihop gamla last till nya noden
            self.__last = new_node      #flytta last till nya noden


#tar bort och returnera första värdet i kön
    def dequeue(self):                  
        if self.__first is None:         #om kö är tom, inget kan tas bort
            raise IndexError("Queue is Empty")

        value = self.__first._Node__value          #spara värdet som ska returneras
        self.__first = self.__first._Node__next    #flytta first till nästa nod 

        if self.__first is None:            #om kön blir tom
            self.__last = None             #ingen last heller

        return value                        #returnera värdet




    