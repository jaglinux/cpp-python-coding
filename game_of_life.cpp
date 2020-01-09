#include<iostream>
#include<vector>

using namespace std;

int find_one(vector<vector<int>>& A, int row, int col, int row_max, int col_max) {
	int one=0;
	if(col > 0) {
		if(A[row][col-1] & 1) one++;
		if(row > 0 && A[row-1][col-1] & 1) one++;
		if(row+1 < row_max && A[row+1][col-1] & 1) one++;
	}
	if(row > 0 && A[row-1][col] & 1) one++;
	if(row+1 < row_max && A[row+1][col] & 1) one++;

	if(col+1 < col_max) {
		if(A[row][col+1] & 1) one++;
		if(row > 0 && A[row-1][col+1] & 1) one++;
		if(row+1 < row_max && A[row+1][col+1] & 1) one++;
	}
	return one;
}

void update_cell(int &a, int one) {
	if(a&1) {
		if(one == 2 || one == 3)
			a = a | 2;
	} else {
		if(one == 3)
			a = a | 2;
	}
}

void game(vector<vector<int>>& A) {

	int row_max = A.size();
	int col_max = A[0].size();

	for(int i=0; i < A.size(); i++) {
		for(int j=0; j < A[i].size(); j++) {
			int one = find_one(A,i, j, row_max, col_max);
			update_cell(A[i][j], one);
		}
	}
	for(int i=0; i < A.size(); i++) {
		for(int j=0; j < A[i].size(); j++) {
			A[i][j] = A[i][j] >> 1;
		}
	}
}

int main() {
	vector<vector<int>> input = {
  {0,1,0},
  {0,0,1},
  {1,1,1},
  {0,0,0}
};

	cout << "inputs are" << endl;
	for(int i=0; i < input.size(); i++) {
		for(int j=0; j < input[i].size(); j++) {
			cout << input[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;

	game(input);

	for(int i=0; i < input.size(); i++) {
		for(int j=0; j < input[i].size(); j++) {
			cout << input[i][j] << " ";
		}
		cout << endl;
	}
}