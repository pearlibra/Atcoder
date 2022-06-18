#include <bits/stdc++.h>
using namespace std;

long long sum_1_to_n(long long n) { return n * (n + 1) / 2; }

int main() {
    long long n, a, b;
    cin >> n >> a >> b;

    cout << sum_1_to_n(n) - sum_1_to_n(n / a) * a - sum_1_to_n(n / b) * b +
                sum_1_to_n(n / lcm(a, b)) * lcm(a, b)
         << endl;

    return 0;
}