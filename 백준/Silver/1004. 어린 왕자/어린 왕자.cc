#include <bits/stdc++.h>

using namespace std;

bool distence(int x,int y,int x1,int y1,int r){
    int dis = sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1));
    if(dis > r)
        return false;
    else if(dis < r)
        return true;
    return false;
}

int main()
{
    int T, P,x1,y1,x2,y2,cx,cy,r,cnt=0;
    cin >> T;
    
    for(int i = 0 ; i < T; i++){
        cnt=0;
        cin >> x1 >> y1 >> x2 >> y2;
        cin >> P;
        for(int j = 0 ;j < P; j++){
            cin >> cx >> cy >> r;
            if(sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)) < r*2&&sqrt((x1-cx)*(x1-cx)+(y1-cy)*(y1-cy))<r&&sqrt((x2-cx)*(x2-cx)+(y2-cy)*(y2-cy))<r){
                continue;
            } else if(distence(x1,y1,cx,cy,r)||distence(x2,y2,cx,cy,r)){
                cnt++;
            }
        }
        cout << cnt << endl;
    }
    
    return 0;
}
//거리 구할때 쓰는 공식 sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))
