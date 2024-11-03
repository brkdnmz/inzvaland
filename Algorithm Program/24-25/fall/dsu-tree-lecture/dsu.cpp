#include <bits/stdc++.h>
using namespace std;

const int N = 2e5 + 5; // Max. number of nodes

// Embrace single-letter naming <3
int p[N]; // Parent of the component that the node belongs to (parent/ancestor/root...)
// Remember to initialize p[i] to i!

int sz[N]; // Component size
// Remember to initialize sz[i] to 1!

// I felt this is needed :D
int find_without_update_human_readable(int x) {
    if (x == p[x])
        return x;
    return find_without_update_human_readable(p[x]);
}

int find_without_update(int x) { return x == p[x] ? x : find_without_update(p[x]); }

// Notice the 7-chars-only difference
int find_with_update_human_readable(int x) {
    if (x == p[x])
        return x;
    return p[x] = find_with_update_human_readable(p[x]);
}

int find_with_update(int x) { return x == p[x] ? x : p[x] = find_with_update(p[x]); }

// Just to show this; no big difference
int find_with_update_2(int x) { return p[x] = (x == p[x] ? x : find_with_update_2(p[x])); }

// There's a `union` keyword in C++. Yes, just noticed right now.
// So I name my function as `comb` for "combine".
// Isn't it so nice?
// Yeah, I thought so.

void union_without_swap(int x, int y) {
    // If used find_without_update, would be n^2
    // With update, gets down to n * log(n)
    x = find_with_update(x);
    y = find_with_update(y);

    // They're already in the same component
    if (x == y)
        return; // Could return boolean for convenience, just sayin'

    p[x] = y; // Or p[y] = x, shouldn't matter
}

void union_with_swap(int x, int y) {
    x = find_with_update(x);
    y = find_with_update(y);

    if (x == y)
        return;

    // Always merge small-to-large to increase efficiency from n * log(n) to n * alpha(n)
    // Would still be n * log(n) if used find_without_update above
    if (sz[x] < sz[y])
        swap(x, y);

    // Here, we merge small-to-large
    p[y] = x;
    sz[x] += sz[y]; // No need to assign sz[y] = 0 as we won't ever use y itself anymore
}

int main() {
    for (int i = 1; i < N; i++)
        p[i] = i, sz[i] = 1;
    // Try stuff, too lazy to prepare template :p
}