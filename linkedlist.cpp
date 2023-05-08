/**
 * 
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* temp = head;
        int total =0;
        int counter = 0;
        while (temp != nullptr){
            temp = temp->next;
            total++;
        }
        std::cout << counter << std::endl;
        while (head != nullptr){
            if (((total)/2) == counter){
                return head;
            }
            head= head->next;
            counter++;
        }
        // std::cout << counter;
        return head;
    }
};