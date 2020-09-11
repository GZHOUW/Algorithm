/*
Reverse a singly linked list.

Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
 */

#include <iostream>
 
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

    void printList() {
        ListNode* s = this;
        while (s) {
            cout << s->val << endl;
            s = s->next;
        }
    }
};

class Solution {
public:
    ListNode* reverseListRec(ListNode* head) {
        // If reached the end, the cur (last) node becomes the newHead  (line 32)
        if (!head || !head->next) { // head and next are both pointers to ListNode
            return head;
        }

        ListNode* n = head->next; // head -> next is equivalent to *head.next
        ListNode* newHead = reverseListRec(n); // keep recursing until return the last node (line 28), WONT change once set

        // newHead->5, n->4, head->3
        n->next = head; 
        head->next = NULL;

        return newHead;
        

    }
};

int main() {
    ListNode L =ListNode(3, &ListNode(4, &ListNode(5)));
    Solution s = Solution();
    ListNode* reversedL = s.reverseListRec(&L);
    reversedL->printList();
}