#verkettete liste v1

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    #3) Element am Ende der Liste hinzufügen
    def add_last(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    #4) Ausgabe der Länge der Datenstruktur
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    #5) Anzeige aller Elemente der verketteten Liste
    def display(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    #6) Iterator-Protokoll
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


# Beispielverwendung
if __name__ == "__main__":
    import random

    #1) Datenstruktur als Objekt instanzierbar
    linked_list = LinkedList()

    for _ in range(5):
        #2) Ganzahl-Werte als Werte der Datenstruktur
        linked_list.add_last(random.randint(1, 100))

    #Ausgabe
    print("\nLänge der Liste:", linked_list.length())
    print("\nAlle Elemente der Liste [Methode]:")
    linked_list.display()
    print("\n--> Zahl wird über Methode am Ende angefügt -->\n")
    linked_list.add_last(5)
    print("Alle Elemente der Liste [Schleife]:")
    for item in linked_list:
        print(item)

