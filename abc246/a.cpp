#include<bits/stdc++.h>
using namespace std;

int main() {
    int x1, y1;
    int x2, y2;
    int x3, y3;
    int x_ans = 0;
    int y_ans = 0;

    cin >> x1 >> y1;
    cin >> x2 >> y2;
    cin >> x3 >> y3;

    if (x1 == x2) {
        x_ans = x3;
        if (y1 == y3) {
            y_ans = y2;
        }
        else {
            y_ans = y1;
        }
    }
    else if  (x2 == x3) {
        x_ans = x1;
        if (y2 == y1) {
            y_ans = y3;
        }
        else {
            y_ans = y2;
        }
    }
    else {
        x_ans = x2;
        if (y1 == y2) {
            y_ans = y3;
        }
        else {
            y_ans = y1;
        }
    }
    cout << x_ans << ' ' << y_ans;
    return 0;
}