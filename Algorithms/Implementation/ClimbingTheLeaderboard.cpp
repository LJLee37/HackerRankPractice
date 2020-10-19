#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'climbingLeaderboard' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY ranked
 *  2. INTEGER_ARRAY player
 */

int bs(const vector<int>& arr, int n, int bsR)
{
    int bsLeft = 0, bsRight = bsR, bsCurrent = (bsLeft + bsRight) / 2;
    while (!(n >= arr[bsCurrent] && n < arr[bsCurrent - 1]))
    {
        if (bsLeft == bsRight)
            return bsLeft;
        if (bsLeft > bsRight)
            return -1;
        if (bsRight - bsLeft == 1)
        {
            if (n >= arr[bsRight] && n < arr[bsLeft])
                return bsRight;
            else if (n >= arr[bsLeft] && n < arr[bsLeft - 1])
                return bsLeft;
            else
                return -1;
        }
        if (n == arr[bsCurrent])
            return bsCurrent;
        if (n >= arr[bsCurrent])
            bsRight = bsCurrent;
        else
            bsLeft = bsCurrent;
        bsCurrent = (bsLeft + bsRight) / 2;
    }
    return bsCurrent;
}
int bsRecursive(const vector<int>& arr, const int& n)
{
    if (arr.size() <= 2)
    {
        if (arr[0] <= n)
            return 0;
        else
            return 1;
    }
    int current = arr.size() / 2 - !(arr.size() % 2);
    if (arr[current] >= n && n < arr[current - 1])
        return current;
    if (n >= arr[current])
        return bsRecursive(vector<int>(arr.cbegin(), (arr.size() % 2) + arr.cend() - current), n);
    else
        return 1 + current + bsRecursive(vector<int>(arr.cbegin() + current + (arr.size() % 2) + 1, arr.cend()), n);
}

vector<int> climbingLeaderboard(vector<int> ranked, vector<int> player) {
    vector<int> retval;
    sort(ranked.begin(), ranked.end());
    ranked.erase(unique(ranked.begin(), ranked.end()), ranked.end());
    reverse(ranked.begin(), ranked.end());
    //int prevIndex = ranked.size() - 1;
    for (auto i : player)
    {
        if (i <= ranked.back())
        {
            if (i != ranked.back())
                ranked.push_back(i);
            retval.push_back(ranked.size());
            //prevIndex = ranked.size() - 1;
            continue;
        }
        if (i >= ranked[0])
        {
            if (i != ranked[0])
            {
                ranked.clear();
                ranked.push_back(i);
            }
            retval.push_back(1);
            //prevIndex = 0;
            continue;
        }
        auto bsCurrent = /*bs(ranked, i, prevIndex)*/bsRecursive(ranked, i);
        ranked.resize(bsCurrent + 1);
        if (i != ranked.back())
        {
            ranked.pop_back();
            ranked.push_back(i);
        }
        retval.push_back(bsCurrent + 1);
        //prevIndex = bsCurrent;
    }
    return retval;
}


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string ranked_count_temp;
    getline(cin, ranked_count_temp);

    int ranked_count = stoi(ltrim(rtrim(ranked_count_temp)));

    string ranked_temp_temp;
    getline(cin, ranked_temp_temp);

    vector<string> ranked_temp = split(rtrim(ranked_temp_temp));

    vector<int> ranked(ranked_count);

    for (int i = 0; i < ranked_count; i++) {
        int ranked_item = stoi(ranked_temp[i]);

        ranked[i] = ranked_item;
    }

    string player_count_temp;
    getline(cin, player_count_temp);

    int player_count = stoi(ltrim(rtrim(player_count_temp)));

    string player_temp_temp;
    getline(cin, player_temp_temp);

    vector<string> player_temp = split(rtrim(player_temp_temp));

    vector<int> player(player_count);

    for (int i = 0; i < player_count; i++) {
        int player_item = stoi(player_temp[i]);

        player[i] = player_item;
    }

    vector<int> result = climbingLeaderboard(ranked, player);

    for (int i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}

