import unittest

from hw5 import *


def _list_len(head):
    """
    Helper function to determine the length of the linked list.
    Note: don't pass in a linked list with a cycle (hehe).

    Input:
        head - the head of the linked list.
    
    Output:
        (int) the length of the linked list.
    """
    if head is None:
        return 0
    return 1 + _list_len(head.next_node)


class tester(unittest.TestCase):
    def test_add_head(self):
        """
        Test for adding an element to the head of the linked list.

        Test Coverage:
            - nullity
            - head elements equal
            - length of the new list
        """
        head = None
        for element in range(1, 10):
            head = add_head(head, element)
            self.assertIsNotNone(head)
            self.assertEqual(head.data, element)
            self.assertEqual(_list_len(head), element)
    
    # Write your own tests!

    def test_add_position(self):
        pass
    
    def test_remove_head(self):
        pass
    
    def test_list_sum(self):
        self.assertEqual(list_sum(None), 0)
    
    def test_is_merged(self):
        pass

    def test_find_merge_point(self):
        pass
    
    def test_find_cycle(self):
        node_a = Node(1)
        node_b = Node(2)
        node_c = Node(3)
        
        node_a.next_node = node_b
        node_b.next_node = node_c
        
        # create cycle between node_b and node_b
        node_c.next_node = node_b

        self.assertTrue(find_cycle(node_a))
    
if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
