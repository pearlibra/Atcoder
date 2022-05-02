#include<bits/stdc++.h>
using namespace std;

int main() {
    double a, b;
    cin >> a >> b;
    double x, y;

    x = a / sqrt(a*a + b*b);
    y = b / sqrt(a*a + b*b);

    cout << x << ' ' << y;
    return 0;
}