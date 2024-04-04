#include <bits/stdc++.h>

using namespace std;

#define ll long long int

ll mult(ll a, ll b, ll m)
{
  ll t = a, res = 0;
  a %= m;
  b %= m;

  while (b)
  {
      if (b % 2 != 0)
          res = (res + t) % m;
      t = t * 2 % m;
      b /= 2;
  }
  return res;
}

ll power(ll a, ll b, ll m)
{
  ll res = 1;
  while (b != 0)
  {
    if (b % 2 != 0)
        res = mult(res, a, m);
    a = mult(a, a, m);
    b /= 2;
  }
  return res;
}

int main()
{
  ll a, b, c;
  scanf("%lld %lld %lld", &a, &b, &c);
  printf("%lld", power(a, b, c));
}