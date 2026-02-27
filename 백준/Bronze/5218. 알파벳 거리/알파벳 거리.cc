#include <iostream>
#include <string>
#include <map>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cin >> t;
    map<char, int> m;
    
    for(int i = 0; i < 26; i++) m.insert({static_cast<char>(i+65), i+1});
    
    for(int i = 0; i < t; i++) {
        string s1, s2;
        cin >> s1 >> s2;
        
        cout << "Distances:";
        
        for(int j = 0; j < s1.length(); j++) {
            int n = m[s2[j]] - m[s1[j]];
            cout << " " << (n < 0 ? 26 + n: n);
        }
        
        cout << "\n";
    }

    return 0;
}