#include <iostream>
#include <string>
using namespace std;
int main()
{
    int a = 0, a1 = 0, a2 = 0, a3 = 0, a4 = 0, a5 = 0, a6 = 0, a7 = 0, a8 = 0, a9 = 0;
    string str;
    std::cin >> str;
    int s_len = str.length();
    for (int i = 0; i < s_len; i++)
    {

        if (str[i] == 0)
        {
            a++;
        }
        else if (str[i] == 1)
        {
            a1++;
        }

        else if (str[i] == 2)
        {
            a2++;
        }
        else if (str[i] == 3)
        {
            a3++;
        }

        else if (str[i] == 4)
        {
            a4++;
        }

        else if (str[i] == 5)
        {
            a5++;
        }

        else if (str[i] == 6)
        {
            a6++;
        }

        else if (str[i] == 7)
        {
            a7++;
        }

        else if (str[i] == 9)
        {
            a9++;
        }
    }

    std::cout << "0" << a << endl;
    std::cout << "1" << a1 << endl;
    std::cout << "2" << a2 << endl;
    std::cout << "3" << a3 << endl;
    std::cout << "4" << a4 << endl;
    std::cout << "5" << a5 << endl;
    std::cout << "6" << a6 << endl;
    std::cout << "7" << a7 << endl;
    std::cout << "8" << a8 << endl;
    std::cout << "9" << a9 << endl;
}