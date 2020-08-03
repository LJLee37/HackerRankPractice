//A : 5m, B : 1m, C : 10s
//A : 300s, B : 60s, C : 10s
//if (input % 10)
//{
//    cout << -1;
//    return 0;
//}
#include <iostream>
using namespace std;
int main()
{
    const int button[3] = {300, 60, 10};
    int input;
    cin >> input;
    if (input % 10)
    {
        cout << -1;
        return 0;
    }
    for (const auto& i : button)
    {
        cout << input / i << ' ';
        input %= i;
    }
    return 0;
}
