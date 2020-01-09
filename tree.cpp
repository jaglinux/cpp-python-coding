#include<iostream>
#include<queue>

using namespace std;

class node {
public:
	node *left;
	node *right;
	int data;

	node(int data) {
		this->data = data;
		this->left = NULL;
		this->right = NULL;
	}

};

class tree {
	node *root;
public:
	tree() {
		cout << "root is " << root << endl;
	}
	void add_node(int data) {
		node *temp = new node(data);
		if(root) {
			queue<node *> Q;
			Q.push(root);
			while(!Q.empty()) {
				node *pop = Q.front();
				if(!pop->left) {
					temp->left = pop->left;
					return;
				}
				else if(!pop->right) {
					temp->right = pop->right;
					return;
				}
				Q.pop();
				Q.push(pop->left);
				Q.push(pop->right);
			}
			
		} else {
			root = temp;
		}
	}

	void print() {
		func(root);
	}
	void func(node *root) {
		if(root == NULL)
			return;
		cout << root->data << " ";
		func(root->left);
		func(root->right);
	}
};

int main() {
	tree T;
	T.add_node(1);
	T.add_node(2);
	T.print();
	return 1;
}