"""
Homework 5 - Linked Lists

Release Date: 10-24
Due Date: 10-31 : s p o o k y :

To understand recursion, you must first understand recursion.
"""


class Node(object):
    """
    Class for linked list node.
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        node = self
        buffer = str(node.data)

        node = node.next_node
        while node:
            buffer += ' -> ' + str(node.data)
            node = node.next_node
        return buffer


# DONE --------------------
def add_head(head, data):
    """
    Given the head of a linked list, appends the given element to
    the head.

    Input:
        head - the head of the linked list.
        data - the item to add to the spot before the head of the linked list.

    Output:
        the newly created linked list.
    """
    if not head:
        head = Node(data)
    else:
        temp = head  # sets the type for temp and allows for .next_node call
        head = Node(data)
        head.next_node = temp
        # Above three are the same as head = Node(data, head)
    return head


linked_list = Node(3)
linked_list.next_node = Node(5)
linked_list.next_node.next_node = Node(7)
linked_list.next_node.next_node.next_node = Node(9)


# DONE -----------------------
def add_position(head, data, position):
    """
    Given the head of a linked list, adds a new element so that
    it is at the given position. If the position is greater than
    the length of the linked list, place the new element at the end
    of the linked list.

    Input:
        head - the head of the linked list.
        data - the item to add to the linked list.
        position - the position to add the element in the linked list.

    Output:
        the head of the linked list.
    """
    if not head:
        head = Node(data)
    elif position == 0:
        return add_head(head, data)
    else:
        insert_point = head
        if head:
            for i in range(position - 1):
                if insert_point.next_node:
                    insert_point = insert_point.next_node
                else:
                    break
            insert_point.next_node = Node(data, insert_point.next_node)
    return head


# DONE ---------------------------------------------
def remove_head(head):
    """
    Given the head of a linked list, removes the first element.
    If head is None, returns None.

    Input:
        head - the head of the linked list.

    Output:
        the new head of the linked list.
    """
    if not head:
        return None
    else:
        temp = head.next_node
        head = temp
    return head


# DONE ---------------------------------------------
def remove_position(head, position):
    """
    Given the head of a linked list, removes the element of the
    specified position. If the position is greater than the length
    of the linked list, do not remove anything.

    Input:
        head - the head of the linked list.
        position - the position at which to remove an element.

    Output:
        the head of the linked list.
    """
    if position == 0:
        return head.next_node
    else:
        insert_point = head
        if head:
            for i in range(position - 1):
                if insert_point.next_node:
                    insert_point = insert_point.next_node
                else:
                    return head
            if not insert_point.next_node:
                return head
            insert_point.next_node = insert_point.next_node.next_node
    return head


# DONE ----------------
def list_sum(head):
    """
    Given the head of a linked list with integer elements, returns
    the sum of the linked list.

    Input:
        head - the head of the linked list.

    Output:
        (int) the sum of the elements in the linked list.
    """
    sum_list = 0
    current = head
    while current:
        sum_list += current.data
        current = current.next_node
    return sum_list


# DONE except 1. This just returns false
def is_merged(head_a, head_b):
    """
    Given the heads of two linked lists, determines if the linked
    lists merge at some point.

    Input:
        head_a - the head of the first linked list.
        head_b - the head of the second linked list.

    Output:
        (bool) whether or not the linked lists merge.
    """
    current_a = head_a
    current_b = head_b
    is_merged = False
    while current_a and current_b:
        is_merged = current_a == current_b
        if is_merged:
            return is_merged
        current_a = current_a.next_node
        current_b = current_b.next_node
    return is_merged


def find_merge_point(head_a, head_b):
    """
    Given the heads of two linked lists that merge, returns the
    data at that merge point.

    This will only be called on lists where
    is_merged(head_a, head_b) is true.

    Input:
        head_a - the head of the first linked list.
        head_b - the head of the second linked list.

    Output:
        the element at the merge point.
    """
    if not head_a or not head_b:
        return None

    current_a = head_a
    current_b = head_b
    while current_b.next_node:
        if current_a.data == current_b.data:
            return current_a.data
        current_b = current_b.next_node

    current_a = head_a
    current_b = head_b
    while current_a.next_node:
        if current_b.data == current_a.data:
            return current_b.data
        current_a = current_a.next_node
    return current_b.data  # useless statement


linked_list2 = Node(999)
linked_list3 = Node(999)
linked_list2.next_node = linked_list
# print(linked_list2)

merge_1 = Node(1000)
merge_1.next_node = Node(8998)
merge_1.next_node.next_node = linked_list


# print(linked_list)
# print(find_merge_point(merge_1, linked_list))


def find_cycle(head):
    """
    Given the head of a linked list, determines whether or not there
    is a cycle in the linked list.

    Input:
        head - the head of the linked list.

    Output:
        (bool) whether or not there is a cycle in the linked list.
    """
    if not head or not head.next_node or not head.next_node.next_node:
        return False

    node_a = head
    node_b = head

    # These two nodes will have to eventually equal each other in a cycle.
    while node_a:
        node_a = node_a.next_node

        if node_b.next_node:
            node_b = node_b.next_node.next_node
        else:
            return False

        if node_a is node_b:
            return True

    return True  # dummy statement