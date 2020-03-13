#include <bits/stdc++.h>

using namespace std;

// Complete the staircase function below.
void staircase(int n) {
    string output = "#";
    for (int i = 0; i < n; i++)
    {
        cout << right << setw(n) << setfill(' ') << output << endl;
        output.append("#");
    }
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}
