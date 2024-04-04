#include <iostream>

using namespace std;

#define ll long long

int main()
{
    ll n=1,phi;
    while(n!=0){
        cin >> n;
        phi = n;
        if(n==0){
            break;
        } else if(n==1){
            cout << 0 << '\n';
            continue;
        }
        for (ll i = 2; i * i <= n; i++) { 
        	if (n % i == 0) { // n의 소인수가 i가 맞는지 확인
        		// 맞으면 오일러 피함수 앞부분 p₁^(a₁-1)p₂^(a₂-1) ..... pk^(ak-1) 
        		phi = phi / i;
        		phi = phi * (i - 1);
        	}
        	while (n % i == 0) n /= i; // 인수의 차수가 높아도 하나만 필요
        	// n의 인수가 아닐때는 다음으로
        }
        if (n != 1) { 
        	phi /= n; // 오일러 피함수 뒷부분 (p₁-1)(p₂-1).... (pk-1)
        	phi *= (n - 1); 
        }
        cout << phi << '\n';
    }
    return 0;
}
