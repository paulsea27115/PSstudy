#include <iostream>

using namespace std;

int li[1001][1001] = {0,};

void print_(){
    for(int i = 0; i < 1001; i++) {
        for(int j = 0; j < 1001; j++) 
        {
            cout << li[i][j];
        }
        cout << "\n";
    }
}

int main()
{
    int t = 0;
    
    cin >> t;
    
    int ans[t] = {0,};

    for(int i = 0; i < t; i++) {
        int x1 = 0, y1 = 0, x2 = 0, y2 = 0;
        
        cin >> x1 >> y1 >> x2 >> y2;
        
        for(int y = y1; y < y1 + y2; y++) {
            for(int x = x1; x < x1 + x2; x++) {
                li[y][x] = i+1;
            }
        }
    }

    for(int i = 0; i < t; i++){
        for(int y = 0; y <= 1000; y++) {
            for(int x = 0; x <= 1000; x++) {
                if(li[y][x] == i+1) {
                    // cout << y << " " << x << endl;
                    ans[i] += 1;
                }
            }
        }
    }
    for(int i = 0; i < t; i++) {
        cout << ans[i] << "\n";
    }

    return 0;
}