# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# This was accepted, but slow


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return []

        combined = head = None

        # first get the smallest to add in front first
        min_val = float('inf')

        # keep a 'pointer' to head of each list
        curr_node = []
        for i in range(len(lists)):
            curr_node.append(lists[i])

        at_least_one_unfinished = True

        while at_least_one_unfinished:
            min_k = -1
            min_val = float('inf')
            at_least_one_unfinished = False
            for k in range(len(lists)):
                if curr_node[k] and curr_node[k].val < min_val:
                    min_val = curr_node[k].val
                    min_k = k
                    at_least_one_unfinished = True
            print(f'min k is {min_k}')
            if min_k == -1:
                break

            if curr_node[min_k]:
                new_node = curr_node[min_k]
                curr_node[min_k] = curr_node[min_k].next
                new_node.next = None
                if combined is None:
                    print("came in here")
                    head = combined = new_node
                else:
                    combined.next = new_node
                    combined = combined.next
                print(f'appended {new_node.val}')

        return head
