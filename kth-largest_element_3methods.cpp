#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

void func1(vector<int>& A, int k) {
	int s = A.size();
	priority_queue<int> Q;

	if(k > s) {
		cout << "k is greates than size of vector " << endl;
		return;
	}
	for(int i=0; i < s; i++) {
		Q.push(A[i]);
	}
	while(k) {
		Q.pop();
		k--;
	}
	cout << "element is " << Q.top() << endl;
}

void func2(vector<int> A, int k) {
	int s = A.size();

	if(k > s) {
		cout << "k is greater than size of vector " << endl;
		return;
	}
	sort(A.begin(), A.end());
	cout << "element is " << A[s-k-1] << endl;
}

void func3(vector<int>& A, int k) {
	int s = A.size();
	priority_queue<int, vector<int>, greater<int>> Q;
	if(k > s) {
		cout << "k is greater than size of vector " << endl;
		return;
	}
	for(int i=0; i < s; i++) {
		if(i <= k)
			Q.push(A[i]);
		else {
			if(A[i] > Q.top()) {
				Q.pop();
				Q.push(A[i]);
			}
		}
	}
	cout << "element is " << Q.top() << endl;
}

int main() {
	int k = 3;
	vector<int> A = {3,2,5,8,1,9};
	func1(A, k);
	func2(A, k);
	func3(A, k);
}