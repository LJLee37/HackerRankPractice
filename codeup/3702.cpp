#include <bits/stdc++.h>
//not finished
int main()
{
    int inputs[2];
    vector<vector<int>> peopleTable;
    cin >> inputs[0] >> inputs[1];
    for (auto j = 0; j <= i[0]; j++)
    {
        if (peopleTable.size() <= j) peopleTable.push_back(new vector<int>);
        for (auto k = 0; k < i[1]; k++)
        {
            if(peopleTable[j].size() <= k)
            {
                if(j == 0)
                    peopleTable[j].push_back(k + 1);
                 else
                     if (k == 0) peopleTable[i].push_back(1);
                     else peoleTable[j].push_back(peopleTable[j-1][k] + peopleTable[j][k-1]);
            }
        }
    }
}
