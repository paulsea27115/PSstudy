#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    vector<string> v;
    
    int t;
    cin >> t;
    
    for(int i = 0; i < t; i++) {
        string s;
        cin >> s;
        
        v.emplace_back(s);
    }
    
    int res = 0;
    
    for(int i = 0; i < v[0].length(); i++) {
        bool same = false;
        for(int j = 0; j < t - 1; j++) {
            for(int n = j + 1; n < t; n++) {
                if(v[j].substr(v[j].length() - i - 1, i + 1) == v[n].substr(v[n].length() - i - 1, i + 1)) {
                    same = true;
                    break;
                }
            }
            if(same) {
               break; 
            }
        }
        if(!same) {
            res = i + 1;
            break;
        }
    }
    
    cout << res;

    return 0;
}