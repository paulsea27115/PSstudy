#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >> t;
    
    vector<int> v;
     
    for(int i = 0; i < t; i++) {
        int a;
        cin >> a;
        
        v.emplace_back(a);
    }
    
    auto check = minmax_element(v.begin(), v.end());
    
    cout << (v[0] == *check.first ? "ez" : v[0] == *check.second ? "hard" : "?");

    return 0;
}