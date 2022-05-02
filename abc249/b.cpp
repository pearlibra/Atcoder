#include<bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int tmp = 0;

    sort(s.begin(), s.end());

    for (int i = 0; i < s.length(); i++) {
        if (i == 0) {
            if (int(s[i]) > 90) {
                cout << "No" << endl;
                return 0;
            }
        }
        else if (i == s.length() - 1) {
            if (int(s[i]) <= 90) {
                cout << "No" << endl;
                return 0;
            }
        }
        else {
            if (tmp == int(s[i])) {
                cout << "No" << endl;
                return 0;
            }
        }
        tmp = int(s[i]);
    }
    cout << "Yes" << endl;

    return 0;
}