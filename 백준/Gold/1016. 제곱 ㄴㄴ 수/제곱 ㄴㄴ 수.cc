#include <bits/stdc++.h>
#define ll unsigned long long
using namespace std;int main(){vector<ll> v;ll a,b,cnt=0;ll array[1000001]={};cin>>a>>b;for(ll i=2;i*i<= b;i++)v.emplace_back(i*i);for(ll j=0;j<v.size();j++){ll div_a=a;if(div_a%v[j]!=0){div_a=(a/v[j]+1)*v[j];}for(ll i=div_a;i<=b;i+=v[j]){if(i%v[j]==0)array[i-a]++;}}for(ll i=0;i<b-a+1;i++){if(array[i]==0){cnt++;}}cout<<cnt;return 0;}