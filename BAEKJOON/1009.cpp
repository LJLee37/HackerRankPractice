
/*
T = int(input())
for i in range(T):
    li = []
    a, b = map(int,input().split())
    for j in range(b):
        if a ** j in li:
            break
        li.append(a ** j)
    n = b % len(li)
    print(n + 1)
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
    int T = 0;
    cin >> T;
    for (auto i = 0; i < T; i++)
    {
        vector<int> li;
        int a = 0, b = 0;
        cin >> a >> b;
        for (auto j = 0; j < b; j++)
        {
            if (find(li.begin(), li.end(), pow(a, j)) != li.end() or li.back() == pow(a,j))
                break;
            li.push_back(pow(a,j));
        }
        cout << li.size() % b + 1 << endl;
    }
}
