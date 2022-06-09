# Iterative T = O(n) S=O(1)
def revlinklistitr(self, head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Recursive T = O(n), S=O(n)
def revlinkedlistrec(self, head):
