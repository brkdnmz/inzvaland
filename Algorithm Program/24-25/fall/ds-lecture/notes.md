Gotta note 'em all.

Open in this file in VS Code, then hit `Ctrl + Shift + V`, or select `Open Preview` after right-clicking the file from the top bar.

---

[CSES Problem Set](https://cses.fi/problemset/), always a good place to practice.

# Data Structures

### [`queue`](https://en.cppreference.com/w/cpp/container/queue)

- Used heavily in graph problems! (Gotta keep waitin' till November 2)
- Nothing so special about it, honestly.

### [`stack`](https://en.cppreference.com/w/cpp/container/stack)

- Recursion is a thing thanks to it.
- Can be used for constructing a [monotonic stack](https://liuzhenglaichn.gitbook.io/algorithm/monotonic-stack).
  - Finding nearest smaller/greater element for each element in $\mathcal{O}(n)$.

#### Problems

- https://algoleague.com/problem/balanced-brackets/detail
- https://algoleague.com/problem/izdimorsil-parantez/detail
- https://algoleague.com/problem/it-is-brute-force/detail
- https://leetcode.com/problems/largest-rectangle-in-histogram/description/
  - This has a fun alternative solution involving DSU.
- https://leetcode.com/problems/next-greater-element-ii/description/

### [`deque`](https://en.cppreference.com/w/cpp/container/deque)

- Can be used for buffed monotonic stack that can handle distance limit between elements: [monotonic deque/queue](https://liuzhenglaichn.gitbook.io/algorithm/mono-deque).

#### Problems

- https://leetcode.com/problems/sliding-window-maximum/description/
- A lovely problem that I haven't forgotten:

  - [Problem](https://github.com/ituacm/algoComp23/blob/main/Final%20Round/Happy%20Walk/README.md)
  - [Solution](https://github.com/ituacm/algoComp23/blob/main/Final%20Round/Happy%20Walk/solution.cpp)

  Sadly, I couldn't solve it during the contest...

### [`vector`](https://en.cppreference.com/w/cpp/container/vector)

- Auto-expanding/dynamic array.
- 2D Vector: `vector<vector<int>>`

### [`set`](https://en.cppreference.com/w/cpp/container/set)

#### Problems

- https://algoleague.com/problem/adnan-fight-club/detail
- https://algoleague.com/problem/soulmate/detail
- https://algoleague.com/problem/which-are-bidirectional-edges/detail

### [`priority_queue`](https://en.cppreference.com/w/cpp/container/priority_queue)

- Dijkstra, a friend of ours, loves it.
- Queue that is sorted in decreasing order. The greatest comes out first.

  - Need it in reverse order, e.g. for Dijkstra's Algorithm?

    ```cpp
    priority_queue<T, vector<T>, greater<T>>
    ```

    Another technique is: push the negated element so that the smallest becomes the greatest.

- Used heavily in graph problems! (Gotta keep waitin' till November 2)

#### Problems

- Such a beatiful one: https://algoleague.com/contest/algorithm-program-2024-2025-fall-qualification-round/problem/flood-disaster/detail

### [`map`](https://en.cppreference.com/w/cpp/container/map)

- Set with values attached to elements.
- Keys can be of almost any type.

#### Problems

- https://algoleague.com/problem/adnan-fight-club/detail
- https://algoleague.com/problem/soulmate/detail
- https://algoleague.com/problem/which-are-bidirectional-edges/detail

### [`multiset`](https://en.cppreference.com/w/cpp/container/multiset)

#### Problems

- https://algoleague.com/problem/cut-the-paper/detail
  - A beatiful example that covers most use cases.

### [`unordered_map`](https://en.cppreference.com/w/cpp/container/unordered_map) (Hash Map)

- There's also [`unordered_set`](https://en.cppreference.com/w/cpp/container/unordered_set), a.k.a. hash set.
- Limited default support for key types.
- 2D: `unordered_map<unordered_map<..., ...>, ...>`

#### Problems

- https://algoleague.com/problem/adnan-fight-club/detail
- https://algoleague.com/problem/soulmate/detail
- https://algoleague.com/problem/which-are-bidirectional-edges/detail

### [`bitset`](https://en.cppreference.com/w/cpp/utility/bitset)

- Performant bit manipulation on an array of bits.

### Bonus: [`ordered_set`](https://codeforces.com/blog/entry/11080)

- Black magic — at least to me.
- `set/map` that also supports finding order of element/getting element by order in $\mathcal{O}(\log n)$.
  - In fact, this is a BASED feature.

### Useful stuff

- [`sort`](https://en.cppreference.com/w/cpp/algorithm/sort)
- [Range-based for loop](https://en.cppreference.com/w/cpp/language/range-for)
- `using ll = long long;`
- [`string`](https://en.cppreference.com/w/cpp/string/basic_string)
- [`pair`](https://en.cppreference.com/w/cpp/utility/pair)
- [`array`](https://en.cppreference.com/w/cpp/container/array)

  STL containers can't have the vanilla array as their element type. This is where `array` shines:

  - `vector<array<int, 3>>`

- [`auto`](https://en.cppreference.com/w/cpp/language/auto)
- [Structured binding](https://en.cppreference.com/w/cpp/language/structured_binding)
  - Can't do without it once get used to it.
- [`next_permutation`](https://en.cppreference.com/w/cpp/algorithm/next_permutation)
- [`iota`](https://en.cppreference.com/w/cpp/algorithm/iota)
- [`accumulate`](https://en.cppreference.com/w/cpp/algorithm/accumulate)
- [`Lambda expressions`](https://en.cppreference.com/w/cpp/language/lambda)

  Inline functions:

  ```cpp
  int prefix_sum[n];
  // ...
  auto range_sum = [&](int l, int r) {
    return prefix_sum[r] - prefix_sum[l - 1];
  };

  cout << range_sum(3, 5) << "\n";
  ```

---

# Binary Search

> [!IMPORTANT]
> A holy source: [Codeforces EDU](https://codeforces.com/edu/course/2/lesson/6). Should first enroll in the "ITMO Academy: pilot course".

- [`lower_bound(x)`](https://en.cppreference.com/w/cpp/algorithm/lower_bound)
  - Smallest $i$ s.t. $a_i \ge x$.
  - The resulting index is the number of elements smaller than $x$. ($0$-indexed)
- [`upper_bound(x)`](https://en.cppreference.com/w/cpp/algorithm/upper_bound)
  - Smallest $i$ s.t. $a_i > x$.
  - The resulting index is the number of elements not exceeding $x$.
  - For integers, `lower_bound(x + 1) == upper_bound(x)`.
- `upper_bound(y) - lower_bound(x)` = The number of elements in the range `[x, y]`.
- There are several possible implementations. Everyone prefers one. I like the following one:

  Condition: `while(l < r)`

  Either:

  - `mid = (l + r) / 2`
  - `r = mid if bs_condition else l = mid + 1`,

  or:

  - `mid = (l + r + 1) / 2`
  - `l = mid if bs_condition else r = mid - 1`

  depending on the problem. The first configuration finds the leftmost position satisfying `bs_condition` while the second one finds the rightmost position.

- $\dfrac{l + r}{2}$ might overflow, you may use $l + \dfrac{r - l}{2}$ instead.
  - I use the former with casting to `long long` if needed. I don't ever use the latter, but it's [Errichto's suggestion](#useful-stuff-1).

### Problems

- https://algoleague.com/problem/lions/detail
- https://algoleague.com/problem/atacan-plays-hide-and-seek-2/detail
- https://algoleague.com/problem/the-king-of-the-inzva-l/detail
- https://algoleague.com/problem/bastan-toplamali-1-0li-arama/detail
- https://algoleague.com/problem/lazy-traveler/detail
- https://algoleague.com/problem/acuka-dreamin-easy/detail/

### Useful stuff

- [Errichto](https://www.youtube.com/watch?v=GU7DpgHINWQ) orz
- I liked [this one](https://liuzhenglaichn.gitbook.io/algorithm/binary-search) that I found at 7:21 AM today. Yes, I didn't sleep.
