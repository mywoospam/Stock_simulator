```
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int testcase, N, Q;
long long Order, N1, N2;

long long INIT_EVEN(vector<long long>& arr, vector<long long>& tree, int node, int st, int ed) {
	if (st == ed) {
		if (st % 2 == 0)
			return tree[node] = arr[st];
		else
			return tree[node] = 0;
	}
	int mid = (st + ed) / 2;
	return tree[node] = INIT_EVEN(arr, tree, node * 2, st, mid) + INIT_EVEN(arr, tree, node * 2 + 1, mid + 1, ed);
}

long long INIT_ODD(vector<long long>& arr, vector<long long>& tree, int node, int st, int ed) {
	if (st == ed) {
		if (st % 2 == 1)
			return tree[node] = arr[st];
		else
			return tree[node] = 0;
	}
	int mid = (st + ed) / 2;
	return tree[node] = INIT_ODD(arr, tree, node * 2, st, mid) + INIT_ODD(arr, tree, node * 2 + 1, mid + 1, ed);
}

long long SUM(vector<long long>& tree, int node, int st, int ed, int left, int right) {
	if (left > ed || right < st)
		return 0;
	else if (left <= st && ed <= right)
		return (long long)tree[node];

	int mid = (st + ed) / 2;

	return SUM(tree, node * 2, st, mid, left, right) + SUM(tree, node * 2 + 1, mid + 1, ed, left, right);
}

void updateTree(vector<long long>& tree, int node, int st, int ed, int idx, long long diff) {
	if (idx < st || idx > ed)
		return;
	tree[node] += diff;

	if (st == ed)
		return;

	int mid = (st + ed) / 2;
	updateTree(tree, node * 2, st, mid, idx, diff);
	updateTree(tree, node * 2 + 1, mid + 1, ed, idx, diff);
}

signed main(void) {
	cin.tie(NULL);
	cout.tie(NULL);
	cin.sync_with_stdio(false);

	int testcase;
	cin >> testcase;
	for (int tc = 1; tc <= testcase; tc++) {
		cin >> N >> Q;
		int H = (int)ceil(log2(N));
		int tree_size = (1 << (H + 1));

		vector<long long> arr(N);
		vector<long long> treeEven(tree_size);
		vector<long long> treeOdd(tree_size);
		vector<long long> ANS;

		for (int i = 0; i < N; i++)
			cin >> arr[i];

		INIT_EVEN(arr, treeEven, 1, 0, N - 1);
		INIT_ODD(arr, treeOdd, 1, 0, N - 1);

		for (int i = 0; i < Q; i++) {
			cin >> Order >> N1 >> N2;
			if (Order) {
				if (N1 % 2 == 0) {//짝수부터 시작한다면
					long long tmpans = SUM(treeEven, 1, 0, N - 1, N1, N2 - 1) - SUM(treeOdd, 1, 0, N - 1, N1, N2 - 1);
					ANS.push_back({ tmpans });
				}
				else {//홀수부터 시작
					long long tmpans = SUM(treeOdd, 1, 0, N - 1, N1, N2 - 1) - SUM(treeEven, 1, 0, N - 1, N1, N2 - 1);
					ANS.push_back({ tmpans });
				}
			}
			else {
				if (N1 % 2 == 0) 
					updateTree(treeEven, 1, 0, N - 1, N1, N2 - arr[N1]);
				else
					updateTree(treeOdd, 1, 0, N - 1, N1, N2 - arr[N1]);
				arr[N1] = N2;
			}
		}

		cout << "#" << tc;
		for (int i = 0; i < ANS.size(); i++)
			cout << " " << ANS[i];
		cout << "\n";
	}
	return 0;
}
```
