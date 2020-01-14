#include<iostream>
#include<queue>

using namespace std;

struct node {
	int data;
	struct node* left;
	struct node* right;
};

class bst {
	struct node *root;
	void func_insert(struct node* first,struct node* temp, struct node*prev, bool flag) {
		if(first == NULL){
			if(flag)
				prev->right = temp;
			else 
				prev->left = temp; 
			return;
		}
		if(temp->data < first->data) func_insert(first->left, temp, first, false);
		else func_insert(first->right, temp, first, true);
	}
	void func_inorder(struct node*first) {
		if(!first) return;
		func_inorder(first->left);
		cout << "inorder is " << first->data << endl;
		func_inorder(first->right);
	}
public:
	bst() {
		//root = NULL;
	}
	void insert(int data) {
		node *temp = new node();
		temp->data = data;
		temp->left = NULL;
		temp->right = NULL;
		if(root == NULL) {
			root = temp;
		} else {
			func_insert(root, temp, NULL, false);
		}
	}

	void print_bst() {
		node *temp = root;
		cout << "BST contents " << endl;
		if(temp) {
			queue<node*> Q;
			Q.push(temp);
			while(!Q.empty()) {
				node *single = Q.front();
				Q.pop();
				cout << "node is " << single->data << endl;
				if(single->left)
					Q.push(single->left);
				if(single->right)
					Q.push(single->right);
			}
		}
	}

	void print_inorder() {
		func_inorder(root);
	}
};

int main() {
	bst B;
	B.insert(50);
	B.insert(30);
	B.insert(20);
	B.insert(40);
	B.insert(70);
	B.insert(60);
	B.insert(80);


	B.print_bst();
	B.print_inorder();
	return 0;
}