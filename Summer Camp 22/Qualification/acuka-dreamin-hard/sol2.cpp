#include <bits/stdc++.h>

using namespace std;

long long n;
const int N = 1e5 + 5;
const long long int lim = 2e18 + 5;
int p[N], m[N];

int visited[12][N];
int pre_sum[12][N];
int cycle_beg[12];
int cycle_beg_idx[12];
int cycle_len[12];
int cycle_sum[12];
int until_cycle_sum[12];

bool check(long long x) {
    long long tot = 0;

    for (int i = 1; i <= 11 and tot <= n; i++) {
        if (x < cycle_beg[i]) {
            tot += pre_sum[i][x];
        } else {
            tot += until_cycle_sum[i];
            // cout << "#" << tot << endl;
            tot += cycle_sum[i] * ((x - cycle_beg_idx[i] + 1) / cycle_len[i]);
            // cout << "##" << tot << endl;

            int in_cycle_idx = (x - cycle_beg_idx[i] + 1) % cycle_len[i];
            tot += pre_sum[i][in_cycle_idx + cycle_beg_idx[i] - 1] - pre_sum[i][cycle_beg_idx[i] - 1];
            // cout << "###" << tot << endl;
        }

        // cout << tot << endl;
    }

    return tot <= n;
}
bool check2(long long x) {
    long long tot = 0;

    for (int i = 1; i <= 11 and tot <= n; i++) {
        tot += pre_sum[i][x];
        // cout << tot << endl;
    }

    return tot <= n;
}

long long calc() {
    long long beg = 0, end = lim + 5;

    while (beg < end) {
        long long mid = (beg + end + 1) / 2;

        if (check(mid)) {
            beg = mid;
        } else {
            end = mid - 1;
        }
    }

    return beg;
}

int main() {
    cin >> n;

    for (int i = 1; i <= 11; i++) {
        cin >> p[i] >> m[i];
    }

    for (int i = 1; i <= 11; i++) {
        int curr = p[i] % m[i];
        for (int j = 1;; j++) {
            if (visited[i][curr]) {
                cycle_beg[i] = curr;
                cycle_beg_idx[i] = visited[i][curr];
                cycle_len[i] = j - cycle_beg_idx[i];
                cycle_sum[i] = pre_sum[i][j - 1] - pre_sum[i][cycle_beg_idx[i] - 1];
                until_cycle_sum[i] = pre_sum[i][cycle_beg_idx[i] - 1];
                break;
            }
            visited[i][curr] = j;
            pre_sum[i][j] += pre_sum[i][j - 1] + curr;

            curr = (long long)curr * i % m[i];
        }
    }

    long long res = calc();

    if (res > lim) {
        cout << -1 << endl;
    } else {
        cout << res << endl;
    }
}