#include <bits/stdc++.h>
using namespace std;

int main() {
    int q;
    cin >> q;
    multiset<int> st;

    // q回ループ回す．毎回デクリメント
    while(q--) {
        int t;
        cin >> t;
        if(t == 1) {
            int x;
            cin >> x;
            st.insert(x); //.insert()で挿入
        } else if(t == 2) {
            int x, c;
            cin >> x >> c;

            // st.find(要素)でイテレータが返ってくるため，最終要素のひとつ後に達していない限りcをデクリメントして一個ずつ消していく
            // st.erase(x)とするとmultiset内のxが全て消えてしまうため，find()を挟む
            while(c-- and st.find(x) != st.end()) {
                st.erase(st.find(x));
            }
        } else {
            // rbegin()で反転したmultisetの最初の要素を指すイテレータ
            // *itrで要素を参照
            cout << *st.rbegin() - *st.begin() << endl;
        }
    }
}
