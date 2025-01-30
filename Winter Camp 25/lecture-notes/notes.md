(VS Code: Ctrl-Shift-V or Ctrl-K then V)

# DAG

- SCC condensation graph
- Trees

# [Topological Sort](https://usaco.guide/gold/toposort?lang=cpp)

- [Additional source](https://cp-algorithms.com/graph/topological-sort.html)
- Task $v$ depends on task $u$ (edge $u \to v$)
- A proper order to finish all tasks (there might be more than one)
- Either DFS or BFS (I'm used to BFS)
  - First time my friend taught me, I was amaaaaazed!
  - Defining those `in` and `out`s yo, how clever & pretty, right?
- Can detect cycles if any!

# DP on DAG

- Bottom-up or top-down (I prefer the latter, which I'm used to 😌)

## Problems

- https://algoleague.com/problem/super-duper-mario/detail

# [Dijkstra](https://cp-algorithms.com/graph/dijkstra_sparse.html)

- `priority_queue<int, vector<int>, greater<int>`
- Alternative: push negated distances
- With state ($k \le 20$ edge skips allowed)
- Multi-source Dijkstra
- Storing "parents" for obtaining a shortest path
- Number of shortest paths (Dijkstra DAG or DP)

# [Floyd-Warshall](https://cp-algorithms.com/graph/all-pair-shortest-path-floyd-warshall.html)

- Shortest path between $(i, j)$ using nodes $0 \dots k$ $(k = 0 \dots n-1)$
- The most straightforward 3 for loops
- Negative cycle detection: Some $i \to t \to j$ exists and $dist[t][t] < 0$

# [Bellman-Ford](https://cp-algorithms.com/graph/bellman_ford.html)

- Use all edges in $n-1$ iterations
- BFS-like approach actually
- Negative cycle detection: Something happens also during the $n$-th iteration
