#include <iostream>

using namespace std;

int main(){
    const int cycle = 25, sleep = 17;
    int t;
    cin >> t;
    
    for(int i = 0; i < t; i++) {
        int a;
        cin >> a;
        
        if(a % cycle >= sleep) cout << "OFFLINE" << endl;
        else cout << "ONLINE" << endl;
    }
    
    return 0;
}