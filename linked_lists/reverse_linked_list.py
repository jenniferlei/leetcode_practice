# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head): # runtime O(n), space O(1)
    """Given the head of a singly linked list, reverse the list, and return the reversed list."""
    reversed_list = []

    # assign temp prev node to None
    # go through each item in linked list, prev should be next 

    # two pointers
    prev, curr = None, head

    while curr:
        nxt = curr.next # store next item in loop, since we're reversing the next item/ hold this in memory
        curr.next = prev # assign new next item to previous
        prev = curr # store current as previous/ update pointer
        curr = nxt # change current to next/ update pointer

    head = prev
    

# [] -> []
# [1,2,3,4,5] -> [5,4,3,2,1]

# go through each item in list
# next needs to be assigned to previous
# store old curr.next for next item
# store curr as prev
# assign curr to nxt as 

def reverse_linked_list(head): # runtime O(n), space O(1)
    """Given the head of a singly linked list, reverse the list, and return the reversed list."""
    reversed_list = []

    # base case
    if not head:
        return None

    new_head = head

    if head.next: # while there is still another node to be reversed
        new_head = reverse_linked_list(head.next)
        head.next.next = head

    head.next = None

    return new_head



# [1,2,3]
# Head -> 1 -> 2 -> 3 -> None
# None <- 1 <- 2 <- 3 <- New Head

# return 3

# 3 next = 2
# 2 next = None

# return 3 -> 2 -> None

# 2 next = 1
# 1 next - None

# return 3 -> 2 -> 1 -> None


# head.next.next = head explanation:

# linkedlist of 1 => 2 => 3

# base case focuses on 2 => 3 where 2 is the head

# Head.next.next = head means 3.next = 2 (the head) so this makes a 2 => 3 circular linked list (which means 2 => 3 & 2 <= 3 exists). 2 is still the head.

# then we must detach 2 => 3(remember we still have 2 <= 3) so head.next = null means we detach 2 => 3.

# Now the result is 2 <= 3.

# Now we go to the next part which is 1 => 2 and repeat.