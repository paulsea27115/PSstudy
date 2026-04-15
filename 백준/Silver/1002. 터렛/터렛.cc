#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a,x1,y1,r1,x2,y2,r2;
    scanf("%d",&a);
    for(int i = 0; i < a; i++) {
        scanf("%d %d %d %d %d %d",&x1,&y1,&r1,&x2,&y2,&r2);
        int d = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
        int dm = (r1-r2)*(r1-r2);
        int dM = (r1+r2)*(r1+r2);
        if(x1 == x2&&y1==y2) {
            if(r1==r2) {
                printf("-1\n");
                continue;
            } else {
                printf("0\n");
                continue;
            }
        }
        if(d < dM&&d>dm) {
            printf("2\n");
        } else if(d==dM||d==dm) {
            printf("1\n");
        } else if(d > dM||d<dm){
            printf("0\n");
        }
    }
    return 0;
}