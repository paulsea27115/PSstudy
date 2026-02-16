#include <iostream>

using namespace std;

class Player {
    public:
    int n;
    int m;
    int s;
};

int main()
{
    int t;
    Player players[100];
    
    cin >> t;
    
    for(int i = 0; i < t; i++) {
        cin >> players[i].n;
        int a, b, c;
        cin >> a >> b >> c;
        
        players[i].m = a * b * c;
        players[i].s = a + b + c;
    }

    for(int i = 0; i < t - 1; i++) {
        for(int j = 0; j < t - 1 - i; j++) {
            bool swap = false;
            
            if(players[j + 1].m < players[j].m) swap = true;
            else if(players[j + 1].m == players[j].m) {
                if(players[j + 1].s < players[j].s) swap = true;
                else if(players[j + 1].s == players[j].s) {
                    if(players[j + 1].n < players[j].n) swap = true;
                }
            }
            
            if(swap) {
                Player tmp = players[j];
                players[j] = players[j + 1];
                players[j + 1] = tmp;
            }
        }
    }
    
    cout << players[0].n << " " << players[1].n << " " << players[2].n;

    return 0;
}