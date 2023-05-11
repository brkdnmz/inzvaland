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
#define FOR(i, n) for(int i = 0; i < (n); i++)
typedef pair<int, int> pii;
typedef long long ll;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
template<typename T>
T gen(T l, T r){
	return rnd(l, r)(rng);
}
template<typename T>
T gen(T r){
	return rnd(1, r)(rng);
}
template<typename T>
T gen0(T r){
    return rnd(0, r)(rng);
}

int target[] = {2, 0, 2, 2};
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int solve(int cur, int r, int c, int N, int M, vector<vector<int>>& grid){
    if(r < 0 || r == N || c < 0 || c == M) return 0;
    if(grid[r][c] != target[cur]) return 0;
    if(cur == 3) return 1;
    int ans = 0;
    for(int d = 0; d < 4; d++){
        int nr = r + dx[d];
        int nc = c + dy[d];
        ans += solve(cur+1, nr, nc, N, M, grid);
    }
    return ans;
}
int main(){
    for(int tc = 0; tc < 5; tc++){
        ofstream input("input/input" + to_string(tc) + ".txt");
        ofstream output("output/output" + to_string(tc) + ".txt");
        int N = gen(2022);
        int M = gen(2022);
        ll ans = 0;
        vector<vector<int>> grid(N, vector<int>(M));
        int prob = gen(5);
        int which = gen0(1) ? 2 : 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                grid[i][j] = which;
            }
        }
        for(int i = 0; i < min(2022, N*M); i++)
            grid[gen0(N-1)][gen0(M-1)] = 2 - which;
        
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                ans += solve(0, i, j, N, M, grid);
            }
        }
        input << N << " " << M << "\n";
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                input << grid[i][j];
                if(j+1 < M) input << " ";
            }
            if(i+1 < N) input << "\n";
        }
        assert(ans <= 64 * N * M);
        output << ans;
    }
}