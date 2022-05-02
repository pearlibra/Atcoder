#include<bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c, d, e, f, x;
    cin >> a >> b >> c >> d >> e >> f >> x;
    int sum_t = 0;
    int sum_a = 0;

    int tmp = x;
    while (tmp > 0) {
        if (tmp / a > 0) {
            sum_t += a*b;
            tmp -= a;
        }
        else {
            sum_t += tmp*b;
            tmp = 0;
        }
        if (tmp / c > 0) {
            tmp -= c;
        }
        else {
            tmp = 0;
        }
    }
    while (x > 0) {
        if (x / d > 0) {
            sum_a += d*e;
            x -= d;
        }
        else {
            sum_a += x*e;
            x = 0;
        }
        if (x / f > 0) {
            x -= f;
        }
        else {
            x = 0;
        }
    }

    if (sum_t > sum_a) {
        cout << "Takahashi" << endl;
    }
    else if (sum_t == sum_a) {
        cout << "Draw" << endl;
    }
    else {
        cout << "Aoki" << endl;
    }
    return 0;
}