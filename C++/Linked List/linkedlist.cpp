#include <iostream>
#include<conio.h>
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
/*
Algorithm for inserting element at the begining.
1.Create a temporary node that holds the data provided by the user.
2.Then set the next value of the temporary node as the head of the linked list.
3.Return head pointer.
*/
Node *insertAtBeg(Node *head, int x)
{
    Node *temp = new Node(x);
    temp->next = head;
    return temp;
}
/*
Algorithm for inserting element at the a Given Postion.
1.Create a temporary node that holds the data provided by the user.
2.Create a curr node which helps in traversal of the linked list.
3.Loop till pos-2 set curr=curr->next.
4.Now to have a link with exitising element in the linked list save temp->next=curr->next.
5.Now put the value of temp in Curr->next.
6.return head.
*/
Node *insertAtpos(Node *head,int pos, int x)
{
    Node *temp = new Node(x);
    Node *curr=head;
    for(int i=1;i<=pos-2&& curr!=NULL;i++){
        curr=curr->next;
    }
    temp->next=curr->next;
    curr->next=temp;
    return head;
}
/*
Algorithm for inserting Element at the back of the linked list.
1.Crete a temporary node which holds the data from the user.
2.Check for the valure of Head if it is NUlL return temp node.
3.Now Create a curr node node which hold Head and loop till curr->next=NULL.
4.Then set teh value of Curr->next=temporary node.
5.Return the value of head of link list. 
*/
Node *insertAtEnd(Node *head, int x)
{
    Node *temp = new Node(x);
    if (head ==NULL)
    {
        return temp;
    }
    Node *curr = head;
    while (curr->next!= NULL)
    {
        curr = curr->next;
    }
    curr->next = temp;
    return head;
}
/*
Algorithm for deleting a node from the begining.
1.Check for head value if it is NULL return NULL.
2.IF the value at the head is not NULL.
3.Create a temporary pointer which holds the next of the head.
4.Delete head and return temp as the new head.
*/
Node *deleteNodeBeg(Node *head){
    if(head==NULL){
        return NULL;
    }
    else{
        Node *temp=head->next;
        delete (head);
        return temp;
    }
}
/*
Algorithm for deleting a node from the Ending og the linked list.
1.Check for head value if it is NULL return NULL.
2.IF the value at the head is not NULL.
3.Create a current pointer fro traversing the linked list.
4.Traverse till next of the current->next is NUll i.e Curr->next->next==NULL.
5.Delete Curr->next and set curr->next as NULL.
6.Return the head pointer.
*/
Node *deleteNodeEnd(Node *head){
    if(head==NULL){
        return NULL;
    }
    else{
        Node *curr=head;
        while(curr->next->next!=NULL){
            curr=curr->next;
        }
        delete (curr->next);
        curr->next=NULL;
        return head;
    }
}
/*
Algorithm for Traversing through the linked list.
1. Crete a Node varaible named as Current which hold the value of Head.
2.Loop till curr=Null
3.Print the data curr->data
4 increment thre loop curr=curr->next;
*/
void printlist(Node *head)
{
    Node *curr = head;
    while (curr!= NULL)
    {
        cout << curr->data <<" ";
        curr = curr->next;
    }
    cout<<endl;
}
int main(){
    Node *head = NULL;
    // char ch;
    int n;
    cout << "No element to be inserted at the Beg"<< ": ";
    cin >> n;
    cout << endl;
    while (n > 0)
    {
        int data;
        cout << "Enter data From Begining"  << ": ";
        cin >> data;
        cout << endl;
        head = insertAtBeg(head, data);
        n--;      
    }
    printlist(head);
    int a;
    cout << "No element to be inserted at the end" << endl;
    cin >> a;
    while (a > 0)
    {
        int data;
        cout << "Enter data From Ending"<< ": ";
        cin >> data;
        cout << endl;
        head = insertAtEnd(head, data);
        a--;
    }
    printlist(head);
    int pos,data;
    cout<<"Enter at spsecific pos:";
    cin>>pos;
    cout<<"\nEnter data:";
    cin>>data;
    cout<<endl;
    head=insertAtpos(head,pos,data);
    printlist(head);
    cout<<"\nNow deleting from beg."<<endl;
    head=deleteNodeBeg(head);
    printlist(head);
    cout<<"\nNow deleting from End."<<endl;
    head=deleteNodeEnd(head);
    printlist(head);
    return 0;
}