```
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>

using namespace std;

int testcase, N, Q;
int Order, N1, N2;

int initMax(vector<int>& arr, vector<int>& tree, int node, int st, int ed) {
	if (st == ed)    // 노드가 리프 노드인 경우
		return tree[node] = arr[st];    // 배열의 그 원소를 가져야 함

	int mid = (st + ed) / 2;
	int LEFT = initMax(arr, tree, node * 2, st, mid);
	int RIGHT = initMax(arr, tree, node * 2 + 1, mid + 1, ed);
	if (LEFT >= RIGHT)
		return tree[node] = LEFT;
	else
		return tree[node] = RIGHT;
}

int initMin(vector<int>& arr, vector<int>& tree, int node, int st, int ed) {
	if (st == ed)    // 노드가 리프 노드인 경우
		return tree[node] = arr[st];    // 배열의 그 원소를 가져야 함

	int mid = (st + ed) / 2;
	int LEFT = initMin(arr, tree, node * 2, st, mid);
	int RIGHT = initMin(arr, tree, node * 2 + 1, mid + 1, ed);
	if (LEFT <= RIGHT)
		return tree[node] = LEFT;
	else
		return tree[node] = RIGHT;
}


int segMax(vector<int>& tree, int node, int start, int end, int left, int right) {
	//st, ed가 노드가 담당한 범위
	//left, right가 구해야 하는 범위
	
	//범위가 전혀 겹치지 않는 경우
	if (left > end || right < start) 
		return -1;

	if (left <= start && end <= right)
		return tree[node];

	int mid = (start + end) / 2;
	int LEFT = segMax(tree, node * 2, start, mid, left, right);
	int RIGHT = segMax(tree, node * 2 + 1, mid + 1, end, left, right);
	if (LEFT >= RIGHT)
		return LEFT;
	else
		return RIGHT;
}

int segMin(vector<int>& tree, int node, int start, int end, int left, int right) {
	//st, ed가 노드가 담당한 범위
	//left, right가 구해야 하는 범위

	if (left > end || right < start)
		return 2000000000;

	if (left <= start && end <= right)
		return tree[node];

	int mid = (start + end) / 2;
	int LEFT = segMin(tree, node * 2, start, mid, left, right);
	int RIGHT = segMin(tree, node * 2 + 1, mid + 1, end, left, right);
	if (LEFT <= RIGHT)
		return LEFT;
	else
		return RIGHT;
}

void updateMax(vector<int>& tree, int node, int start, int end, int index, int New) {
	if (index < start || index > end) 
		return;
	if (start == end && start == index)
		tree[node] = New;
	//if(tree[node]<New)
	//	tree[node] = New;   

	// 리프 노드가 아닌 경우 자식도 변경
	if (start != end) {
		int mid = (start + end) / 2;
		updateMax(tree, node * 2, start, mid, index, New);
		updateMax(tree, node * 2 + 1, mid + 1, end, index, New);
		if (tree[node * 2] < tree[node * 2 + 1])
			tree[node] = tree[node * 2 + 1];
		else
			tree[node] = tree[node * 2];
	}
}

void updateMin(vector<int>& tree, int node, int start, int end, int index, int New) {
	if (index < start || index > end)
		return;
	if (start == end && start == index)
		tree[node] = New;
	
	// 리프 노드가 아닌 경우 자식도 변경
	if (start != end) {
		int mid = (start + end) / 2;
		updateMin(tree, node * 2, start, mid, index, New);
		updateMin(tree, node * 2 + 1, mid + 1, end, index, New);
		if (tree[node * 2] < tree[node * 2 + 1])
			tree[node] = tree[node * 2];
		else
			tree[node] = tree[node * 2 + 1];
	}
}

int main(void) {
	cin.tie(NULL);
	cout.tie(NULL);
	cin.sync_with_stdio(false);

	cin >> testcase;

	for (int tc = 1; tc <= testcase; tc++) {
		cin >> N >> Q;
		int H = (int)ceil(log2(N));
		int tree_size = (1 << (H + 1));

		vector<int> arr(N);
		vector<int> treeMax(tree_size);
		vector<int> treeMin(tree_size);
		vector<int> ans;

		for (int i = 0; i < N; i++)
			cin >> arr[i];

		initMax(arr, treeMax, 1, 0, N - 1);
		initMin(arr, treeMin, 1, 0, N - 1);

		//for (int j = 1; j <= 5; j++)
		//	cout << treeMin[j] << " ";
		//cout << "\n\n";
	
		for (int i = 0; i < Q; i++) {
			cin >> Order >> N1 >> N2;
			if (Order == 1) {//여기서는 N1 ~ N1+N2-1 최대 최소 차이
				int tmp = segMax(treeMax, 1, 0, N - 1, N1, N2 - 1) - segMin(treeMin, 1, 0, N - 1, N1, N2 - 1);
				//cout <<"\n   " << segMax(treeMax, 1, 0, N - 1, N1, N2 - 1) << " " << segMin(treeMin, 1, 0, N - 1, N1, N2 - 1) << "\n";
				ans.push_back({ tmp });
			}
			else {
				updateMax(treeMax, 1, 0, N - 1, N1, N2);
				updateMin(treeMin, 1, 0, N - 1, N1, N2);
				//for (int j = 1; j <= 5; j++)
				//	cout << treeMin[j]<<" ";
				//cout << "\n\n";
			}
		}

		cout << "#" << tc;
		for (int i = 0; i < ans.size(); i++)
			cout << " " << ans[i];
		cout << "\n";
	}

	return 0;
}
```
