#include<iostream>
using namespace std;
bool CheckPassword(char str[],int len){
    bool checkNum=false;
    bool isCapital=false;
    bool startNum=false;
    bool hasSlash=false;
    bool Checklen=false;
    if(len<4){
        Checklen=true;
    }
    if(str[0]>='0'&& str[0]<='9'){
        startNum=true;
    }
    for(int i=1;i<len;i++){
        cout<<str[i];
        if(str[i]>='A'&&str[i]<='Z'){
            isCapital=true;
        }
        else if(str[i]=='/'||str[i]==' '){
            hasSlash=true;
        }
        else if(str[i]>='0'&&str[i]<='9'){
            checkNum=true;
        }
    }
    cout<<"\n";
    cout<<"StartNUM:"<<!startNum<<"\nhasSlash:"<<!hasSlash<<"\ncapital:"<<isCapital<<"\nCHeclklen:"<<!Checklen<<"\nCheckNUM:"<<checkNum<<"\n";
    return !startNum && !hasSlash && isCapital && !Checklen && checkNum;
}

int main()
{
	char str[100];
	scanf("%[^\n]s",str);
	int len=0;
	for(len=0;str[len]!='\0';len++);
	cout<<CheckPassword(str,len);
}