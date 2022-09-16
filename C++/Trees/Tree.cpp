#include<iostream>
#include<bits/stdc++.h>
using namespace std; 
int MAX=0;
class Node{
     public:
     int data;
     Node *left;
     Node *right;
     Node(int x){
         data=x;
         left=NULL;
         right=NULL;
     }
 };
class Tree{
public:
void Inorder(Node*);
void Preorder(Node*);
void Postorder(Node*);
int hieght(Node*);
void knode(Node*,int);
int size(Node*);
void leftview(Node*);
bool isBalanced(Node*);
int width(Node*);
Node* constructBinaryTree(int[],int[],int,int);
void spiratTraverse(Node*);
int NumberofNode(Node*);
int longestpath(Node*);
int maximumKey(Node*);
void maximumKeyInorder(Node*);
bool childrenSum(Node*);
};

void Tree::Inorder(Node *root){
   
    if(root!=NULL){
        Inorder(root->left);
        cout<<root->data<<" ";
        Inorder(root->right);
    }
}
void Tree::Preorder(Node *root){
    
    if(root!=NULL){
        cout<<root->data<<" ";
        Preorder(root->left);
        Preorder(root->right);
    }
}
void Tree::Postorder(Node *root){
    
    if(root!=NULL){
        Postorder(root->left);
        Postorder(root->right);
        cout<<root->data<<" ";
    }
}
int Tree::hieght(Node *root){
    if(root==NULL){
        return 0;
    }
    return 1+ std::max(hieght(root->left),hieght(root->right));
}
void Tree::knode(Node *root,int k){
    if(root==NULL){
        cout<<"Root is NUll";
        return;
    } 
    if(k==0){
        cout<<root->data<<" ";
    }
    else{
        knode(root->left,k-1);
        knode(root->right,k-1);
    }
}
int Tree::size(Node*root){
    if(root==NULL){
        return 0;
    }
    return 1+size(root->left)+size(root->right);
}
int Tree::maximumKey(Node*root){
    if(root==NULL){
        return 0;
    }
    return std::max(root->data,std::max(maximumKey(root->left),maximumKey(root->right)));
}
int Tree::NumberofNode(Node *root){
    if (root==NULL){
        return 0;
    }
    return 1+NumberofNode(root->left)+NumberofNode(root->right);
}
int Tree::longestpath(Node *root){
    if(root==NULL){
        return 0;
    }
    int lh=hieght(root->left);
    int rh=hieght(root->right);
    return 1+max(lh+rh,max(longestpath(root->left),longestpath(root->right)));
}
bool Tree::childrenSum(Node* root){
    if(root==NULL){
        return true;
    }
    if (root->left==NULL&&root->right==NULL){
        return true;
    }
    int sum=0;
    if(root->left!=NULL){
        sum+=root->left->data;
    }
    
    if(root->right!=NULL){
        sum+=root->right->data;
    }
    return root->data==sum&&childrenSum(root->left)&&childrenSum(root->right);
}
bool Tree::isBalanced(Node* root){
    if(root==NULL){
        return true;
    }
    int lh=hieght(root->left);
    int rh=hieght(root->right);
    return abs(lh-rh)<=1&&isBalanced(root->left)&&isBalanced(root->right);
}
void Tree::maximumKeyInorder(Node*root){
    if (root!=NULL)
    {
        maximumKeyInorder(root->left);
        MAX=max(root->data,MAX);
        maximumKeyInorder(root->right);
    }
}
    

int main() {
	Tree tree1;
	Node *root=new Node(10);
	root->left=new Node(20);
	root->right=new Node(30);
	root->right->left=new Node(40);
	root->right->right=new Node(50);
	tree1.Preorder(root);
    cout<<endl;
    tree1.Inorder(root);
    cout<<endl;
    cout<<"Longest path:"<<tree1.longestpath(root);
    cout<<"\nis balanced:"<<tree1.isBalanced(root);
    cout<<"\nchildren sum:"<<tree1.childrenSum(root);
    cout<<"\nNumber of node:"<<tree1.NumberofNode(root);
    tree1.maximumKeyInorder(root);
    cout<<"\nLargest element in the tree INORDER:"<<MAX;
    cout<<"\nLargest element in the tree:"<<tree1.maximumKey(root);
}