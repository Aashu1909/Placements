#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string str;
    cin >> str;
    int n = str.length();
    if (isupper(str[0]))
    {
        if (n == 1)
        {
            str[0] = tolower(str[0]);
        }
        else
        {
            for (int i = 1; i < n; i++)
            {
                str[i] = tolower(str[i]);
            }
        }
    }
    else
    {
        str[0] = toupper(str[0]);
        for (int i = 1; i < n; i++)
        {
            str[i] = tolower(str[i]);
        }
    }

    cout << str;
    return 0;
}