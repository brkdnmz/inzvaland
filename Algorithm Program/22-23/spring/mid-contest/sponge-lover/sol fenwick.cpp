#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5;
int fw[N];

void add(int x) {
    for (; x < N; x += x & -x)
        fw[x]++;
}
int get(int x) {
    int res = 0;
    for (; x > 0; x -= x & -x)
        res += fw[x];
    return res;
}

vector<int> id_to_rank(vector<int> &v) {
    int n = v.size();
    vector<array<int, 2>> v_with_ids;
    for (int i = 0; i < n; i++)
        v_with_ids.push_back({v[i], i});
    sort(v_with_ids.begin(), v_with_ids.end());
    vector<int> res(n);
    for (int i = 0; i < n; i++)
        res[v_with_ids[i][1]] = i;
    return res;
}

vector<int> rank_to_id(vector<int> &v) {
    int n = v.size();
    vector<array<int, 2>> v_with_ids;
    for (int i = 0; i < n; i++)
        v_with_ids.push_back({v[i], i});
    sort(v_with_ids.begin(), v_with_ids.end());
    vector<int> res(n);
    for (int i = 0; i < n; i++)
        res[i] = v_with_ids[i][1];
    return res;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    vector<int> dishes(n), sponges(n);
    for (int &x : dishes)
        cin >> x;
    for (int &x : sponges)
        cin >> x;
    vector<int> dish_id_to_rank = id_to_rank(dishes);
    vector<int> sponge_rank_to_id = rank_to_id(sponges);
    vector<int> sponge_orders;
    for (int i = 0; i < n; i++) {
        int dish_rank = dish_id_to_rank[i];
        int nth_sponge = sponge_rank_to_id[dish_rank];
        sponge_orders.push_back(nth_sponge - get(nth_sponge + 1) + 1);
        add(nth_sponge + 1);
    }
    for (int sponge_order : sponge_orders)
        cout << sponge_order << "\n";
}