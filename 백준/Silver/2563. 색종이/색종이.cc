#include <iostream>
int li[100][100] = {0,};

void output() {
    for(int i = 0 ; i < 100; i++) {
        for(int j  =0 ; j < 100; j++) {
            std::cout << li[i][j];
        }
        std::cout << std::endl;
    }
}

int main()
{
    int a, n, m;
    int cnt = 0;
    std::cin >> a;
    
    for(int i = 0; i < a; i++) {
        std::cin >> n >> m;
        for(int y = m; y < m + 10; y ++) {
            for(int x = n; x < n + 10; x++) {
                li[y][x] += 1;
            }
        }
    }
    
    for(int i = 0; i < 100; i++) {
        for(int j = 0; j < 100; j++) {
            if(li[i][j] != 0) {
                cnt += 1;
            }
        }
    }
    
    // output();
    
    std::cout << cnt;
    
    return 0;
}

