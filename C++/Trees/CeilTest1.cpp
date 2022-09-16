#include <bits/stdc++.h>
using namespace std;
int Min=INT_MIN;
struct Node  
{ 
  int key; 
  struct Node *left; 
  struct Node *right; 
  Node(int k){
      key=k;
      left=right=NULL;
  }
};
void Inorder(Node *root,int x){
    if(root!=NULL){
        Inorder(root->left,x);
        if(root->key==x){
          Min=root->key;
        }
        else if(root->key>x){
            if(Min==INT_MIN){
                Min=max(root->key,Min);
            }
            Min=min(root->key,Min);
        }
        Inorder(root->right,x);
    }
}
Node *ceil(Node *root, int x){
    Node *res=NULL;
    while(root!=NULL){
        if(root->key==x)
            return root;
        else if(root->key<x)
            root=root->right;
        else{
            res=root;
            root=root->left;
        }
    }
    return res;
} 

int main(){
	
	Node *root=new Node(10);                                 
	root->left=new Node(5);
	// root->left->left=new Node(3);
	root->right=new Node(15);
	root->right->left=new Node(12);
	// root->right->left->left=new Node(16);
	root->right->right=new Node(30);
	// int x=1;
    
    /*
        15
       / \
     5    20
    /    /  \
   3   18    80
      /
    16 
    */ 

	cout<<"Ceil: "<<(ceil(root,14)->key);
    cout<<endl;
    Inorder(root,14);
    cout<<"Ceil int: "<<Min<<endl;
}