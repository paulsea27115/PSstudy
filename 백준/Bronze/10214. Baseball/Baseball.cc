#include <iostream>
#include <string>

using namespace std;

string output(int Yonsei, int Korea){
    string ans;
    if(Yonsei > Korea) ans = "Yonsei";
    else if(Yonsei < Korea) ans = "Korea";
    else ans = "Draw";
    
    return ans;
}

int main(){
    int t;
    cin >> t;
    
    for(int i = 0; i < t; i++) {
        int l = 0, r = 0;
        
        for(int j = 0; j < 9; j++) {
            int a, b;
            cin >> a >> b;
            
            l += a;
            r += b;
        }
        
        cout << output(l, r) << endl;
    }
    return 0;
}