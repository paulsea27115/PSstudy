#include <bits/stdc++.h>

using namespace std;

int a[50], b[50];

int f0(int n)
{
	if (n == 0)
		return 1;
	else if (n == 1)
		return 0;
	else if (a[n] != 0)
		return a[n];
	else
		return a[n] = f0(n - 1) + f0(n - 2);
}

int f1(int n)
{
	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	else if (b[n] != 0)
		return b[n];
	else
		return b[n] = f1(n - 1) + f1(n - 2);
}

int main()
{
	int t, n;

	scanf("%d", &t);

	while (t--)
	{
		scanf("%d", &n);

		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		printf("%d %d\n", f0(n), f1(n));
	}
}