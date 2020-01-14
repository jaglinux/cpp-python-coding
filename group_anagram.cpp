#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<unordered_map>

using namespace std;

vector<vector<string>> func(vector<string>& in) {
	unordered_map<string, vector<string>> H;
	vector<vector<string>> out;
	for(int i=0; i < in.size(); i++) {
		string temp = in[i];
		sort(temp.begin(), temp.end());
		H[temp].push_back(in[i]);
	}
	for(auto it=H.begin(); it != H.end(); it++) {
		out.push_back((*it).second);
	}
	return out;
}

int main() {
	vector<string> input = {"eat", "tea", "tan", "ate", "nat", "bat"};
	vector<vector<string>> output;

	cout << "input is " << endl;
	for(int i=0; i < input.size(); i++) {
		cout << input[i] << " ";
	}
	cout << endl;
	output = func(input);
	cout << "output is " << endl;

	for(int i=0; i < output.size(); i++) {
		for(int j=0; j < output[i].size(); j++) {
			cout << output[i][j] << " ";
		}
		cout << endl;
	}

}