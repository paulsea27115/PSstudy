#include <stdio.h>

int main()
{
    int a, b;
    
    scanf("%d %d", &a, &b);
    
    int res;
    
    res = 10 + 2 * (25 - a + b);
    
    printf("%d", res<=0?0:res);

    return 0;
}