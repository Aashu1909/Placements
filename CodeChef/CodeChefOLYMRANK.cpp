// CPP program to demonstrate the
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int tc;
	cin>>tc;
	while(tc--){
	    int arr[6];
	    for (int i =0;i<6;i++){
            cin>>arr[i];
	    }
        int sum_first_three=0,sum_last_three=0;
        int i=0,j=5;
        while(i<3 and j>=3){
            sum_first_three+=arr[i];
            sum_last_three+=arr[j];
            i++;
            j--;
        }
        if(sum_first_three>sum_last_three){
            cout<<"1"<<"\n";
        }
        else{
            cout<<"2"<<"\n";
        }

	    }
	return 0;
}