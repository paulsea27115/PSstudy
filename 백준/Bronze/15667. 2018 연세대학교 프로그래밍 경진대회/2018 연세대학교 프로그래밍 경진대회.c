#include <stdio.h>
#include <math.h>

int main()
{
    int y, res;
    scanf("%d", &y);
    res = (-1 + sqrt(4*y-3)) / 2;
    printf("%d", res);
    return 0;
}