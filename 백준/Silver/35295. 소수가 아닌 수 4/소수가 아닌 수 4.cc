#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool check_n(int a) {
    for(int i = 2; i <= sqrt(a); i++) {
        if(a % i == 0) return false;
    }
    
    return true;
}

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
    
    if(v.size() == 2 && v[0] + v[1] > v[0] * v[1] && check_n(v[0] * v[1])) {
        cout << "NO";
    } else {
        cout << "YES\n" << v.size() << "\n";
        for(int i = 0; i < v.size(); i++)
            cout << v[i] << " ";
    }

    return 0;
}