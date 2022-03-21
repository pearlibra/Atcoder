#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    int N, X;
    int a;
    cin >> N >> X;
    int sum;


    vector<int> v;

    for (int i=0; i<N; i++) {
        cin >> a;
        v.push_back(a);
    }
    sum = accumulate(v.begin(), v.end(), 0) - N/2;
    if (X >= sum) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}