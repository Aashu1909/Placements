class Solution
{
    public:
    //Function to add two numbers represented by linked list.
    struct Node* addTwoLists(struct Node* first, struct Node* second)
    {
        // code here
        Node*curr=first;
        string s="";
        while(curr!=NULL){
            s+=to_string(curr->data);
            curr=curr->next;
        }
        Node*curr2=second;
        string s2="";
        while(curr2!=NULL){
            s2+=to_string(curr2->data);
            curr2=curr2->next;
        }
        int c=stoi(s)+stoi(s2);
        Node* head=NULL;
        while(c!=0){
            int r=c%10;
            if(head==NULL){
            Node *result=new Node(r);
            head=result;
            }
            else{
                Node *temp=new Node(r);
            temp->next=head;
            head=temp;
            
            }
            c/=10;
        }
        return head;
    }
};