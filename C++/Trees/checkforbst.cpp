#include<iostream>
#include<bits/stdc++.h>
using namespace std;
struct Node
{
    /* data */
    int key;
    Node*left;
    Node*right;
    Node(int x){
        key=x;
        left=NULL;
        right=NULL;
    }
};
int maximumkey(Node *root){
    if(root==NULL){
        return INT_MIN;
    }
    return max(root->key,max(maximumkey(root->left),maximumkey(root->right)));

}
int minimumkey(Node*root){
    if(root==NULL){
        return INT_MAX;
    }
    return min(root->key,min(minimumkey(root->left),minimumkey(root->right)));
}


bool isBST(Node*root){
    int x=INT_MIN;
    int y=INT_MAX;
    if(root==NULL){
        return true;
    }
    if(root->left!=NULL){
         x=maximumkey(root->left);
    }
    if(root->right!=NULL){
         y=minimumkey(root->right);
    }
    if(x<root->key&&root->key<y){
        return true;
    }
    return false;

}
int main(){

	Node *root = new Node(20);  
    root->left = new Node(8);  
    root->right = new Node(30);  
    root->right->left = new Node(18);  
    root->right->right = new Node(35);  
    int x=maximumkey(root->left);
    int y=minimumkey(root->right);
    cout<<x<<" max "<<y<<" min \n";
    if(isBST(root))  
        cout<<"Is BST";  
    else
        cout<<"Not a BST";  
          
    return 0;  
}