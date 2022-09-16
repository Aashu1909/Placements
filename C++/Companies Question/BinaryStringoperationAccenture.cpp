#include<iostream>
using namespace std;
int OperationsBinaryString(char* str)
{
	int len=0;
	int ans= int(str[0]-'0');
    cout<<ans;
	for(len=0;str[len]!='\0';len++);
	for(int i=1;i<len-1;i+=2)
	{
		int j=i+1;
		if(str[i]=='A')
		{   cout<<ans<<"&"<<str[j]<<":";
			ans = ans & int(str[j]-'0');
            cout<<ans<<endl;
		}
		else if(str[i]=='B')
		{
			cout<<ans<<"|"<<str[j]<<":";
			ans = ans | int(str[j]-'0');
            cout<<ans<<endl;
		}
		else if(str[i]=='C')
		{
			cout<<ans<<"^"<<str[j]<<":";
			ans = ans ^ int(str[j]-'0');
            cout<<ans<<endl;
		}
	}
	return ans;
} 
int main()
{
	char str[100];
	scanf("%s",str);
	cout<<OperationsBinaryString(str);
}