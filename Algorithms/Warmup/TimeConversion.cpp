#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the timeConversion function below.
 */
string timeConversion(string s) {
    char AMPM = s[8];
    string retval;
    if(AMPM - 'A')
        if(s.substr(0,2) == "12")
            retval.append(s.substr(0,2));
        else
            retval.append(to_string(stoi(s.substr(0,2)) + 12));
    else
        if(s.substr(0,2) == "12")
            retval.append("00");
        else
            retval.append(s.substr(0,2));
    retval.append(s.substr(2,6));
    return retval;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
