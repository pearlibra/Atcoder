#include<bits/stdc++.h>
using namespace std;
 
string make_progression(int n) {
    if (n == 1) {
        return to_string(1);
    }
    else {
        return make_progression(n-1) + " " + to_string(n) + " " + make_progression(n-1);
    }
}
 
int main() {
    int n;
    cin >> n;
 
    cout << make_progression(n) << endl;
    
    return 0;
}