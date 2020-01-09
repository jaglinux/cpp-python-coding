#include<iostream>
#include<vector>
#include<set>
#include<stack>

using namespace std;

bool cyclic_util(vector<vector<int>>& G, vector<int>& visited, int vertex) {
	int result = true;
	visited[vertex] = 1;
	for(int i=0; i < G[vertex].size(); i++) {
		if(visited[G[vertex][i]] == 1)
			return false;
		else 
			result = cyclic_util(G, visited, G[vertex][i]);
	}
	visited[vertex] = 2;
	return result;
}

bool cyclic(vector<vector<int>> A) {
	set<int> S;
	bool result = true;

	for(int i=0; i < A.size(); i++) {
		for(int j=0; j < A[i].size(); j++) {
			S.insert(A[i][0]);
			S.insert(A[i][1]);
		}
	}
	cout << "Vertex size is " << S.size() << endl;
	vector<vector<int>> G(S.size());
	for(int i=0; i < A.size(); i++) {
		G[A[i][0]].push_back(A[i][1]);
	}
	cout << "Graph is " << endl;
	for(int i=0; i < G.size(); i++) {
		cout << "Vertex are " << i << endl;
		for(int j=0; j < G[i].size(); j++) {
			cout << G[i][j] << " " << endl; 
		}
		cout << endl;
	}
	vector<int> visited(G.size(), 0);
	for(int i=0; i < G.size(); i++) {
		if(visited[i] == 0)
			result = cyclic_util(G, visited, i);
		if(result == false)
			return result;
	}
	return result;
}
void dfs(vector<vector<int>>& G, stack<int>& S, set<int>& Set, int index) {
	Set.insert(index);
	for(int i=0; i < G[index].size(); i++) {
		if(Set.find(G[index][i]) == Set.end())
			dfs(G, S, Set, G[index][i]);
	}
	S.push(index);
}
vector<int> topo_sort(vector<vector<int>> A) {
	vector<vector<int>> G(6);
	stack<int> S;
	set<int> Set;
	vector<int> result;

	for(int i=0; i < A.size(); i++) {
		G[A[i][0]].push_back(A[i][1]);
	}
	for(int i=0; i < 6; i++) {
		if(Set.find(i) == Set.end()) {
			dfs(G, S, Set, i);
		}
	}

	while(!S.empty()) {
		result.push_back(S.top());
		S.pop();
	}
	return result;
}

int main() {
	vector<vector<int>> A = {
		{5,2},
		{5,0},
		{4,0},
		{4,1},
		{2,3},
		{3,1}
	};
	bool result;
	vector<int> sorted;

	cout << "Input is " << endl;
	for(int i=0; i < A.size(); i++) {
		for(int j=0; j < A[i].size(); j++) {
			cout << A[i][j] << " ";
		}
		cout << endl;
	}
	result = cyclic(A);
	cout << "result is " << result << endl;
	sorted = topo_sort(A);
	cout << "Sorted is " << endl;
	for(int i=0; i < sorted.size(); i++) {
		cout << sorted[i] << " "<< endl;
	}
	cout << endl;
}