#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef uniform_int_distribution<ll> rnd;
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define REVERSE(v) reverse((v).begin(), (v).end())
#define MAX(v) (*max_element((v).begin(), (v).end()))
#define MIN(v) (*min_element((v).begin(), (v).end()))
#define pb push_back
#define FOR(i, n) for (int i = 0; i < (n); i++)
typedef pair<int, int> pii;
typedef long long ll;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
ll gen(ll l, ll r)
{
	return rnd(l, r)(rng);
}
ll gen(ll r)
{
	return rnd(1, r)(rng);
}

const int mod = 1e9 + 7;
const int N = 1e6 + 5;
int modsum(int a, int b)
{
	return (a + b) % mod;
}
int seg[4 * N + 5];
void update(int c, int l, int r, int t, int v)
{
	if (!(l <= t && t <= r))
		return;
	if (l == r)
	{
		seg[c] = v;
		return;
	}
	int mid = (l + r) / 2;
	update(2 * c, l, mid, t, v);
	update(2 * c + 1, mid + 1, r, t, v);
	seg[c] = modsum(seg[2 * c], seg[2 * c + 1]);
}
int get(int c, int l, int r, int t)
{
	if (l > t)
		return 0;
	if (r <= t)
	{
		return seg[c];
	}
	int mid = (l + r) / 2;
	return modsum(get(2 * c, l, mid, t), get(2 * c + 1, mid + 1, r, t));
}
int main()
{
	for (int tc = 0; tc < 5; tc++)
	{
		FOR(i, 4 * N + 5)
		{
			seg[i] = 0;
		}
		string input = "input/input" + to_string(tc) + ".txt";
		string output = "output/output" + to_string(tc) + ".txt";
		ofstream in(input);
		ofstream out(output);

		int n = gen(1, 2e5);
		set<pair<ll, int>> st;
		vector<ll> a(n);
		FOR(i, n)
		{
			a[i] = gen(0, 1e12);
		}
		FOR(i, n)
		{
			int max_val = sqrt(a[i]);
			if (1ll * (max_val + 1) * (max_val + 1) <= a[i])
				max_val++;
			int new_ans = get(1, 0, N, max_val);
			new_ans = modsum(new_ans, 1);
			if (a[i] > N)
				st.insert({a[i], new_ans});
			else
			{
				update(1, 0, N, a[i], new_ans);
			}
		}
		int tot = get(1, 0, N, N);
		for (auto x : st)
		{
			tot = modsum(tot, x.second);
		}
		in << n << "\n";
		FOR(i, n)
		{
			in << a[i];
			if (i + 1 < n)
				in << " ";
		}
		out << tot;
		in.close();
		out.close();
	}
}