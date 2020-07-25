#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int main()
{
    int len = 0;
    string num;
    cin >> len;
    cin >> num;
    int count = 0;
    reverse(num.begin(), num.end());
    for (auto i = 0; i < num.length(); i++)
    {
        if (i && !((i - count) % 3))
        {
            num.insert(i,",");
            i++;
            count++;
        }
    }
    reverse(num.begin(), num.end());
    cout << num;
    return 0;
}
