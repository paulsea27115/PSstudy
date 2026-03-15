#include <iostream>

using namespace std;

int main()
{
    int t, first, input;
    cin >> t;
    bool check = true;
    
    while(t--) {
        cin >> input;
        
        if(check) {
            first = input;
            check = false;
            continue;
        }
        
        if(input % first == 0) {
            cout << input << endl;
            check = true;
        }
    }
    return 0;
}