#include <iostream>
#include <string>

using namespace std;

string star(int t){
    int half = t / 2;
    string ans("");
    
    for(int i = 0; i < t; i++) {
        ans += "*";
    }
    
    ans += "\n";
    
    for(int i = 0; i < half + 1; i++) {
        for(int j = 0; j < i + half; j++) {
            if(half - i == j) ans += "*";
            else ans += " ";
        }
        
        ans += "*\n";
    }
    
    return ans;
}

int main()
{
    int t;
    cin >> t;
    
    cout << (t % 2 == 0 ? "I LOVE CBNU" : star(t));

    return 0;
}