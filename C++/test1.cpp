#include<iostream>
#include <algorithm>
using namespace std;
int main()
{ 
    int test;
    int a,b,d,n;
    cin>>test;
    while(test>0)
    {
       cin>>a>>b;
       d=std::min(a,b);
       n=std::max(a,b)/d;
       cout<<n;
    }

}