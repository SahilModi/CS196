class Node(object):
    def __init__(self, data=None, next_node=None):
        """
        Initializes Node in Linked List.
        """
        self.data = data
        self.next = next_node

    def __str__(self):
        """
        Converts current linked list to a string.
        """
        node = self
        buffer = str(node.data)
        node = node.next

        while node != None:
            buffer += ' -> ' + str(node.data)
            node = node.next

        return buffer


print("Linked List with only one element")
linked_list = Node(1)
print(linked_list)

print("Linked List with two elements")
next_node = Node(2)
linked_list.next = next_node
print(linked_list)

print("Linked List with three elements.")
next_node.next = Node(4)  # Notice that linked_list.next.next is the same as next_node.next
print(linked_list)

print("Printing an intermediary linked list")
print(next_node)

print("Linked List with many types of elements")
linked_list.next.next.next = Node(10)
linked_list.next.next.next.next = Node(['we', 'can', 'store', 'other', 'objects'])
linked_list.next.next.next.next.next = Node("Second to last")
linked_list.next.next.next.next.next.next = Node("last")
print(linked_list)


# list:norm, the list to be turned into a linked list
def list_to_linked_list(norm):
    first = Node(norm[0])
    current = first

    for i in range(1, len(norm)):
        new_node = Node(norm[i])
        current.next = new_node
        current = new_node  # same as current = current.next
        # first.next = new_node !! can't do this because then only last data elem is returned

    return first


print("-----------------------------------")
print(list_to_linked_list([3, 4, 0, 5]))
