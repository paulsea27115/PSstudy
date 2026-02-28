#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    vector<pair<int, int>> v;
    vector<double> res;
    
    for(int i = 0; i < t; i++) {
        int a, b;
        cin >> a >> b;
        
        v.emplace_back(make_pair(a, b));
    }
    
    for(int i = 0; i < t - 2; i++) {
        for(int j = i + 1; j < t - 1; j++) {
            for(int n = j + 1; n < t; n++){
                res.emplace_back((double)abs(v[i].first*v[j].second+v[j].first*v[n].second+v[n].first*v[i].second-(v[i].second*v[j].first+v[j].second*v[n].first+v[n].second*v[i].first)) / 2);
            }
        }
    }
    cout.precision(9);
    cout << *max_element(res.begin(), res.end());
    return 0;
}