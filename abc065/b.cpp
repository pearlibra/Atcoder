#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int a[N + 1];
    bool mem[N + 1] = {false};
    for(int i = 1; i <= N; i++) {
        cin >> a[i];
    }

    int cnt = 0;
    int next = 1;
    while(next != 1 or cnt == 0) {
        next = a[next];
        if(mem[next] == true) {
            break;
        } else {
            mem[next] = true;
            cnt++;
            if(next == 2) {
                cout << cnt << endl;
                exit(0);
            }
        }
    }

    cout << -1 << endl;

    return 0;
}