#import <ios>
long n,p,i=2;main(){scanf("%ld",&n);p=n;while(i*i<=n){if(n%i==0)p=p/i*(i-1);while(n%i==0)n/=i;i++;}if(n!=1)p=p/n*(n-1);printf("%ld\n",p);}