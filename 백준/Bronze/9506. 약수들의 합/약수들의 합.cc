#include <iostream>
#include <string>
#include <vector>
#include <numeric>

int main()
{
    while(true) {
        int n;
        std::cin >> n;
        
        std::vector<int> v = {1};
        std::string ans(std::to_string(n));
        
        
        if(n == -1) break;
        
        for(int i = 2; i < n; i++) {
            if(n % i == 0) v.emplace_back(i);
        }
        
        int sum = std::accumulate(v.begin(), v.end(), 0);
        
        if(sum != n) ans += " is NOT perfect.";
        else {
            ans += " =";
            
            for(int i = 0; i < v.size(); i++) {
                ans += " " + std::to_string(v[i]);
                ans += i != v.size() - 1 ? " +" : "";
            }
        }
        
        std::cout << ans << "\n";
    }

    return 0;
}