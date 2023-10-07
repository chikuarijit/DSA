"""
Question

Merge Two Sorted Lists Easy

You are given the heads of two sorted linked lists list1 and list2 .
Merge the two lists in a one sorted list. The list should be made by splicing
together the nodes of the first two lists.
Return the head of the merged linked list.
"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def print_list(current_list):
    while current_list:
        print(current_list.val, end=" -> ")
        current_list = current_list.next
    print()


def merge_two_lists(list1, list2):
    # Creating a dummy node to simplify the node
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next

        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Append the remaining nodes (if any) from list1 or list2
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    # The merged list starts after the dummy node
    return dummy.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

print_list(list1)
print_list(list2)

print_list(merge_two_lists(list1, list2))