//A + Bn < Cn
//A < Cn - Bn
//A / (C - B) < n (C > B)
//A + Bn - Cn < 0
//1000 80 170
//1000 / (170 - 80)
//문제는 제대로 읽자... -1을 안해서 얼마나 고생한거냐... feat. line 16
#include <iostream>
using namespace std;
int main()
{
    unsigned int a, b, c, n;
    cin >> a >> b >> c;
    if (b >= c)
    {
        cout << -1;
        return 0;
    }
    n = a / (c - b) + 1;
    cout << n;
    return 0;
}
