# Сначала необходимо определить класс узла в списке для разворота:

class InitNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# После этого необходимо определить класс для списка:

class LinkedList:
    def __init__(self):
        self.head = None                # указатель на начальный элемент списка

    def addNewNod(self, new_val):       # функция для добавления нового элемента в начало списка
        new_node = InitNode(new_val)    # новый элемент
        new_node.next = self.head       # связывание нового элемента со старым начальным элементом
        self.head = new_node            # замена нового элемента с начальным

    def printList(self):                # печать списка в консоль
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next

# Функция разворота связного списка:

    def reverseList(self):
        prev_node = None
        curr_node = self.head
        while curr_node != None:
            next_node = curr_node.next  # запоминаем следующий элемент
            curr_node.next = prev_node  # меняем ссылку
            prev_node = curr_node       # перемещаем указатели на текущий и предыдущий элементы
            curr_node = next_node
        self.head = prev_node           # устанавливаем новый начальный элемент


Linked_list = LinkedList()              # создание нового объекта списка
Linked_list.addNewNod(3)                # добавление элементов в список
Linked_list.addNewNod(4)
Linked_list.addNewNod(5)
Linked_list.addNewNod(6)
Linked_list.addNewNod(7)

Linked_list.printList()                # печать списка перед разворотом

Linked_list.reverseList()              # разворот списка

Linked_list.printList()                # печать списка после разворота

# Результат:

# 7 6 5 4 3        # до разворота
# 3 4 5 6 7        # после разворота
