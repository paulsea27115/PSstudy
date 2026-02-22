#include <iostream>

using namespace std;

long long int li[1000001] = {0,};

int main()
{
    li[1] = 1;
    long long int t, res = 0;
    cin >> t;
    
    for(long long int i = 2; i < 1000001; i++) {
        long long int a;
        li[i] = i * i + li[i - 1];
    }
    
    for(int i = 0; i < t; i++) {
        long long int a;
        cin >> a;
        
        cout << li[a] << "\n";
    }
    
    return 0;
}