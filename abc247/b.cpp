#include<bits/stdc++.h>
using namespace std;
 
int main() {
    int n;
    cin >> n;
    string s[n], t[n];
 
    for (int i = 0; i < n; i++) {
        cin >> s[i] >> t[i];
    }
 
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                continue;
            }
            if (s[i] == s[j] || s[i] == t[j]) {
                for (int k = 0; k < n; k++) {
                    if (i == k) {
                        continue;
                    }
                    if (t[i] == s[k] || t[i] == t[k]) {
                        cout << "No" << endl;
                        return 0;
                    }
                }
            }
        }
    }
 
    cout << "Yes" << endl;
 
    return 0;
}