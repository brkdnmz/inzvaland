#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int mod = 1e9 + 7;

using Coords = array<ll, 2>;
using Combination = pair<Coords, int>; // (Net coords, # of used coords)

void helper(vector<Coords> &actions, vector<Combination> &combs, int i, Combination cur_comb) {
    if (i == actions.size()) {
        combs.push_back(cur_comb);
        return;
    }
    helper(actions, combs, i + 1, cur_comb);
    cur_comb.first[0] += actions[i][0];
    cur_comb.first[1] += actions[i][1];
    cur_comb.second++;
    helper(actions, combs, i + 1, cur_comb);
}

vector<Combination> gen(vector<Coords> &actions) {
    vector<Combination> combs;
    helper(actions, combs, 0, {{0, 0}, 0});
    return combs;
}

int main() {
    int n;
    cin >> n;
    Coords g;
    cin >> g[0] >> g[1];
    vector<Coords> left, right;
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        i < n / 2 ? left.push_back({x, y}) : right.push_back({x, y});
    }
    auto lcombs = gen(left), rcombs = gen(right);
    ll ans[n + 1] = {};

    // n_combs[x][y][# of actions] = # of combs
    map<Coords, unordered_map<int, ll>> n_combs;

    for (auto &rcomb : rcombs) {
        n_combs[{rcomb.first[0], rcomb.first[1]}][rcomb.second]++;
    }
    for (auto &lcomb : lcombs) {
        ll x = lcomb.first[0], y = lcomb.first[1];
        int cnt = lcomb.second;
        // Ben rcombs'ta ({g.x - x, g.y - y}, size)'ları bulmak istiyorum
        // Her size değeri için ans[cnt + size]++
        Coords need = {g[0] - x, g[1] - y};
        if (!n_combs.count(need))
            continue;
        auto &target = n_combs[need];
        for (auto &[size, cur_cnt] : target) {
            ans[cnt + size] += cur_cnt;
        }
    }
    for (int i = 1; i <= n; i++)
        cout << ans[i] << "\n";
}