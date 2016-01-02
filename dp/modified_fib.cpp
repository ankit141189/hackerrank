#include<iostream>
using namespace std;

int main() {
	int n;
	long long a, b, c;
	cin>>a>>b>>n;
	for (int i = 3; i <= n; ++i) {
		c = b * b + a;
		a = b;
		b = c;
		cout<<b<<endl;
	}
	cout<<b;
	return 0;
}
