#include <iostream>
#include <string>

using namespace std;

int to_binary(int num) {
	string s = "";
	while (num > 0) {
		if (num % 2 == 1) s = "1" + s;
		else s = "0" + s;
		num >>= 1;
	}
	
	return s.length();
}

int main(){
    int n;
    int check = 0;
    cin >> n;
    if(n < 0) {
        cout << 32;
        return 0;
    }
    
    if(n == 0) check += 1;
    
    cout << to_binary(n) + check;
    return 0;
}