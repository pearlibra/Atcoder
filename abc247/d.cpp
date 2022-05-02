#include<bits/stdc++.h>
using namespace std;
 
int main() {
    int n;
    cin >> n;
    int q_num, x, c;
    vector<vector<long long>> v(n, vector<long long>(2, 0));
    unsigned long long sum = 0;
    int head, tail = 0;
 
    for (int i = 0; i < n; i++) {
        cin >> q_num;
        if (q_num == 1) {
            cin >> x >> c;
            v[tail][0] = x;
            v[tail][1] = c;
            tail++;
        }
        else if (q_num == 2) {
            cin >> c;
            while (c > 0) {
                if (v[head][1] > c) {
                    v[head][1] -= c;
                    sum += v[head][0] * c;
                    c = 0;
                }
                else if (v[head][1] == c) {
                    sum += v[head][0] * c;
                    head++;
                    c = 0;
                }
                else {
                    sum += v[head][0] * v[head][1];
                    c -= v[head][1];
                    head++;
                }
            }
            cout << sum << endl;
            sum = 0;
        }
    }
    return 0;
}