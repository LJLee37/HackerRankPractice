#include <iostream>
using namespace std;
int main()
{
    long long A, B, V, N;
    cin >> A >> B >> V;
    long long tmp1 = V - A, tmp2 = A - B;
    N = tmp1 / tmp2;
    if(tmp1 % tmp2)
        N++;
    cout << N;
}
