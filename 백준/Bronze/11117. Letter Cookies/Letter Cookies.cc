#include <iostream>
#include <map>

using namespace std;

class sol{
    private:
    string compare_str;
    map<char, int> m;
    
    public:
    sol(string compare_str_input){
        compare_str = compare_str_input;
        
        for(const char& one_str:compare_str)
            m[one_str]++;
    }
    
    bool compare(string check_str){
        map<char, int> use_m(m);
        
        for(const char& one_str:check_str)
            use_m[one_str]--;
        
        for(const auto& entry : use_m) {
            if(entry.second < 0) return false;
        }
        return true;
    }
    
};

int main()
{
    int t1;
    cin >> t1;
    
    while(t1--) {
        string str;
        cin >> str;
        sol ans(str);
        
        int t2;
        cin >> t2;
        while(t2--) {
            cin >> str;
            if(ans.compare(str)) cout << "YES\n";
            else cout << "NO\n";
        }
    }

    return 0;
}