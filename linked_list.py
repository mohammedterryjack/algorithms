from typing import Any, Optional

class Node:
    def __init__(self,value:Any) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self,value:Any) -> None:
        if self.head is None: 
            self.head = Node(value)
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(value)

    def delete(self, value:Any) -> None:
        if self.head.value == value:
            self.head = self.head.next
            return

        previous_node = None
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                previous_node.next = current_node.next
            previous_node = current_node
            current_node = current_node.next

    def __repr__(self) -> str:
        representation = f"{type(self).__name__}( "

        current_node = self.head 
        while current_node is not None:
            representation += f"{current_node.value}, "
            current_node = current_node.next
        representation += "None )"
        return representation
    
    def index(self,value:Any) -> int:
        current_node = self.head 

        index = 0
        while current_node is not None:
            if value == current_node.value:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def contains(self, value:Any) -> bool:
        return self.index(value) != -1 

    def reverse(self,node_to_attach_to_tail:Optional[Node]=None) -> None:
        previous_node = node_to_attach_to_tail
        current_node = self.head 
        while current_node is not None:
            old_next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = old_next_node
        self.head = previous_node

#my_linked_list = LinkedList()
#print(my_linked_list)
#my_linked_list.append("a")
#my_linked_list.append("b")
#my_linked_list.append("c")
#my_linked_list.append("d")
#print(my_linked_list)
#my_linked_list.reverse()
#print(my_linked_list)
#my_linked_list.reverse()
#print(my_linked_list)
#print(my_linked_list.index("c"))
#print(my_linked_list.contains("c"))
#my_linked_list.delete("c")
#print(my_linked_list.contains("c"))
#print(my_linked_list)
#my_linked_list.delete("d")
#my_linked_list.delete("a")
#print(my_linked_list)
#my_linked_list.reverse()
#print(my_linked_list)
