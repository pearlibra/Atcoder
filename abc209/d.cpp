// failed

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct city{
	int number;

};
int main() {
    int N, Q;
    cin >> N >> Q;
    int road[2][N-1];
    int query[2][Q];
    int c, d;
    int road_n = 0;
    vector<int> v;

    for (int i=0; i<N-1; i++) {
        cin >> road[0][i] >> road[1][i];
    }
    // for (int i=0; i<Q; i++) {
    //     cin >> query[0][i] >> query[1][i];
    // }
    while(cin >> c >> d) {
        int s = ;
        for (int i=0; i<N-1; i++) {
            if (road[0][i] == s) {
                if (road[1][i] == d) {
                    road_n++;
                    return;
                } else {
                    for(int j=0; j<v.size(); j++){
                        if (road[1][i] == v[j]) {
                            break;
                        } else if (j == v.size()) {
                            v.push_back(road[1][i]);
                        }
                    }
                }
            }
        }
        road_n++;
    }
    








    return 0;
}