#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;

    long a[N];
    unsigned long long ans = 1;

    for (int i=0; i<N; i++) {
        cin >> a[i];
    }
    sort(a, a+N);

    

    for (int i=0; i<N; i++) {
        ans *= (a[i] - i);
        if (ans >= 1000000007) {
            ans %= 1000000007;
        }
    }
    
    cout << ans << endl;

    return 0;
}