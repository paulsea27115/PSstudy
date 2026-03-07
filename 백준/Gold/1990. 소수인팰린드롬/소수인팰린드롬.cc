#include <bits/stdc++.h>
#define ll long long int
#define N 10000000

using namespace std;

bool isP(ll n) {
    ll r_h = 0;
    
    while(n > r_h){
        r_h = (r_h * 10) + (n % 10);
        n /= 10;
    }
    
    return (n == r_h || n == r_h / 10);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    std::vector<bool> v(N, true);
    v[0] = false;
    v[1] = false;
    
    for(ll i = 2; i < sqrt(N); i++) {
        if(v[i]) {
            for(ll j = i * i; j < N + 1; j+=i) v[j] = false;
        }
    }
    
    ll a_to, b_from;
    cin >> a_to >> b_from;
    
    for(ll i = a_to; i <= b_from; i++) {
        if(i >= 10000000) continue;
        else if(v[i] && isP(i)) cout << i << "\n";
    }
    cout << -1;
    return 0;
}