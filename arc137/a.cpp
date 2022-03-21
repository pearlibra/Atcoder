#include<bits/stdc++.h>
using namespace std;

long long GCD(long long a, long long b) {
    if (b == 0) return a;
    else return GCD(b, a % b);
}

int main() {
    unsigned long long l, r, t;
    cin >> l >> r;

    for (int i = 0; i < r-l; i++) {
        for (int j = 0; j <= i; j++) {
            t = GCD(r-j, l+i-j);
            if (t == 1) {
                cout << r - l - i << endl;
                return 0;
            }
        }
    }
}