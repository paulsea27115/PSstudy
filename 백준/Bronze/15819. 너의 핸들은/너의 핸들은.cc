#include <iostream>
#include <string>

using namespace std;

bool compare(string s1, string s2){
    return s1 > s2;
}

int main()
{
    int t, a;
    cin >> t >> a;
    
    string* names = new string[t];
    
    for(int i = 0; i < t; ++i)
        cin >> names[i];
    
    string tmp("");
    
    for(int i = 0; i < t; ++i) {
        for(int j = 0; j < t - i - 1; ++j) {
            if(compare(names[j], names[j + 1])) {
                tmp = names[j];
                names[j] = names[j + 1];
                names[j + 1] = tmp;
            }
        }
    }
    
    cout << names[a - 1];
    
    return 0;
}