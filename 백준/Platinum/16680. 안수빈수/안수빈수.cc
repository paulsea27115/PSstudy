#include<bits/stdc++.h>

using namespace std;

#define ll long long int

int main()
{
    ll a,num,res;
    string sum;
    
    scanf("%lld",&a);
    
    for(int j = 0;j < a;j++){
        res = 0;
        scanf("%lld",&num);
        num=num*999999999;
        sum=to_string(num);
        for(int i = 0; i < sum.size();i++) res += sum[i]-'0';
        if(res % 2 !=0) printf("%lld\n",num);
        else printf("-1\n");
        
    }
    return 0;
}
