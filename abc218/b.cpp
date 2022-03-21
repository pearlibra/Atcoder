#include <iostream>
using namespace std;

int main() {
    int p[26];
    for (int i=0; i<26; i++) {
        cin >> p[i];
    }

    for (int i=0; i<26; i++) {
        char alpha = 96 + p[i];
        cout << alpha;
    }
    return 0;
}

