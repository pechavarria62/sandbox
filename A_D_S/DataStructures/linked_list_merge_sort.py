
from ds import linkedList

# l = linkedList()
# l.add(1)
# print(l)

def merge_sorted(ds):
    '''
    Sort a linked list in ascending order.
    - Recursively divide the linked list into sublist containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains.

    Returns a sorted linked list.

    Runs in O(kn log n) time 
    '''

    if ds.size() == 1:
        return ds
    elif ds.head is None:
        return ds
    
    left_half, right_half = split(ds)
    left = ds(left_half)
    right = ds(right_half)

    return merge(left, right)

def split(ds):
    '''
    Divide the unsorted list at midpoint into sublist.

    Takes O(k log n) time
    '''
    if ds == None or ds.head == None:
        left_half = ds
        right_half = None

        return left_half, right_half
    else:
        size = ds.size()
        mid = size // 2
        
        mid_node = ds.node_at_index(mid - 1)

        left_half = ds
        right_half = ds()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half , right_half

def merge(left, right):

    '''
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list.

    Runs in O(n) time
    '''
    # Create a new linked list that contain nodes from
    # merging left and right.

    merged = linkedList()

    # Add a fake head that is discarded later.
    merged.add(0)

    # Set current to the head of the linked list.
    current = merged.head

    # Obtain head nodes for left and right linked lists.
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node
    # of either
    while left_head or right_head:
        # if the head node of left in None, we're past the tail
        # Add the node from right to merged linked list.
        if left_head is None:
            current.next_node = right_head

            # Call next on right to set loop condition to False.
            right_head = right_head.next_node

        # If the head node of right is None, We're past the tail.
        # Add the tail node from left to merged linked list.
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node

        else:
            # Not at either tail node.
            # Obtain node data to perform comparison operations.
            left_data = left_head.data
            right_data = right_head.data

            # If left data is less than right data , set current to left node.
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node on that list.
                left_head = left_head.next_node 

            # If left data is grater than right, set current to right node.
            else:
                current.next_node = right_head

                # Move right head to nex node
                right_head = right_head.next_node
    
        # Move current to next node.
        current = current.nex_node
    # Discard fake head and set first merged node as head.
    head = merged.head.next_node
    merged.head = head

    return merged

l = linkedList()
l.add(10)
l.add(3)
l.add(6)
l.add(90)
l.add(5)

print(l)
# sorted_linked_list = merge_sorted(l) 





