from collections import deque

N = 200005
g = [[] for _ in range(N)]
component_no = [0] * N
max_of_component = [0] * N
min_of_component = [10**9] * N
dist_to_max = [10**9] * N
dist_to_sigo = [10**9] * N
dist_to_ciko = [10**9] * N
pre_sum_costs = [0] * N
cur_component_no = 0


def dfs(n):
    global cur_component_no
    component_no[n] = cur_component_no
    min_of_component[cur_component_no] = min(min_of_component[cur_component_no], n)
    max_of_component[cur_component_no] = max(max_of_component[cur_component_no], n)
    for nxt in g[n]:
        if component_no[nxt]:
            continue
        dfs(nxt)


def calc_dist_within_component(source, dist):
    q = deque()
    q.append(source)
    dist[source] = 0
    while q:
        cur = q.popleft()
        for nxt in g[cur]:
            if dist[nxt] <= dist[cur] + 1:
                continue
            dist[nxt] = dist[cur] + 1
            q.append(nxt)


def preprocess_components():
    global cur_component_no
    n_components = cur_component_no
    for i in range(1, n_components + 1):
        calc_dist_within_component(max_of_component[i], dist_to_max)
    for i in range(1, n_components + 1):
        pre_sum_costs[i] = pre_sum_costs[i - 1] + min_of_component[i] + dist_to_max[min_of_component[i]]


def calc_dist(node, sigo_or_ciko, dist_to_sigo_or_ciko):
    o1 = component_no[node]
    o2 = component_no[sigo_or_ciko]
    if o1 == o2:
        return dist_to_sigo_or_ciko[node]

    dist = dist_to_max[node] + min_of_component[o2] + dist_to_sigo_or_ciko[min_of_component[o2]]
    if o1 < o2:
        dist += pre_sum_costs[o1 - 1] + pre_sum_costs[o2 - 1] - pre_sum_costs[o1]
    else:
        dist += pre_sum_costs[o2 - 1]

    return dist


def main():
    global cur_component_no
    n, m, sigo, ciko = map(int, input().split())

    assert 1 <= n <= 200000
    assert 0 <= m <= 200000
    assert 1 <= sigo <= n
    assert 1 <= ciko <= n

    for _ in range(m):
        a, b = map(int, input().split())
        assert 1 <= a <= n
        assert 1 <= b <= n
        g[a].append(b)
        g[b].append(a)

    for i in range(1, n + 1):
        if component_no[i]:
            continue
        cur_component_no += 1
        dfs(i)

    calc_dist_within_component(sigo, dist_to_sigo)
    calc_dist_within_component(ciko, dist_to_ciko)

    preprocess_components()

    q = int(input())
    assert 1 <= q <= 200000
    for _ in range(q):
        rumeysa, e = map(int, input().split())
        assert 1 <= rumeysa <= n
        assert 1 <= e <= n
        rumeysa_dist = calc_dist(rumeysa, sigo, dist_to_sigo) + calc_dist(sigo, ciko, dist_to_ciko)
        elif_dist = calc_dist(e, ciko, dist_to_ciko)
        print(rumeysa_dist, elif_dist)


if __name__ == "__main__":
    main()
