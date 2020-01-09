#include<iostream>
#include<string>
#include<vector>

using namespace std;

class node {
public:
	string name;
	vector <node *> list;
	node() {}
	node(string a) {
		name = a;
	}
};

class tree {
public:
	vector<node*> vertex;
	tree() {}
	void add_node(string a) {
		node *temp = new node(a);
		vertex.push_back(temp);
	}
	void add_edge(string a, string b) {
		int flag = 0;
		node *first = NULL;
		node *second = NULL;
		for(int i=0; i < vertex.size(); i++) {
			if(vertex[i]->name == a)  {
				first = vertex[i];
			}
			else if(vertex[i]->name == b) {
				second = vertex[i];
			}
		}
		if(first && second) {
			first->list.push_back(second);
			second->list.push_back(first);
		}
	}

	void print() {
		cout << "Vertex are " << endl;
		for(int i=0; i < vertex.size(); i++) {
			cout << vertex[i]->name << " ";
		}
		cout << endl;

		cout << "Edge are " << endl;
		for(int i=0; i < vertex.size(); i++) {
			cout << "For vertex " << vertex[i]->name << " neighbors are " << endl;
			for(int j =0; j < vertex[i]->list.size(); j++) {
				cout << vertex[i]->list[j]->name << " " <<endl;
			}
			cout << endl;
		}
	}
};

int main() {
	tree T;
	T.add_node("1");
	T.add_node("2");
	T.add_node("3");
	T.add_edge("1", "2");
	T.add_edge("1", "3");
	T.print();
}


