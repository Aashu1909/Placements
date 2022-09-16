#include<iostream>
using namespace std;

class List
{
    struct Node{
        int item;
        Node *next;
    };
    Node *start;
    Node* Search(int value)
    {
        Node *temp = start;
        for(int i; temp!=NULL ; i++){
            if(temp->item == value)
                return temp;
            temp = temp->next;
        }
        return NULL;
    }
public:
    List(){
        start = NULL;
    }
    void View();
    void Append(int);
    void InsertFirst(int);
    void InsertAfter(int, int);
    void DeleteFirst();
    void DeleteLast();
    void DeleteNode(int);

};



void List::View()
{
    Node *temp =start;
    while(temp != NULL){
        cout<<temp->item<<" ";
        temp = temp->next;
    }
}
void List::InsertFirst(int value)
{
    Node *n = new Node;
    n->item = value;
    n->next = start;
    start = n;
}

void List::Append(int value)
{
    Node *n = new Node;
    n->item = value;
    n->next = NULL;
    Node *temp = start;
    if(start == NULL)
        start = n;
    else{
        while(temp->next != NULL)
            temp = temp->next;
        temp->next = n;
    }
}

void List::DeleteFirst()
{
   if(start == NULL)
       cout<<"UnderFlow";
   else{
        struct Node *temp = start;
        start = temp->next;
        delete temp;
   }

}

void List::DeleteLast()
{
   if(start == NULL)
        cout<<"UnderFlow";
   else if(start->next == NULL)
        DeleteFirst();
   else{
        Node *temp = start, *ttemp = NULL;
        while(temp->next != NULL){
            ttemp = temp;
            temp = temp->next;
        }
        ttemp->next = NULL;
        delete temp;
   }

}

void List::DeleteNode(int value)
{
    Node *temp = start, *ttemp = NULL;
    if(temp == NULL)
        cout<<value<<" not Found in List";
    else{
        while(temp->item != value){
            ttemp = temp;
            temp = temp->next;
        }
        if(ttemp == NULL)
            DeleteFirst();
        else{
            ttemp->next = temp->next;
            delete temp;
        }
    }
}

void List::InsertAfter(int value, int newValue)
{
    Node *temp = Search(value);
    if(temp == NULL)
        cout<<value<<" doesn't Exist";
    else{
        Node *n = new Node;
        n->item = newValue;
        n->next = temp->next;
        temp->next = n;
    }
}

int main()
{
    List l1;
    l1.Append(10);
    l1.Append(20);
    l1.Append(30);
    l1.InsertFirst(5);
    l1.InsertAfter(30, 40);
    l1.InsertAfter(20, 25);
    l1.View();
    cout<<endl<<"After deleting 1st ";
    l1.DeleteFirst();
    l1.DeleteLast();
    l1.DeleteNode(20);
    l1.View();
}