#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int N = 1e6 + 5;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k;
    cin >> n >> k;
    int hours[n];
    for (int &x : hours)
        cin >> x;

    int l = 1, r = *max_element(hours, hours + n);
    while (l < r) {
        int mid = (l + r) / 2;
        // Biz K işlem sonucunda max değeri mid yapabilir miyiz?
        ll total_required = 0;
        for (int h : hours) {
            // mid mid mid... -> h
            // ceil(h / mid)

            // h = k * mid + r
            // h/mid = k
            // k + 1
            // (k + 1) * mid - 1

            total_required += (h + mid - 1) / mid - 1;
        }
        if (total_required <= k) {
            r = mid;
        } else { // > k
            l = mid + 1;
        }
    }

    cout << l << "\n";
}