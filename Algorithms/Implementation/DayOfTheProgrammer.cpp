#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

// Complete the dayOfProgrammer function below.
string dayOfProgrammer(int year) {
    //1. 윤년 계산.
    //2. 더해서 256번째 날짜 구하기.
    //3. DD.MM.YYYY.
    //4. YYYY = year.

    //그레고리력과 율리우스력의 차이.

    bool yun = false;
    if (!(year % 4))
    {
        if (!(year % 100))
        {
            if (year < 1918)
                yun = true;
            else
            if(!(year % 400))
                yun = true;
        }
        else
            yun = true;
    }
    //더해서 256 : 31 + 28(29) + 31 + 30 + 31 + 30 + 31 + 31 = 243(244)
    //243 + 13 = 256
    //244 + 12 = 256
    string retval = (year == 1918 ? (string)"26" : (yun ? (string)"12" : (string)"13")) + ".09." + to_string(year);
    return retval;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string year_temp;
    getline(cin, year_temp);

    int year = stoi(ltrim(rtrim(year_temp)));

    string result = dayOfProgrammer(year);

    fout << result << "\n";

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
