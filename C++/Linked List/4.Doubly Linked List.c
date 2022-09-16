#include<stdio.h>
#include<stdlib.h>
struct Node
{
    struct Node *prev;
    int item;
    struct Node *next;
};
void Append(struct Node **s, int value)
{
    struct Node *n = (struct Node*)malloc(sizeof(struct Node));
    n->item = value;
    n->next = NULL;
    if(*s == NULL)
}
