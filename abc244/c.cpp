#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, a;
    cin >> n;
    int buff[2001] = {0};
    buff[n-1] = 1;
    cout << n << endl;
    
    cin >> a;
    while (a > 0) {
        buff[a-1] = 1;
        for (int i = 0; i < 2001; i++) {
            if (buff[i] == 0) {
                cout << i + 1 << endl;
                buff[i] = 1;
                break;
            }
        }
        cin >> a;
    }
    return 0;
}

