class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"<{self.val}; Next: {self.next}>"

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# [1, 3, 4, 6, 7]
# [2, 3, 5]
# [1,2,3,3,4,5,6,7]

# [1, 3, 4, 6, 7]
# [7, 8, 9, 10]
# [1,3,4,6,7,7,8,9,10]
# curr1, curr2 = 1, 7
# head = 1
# curr1 = curr1.next = 3
# head.next = 3
# curr1 = curr1.next = 4
# 

# []
# []
# []


# loop while there are still nodes in list1 and list2
# new list variable
# give heads of each list

# two pointers curr1 and curr2
# while curr1.next or curr2.next
# if one of the variables is smaller, add to new linked list
# move the pointer to next

def merge_two_sorted_linked_lists(list1, list2):

    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next

# [1, 3, 4, 6, 7]
# [2, 8, 9, 10]
# [1,2,3,4,6,7,8,9,10]

node5 = ListNode(7)
node4 = ListNode(6, node5)
node3 = ListNode(4, node4)
node2 = ListNode(3, node3)
node1 = ListNode(1, node2)

node9 = ListNode(10)
node8 = ListNode(9, node9)
node7 = ListNode(8, node8)
node6 = ListNode(2, node7)

print(node1)
print(node6)

print(merge_two_sorted_linked_lists(node1, node6))