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