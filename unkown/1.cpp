#include <bits/stdc++.h>
int main()
{
    int n;
    cin >> n;
    vector<vector<int>> inputs;
    vector<vector<int>> peopleTable;
    for(auto i = 0; i < n; i++)
    {
        vector<int> aInput;
        for(auto j = 0; j < 2; j++)
        {
            int temp;
            cin>>temp;
            aInput.push_back(temp);
        }
        inputs.push_back(aInput);
    }
    
    for (auto& i : inputs)
    {
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
            cout << peopleTable[i[0] + 1][i[1]] << “ “;
       }
}
