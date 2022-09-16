#include <iostream>
#define TRUE 1
#define FALSE 0
using namespace std;
int n;
bool isprime(int n)
{   if(n==1) {return FALSE;}
    if (n==2||n==3) {return TRUE;}
    if (n%2==0||n%3==0) {return FALSE;}
    for(int i=5;i*i<n;i++){
        if (n%i==0)
        return FALSE;
    }
        return TRUE;

}
int primefactor(int a){
    for(int j=2; j<=a; j++)
    {
        if(a%j==0&&isprime(j))
        {
            return j;
        }
    }
    return -1;
}
int main()
{
    int b,c;
    cout<<"enter the number: ";
    cin>>n;
    c=primefactor(n);
    cout<<c;
    return 0;
}
