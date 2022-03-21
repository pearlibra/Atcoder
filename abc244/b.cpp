#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    char t[n];
    char front = 0;
    int x = 0, y = 0;
    for (int i = 0; i < n; i++) {
        cin >> t[i];
        if (t[i] == 'S') {
            if (front == 0) {
                x++;
            }
            else if (front == 1) {
                y--;
            }
            else if (front == 2) {
                x--;
            }
            else {
                y++;
            }
        }
        else {
            front = (front + 1) % 4;
        }
    }

    cout << x << " " << y << endl;
    return 0;
}