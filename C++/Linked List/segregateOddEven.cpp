#include <iostream>
// #include <conio.h>
#include <bits/stdc++.h>
using namespace std;
// INITIALIZING THE STRUCTURE OF THE LINKED LIST.
struct Node
{
    /* data */
    int data;
    Node *next;
    Node(int d)
    {
        data = d;
        next = NULL;
    }
};
Node *insertAtEnd(Node *head, int x)
{
    Node *temp = new Node(x);
    if (head == NULL)
    {
        return temp;
    }
    Node *curr = head;
    while (curr->next != NULL)
    {
        curr = curr->next;
    }
    curr->next = temp;
    return head;
}
void printlist(Node *head)
{
    Node *curr = head;
    while (curr != NULL)
    {
        cout << curr->data << " ";
        curr = curr->next;
    }
    cout << endl;
}
void segregateEvenOdd(Node *head)
{     
    
    Node *lastnode = head;
    while (lastnode->next != NULL)
    {
        lastnode = lastnode->next;
    } // lastNode= 2
    Node *curr = head;//1
    Node *New_lastNode = lastnode;
    while (curr->data % 2 != 0 && curr != lastnode)
    {                              // 1 3 4 5 7 2
        New_lastNode->next = curr; // first iteration 3 4 5 7 2 1
        curr = curr->next;         // Second iteration 4 5 7 2 1 3
        New_lastNode = New_lastNode->next;
        New_lastNode->next->next = NULL;
    }
    //NOW THE CURR POINTER POINTS TO THE FIRST EVEN NODE.
    Node *prev = NULL;
    if (curr->data % 2 == 0)
    {
        head = curr;             // 4 is the new head
        while (curr != lastnode) // 4 5 7 2 1 3
        {
            /* code */
            if (curr->data % 2 == 0)
            {
                prev = curr;
                curr = curr->next;
            }
            else
            {
                prev->next = curr->next;   // curr= 5 prev=4  same for the second time
                curr->next = NULL;         //5->next=Null     7->next=Null
                New_lastNode->next = curr; //3->next=5        5->next=7
                New_lastNode = curr;       //New_lastnode=5   New_lastnode=7
                curr = prev->next;         // 4 7 2 1 3 5     4 2 1 3 5 7
            }
        }
    }
    prev = head; //4=head;
                 /*
        Now if the end of linked list is a odd number. 
        */
    if (lastNode->data % 2 != 0)
    {
        prev->next = lastnode->next;
        New_lastnode->next = lastnode;
        lastnode->next = NULL;
    }
    printlist(prev);
}

// 1 3 4 5 7 2
int main()
{
    Node *head = NULL;
    int a;
    cout << "No element to be inserted at the end" << endl;
    cin >> a;
    while (a > 0)
    {
        int data;
        cout << "Enter data From Ending"
             << ": ";
        cin >> data;
        cout << endl;
        head = insertAtEnd(head, data);
        a--;
    }
    printlist(head);
    return 0;
}