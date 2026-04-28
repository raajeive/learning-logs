# DSA Mastery Syllabus — Pattern-Based

> **Goal:** Recognize patterns instantly. Not just solve problems — know *why* and *which pattern* within 30 seconds of reading a problem.

**Stats:** 19 core patterns · ~400 problems · 4–5 months · 3 phases

---

## Phase 1 — Foundation
**Weeks 1–4 · Build the instincts**

### 1. Arrays & Two Pointers (~30 problems)
*Most frequent pattern at every company*
- Two pointer (opposite ends)
- Two pointer (same direction / slow-fast)
- Prefix sum & running totals
- Sliding window (fixed size)
- Kadane's — max subarray

### 2. Sliding Window (~20 problems)
*Substring / subarray with constraint*
- Variable window (shrink when invalid)
- Window with frequency map
- At-most-K distinct trick
- Minimum window substring pattern
- Deque-based window maximum

### 3. Hashing & Maps (~25 problems)
*O(1) lookup — unlocks everything*
- Frequency counting
- Two-sum family (complement map)
- Grouping / anagram buckets
- Subarray sum equals K (prefix + map)
- Count distinct in window

### 4. Linked Lists (~20 problems)
*Pointer manipulation fundamentals*
- Reverse in-place
- Floyd's cycle detection
- Merge two sorted lists
- Find middle (slow-fast pointer)
- K-group reversal

### 5. Stack & Monotonic Stack (~20 problems)
*Next greater / smaller in O(n)*
- Basic stack simulation
- Monotonic decreasing stack
- Monotonic increasing stack
- Next greater element family
- Largest rectangle in histogram

---

## Phase 2 — Core Patterns
**Weeks 5–12 · The interview meat (80% of questions live here)**

### 6. Trees — DFS & BFS (~35 problems)
*Binary trees, BST, N-ary*
- Preorder / inorder / postorder DFS
- Level-order BFS (queue)
- Path sum family
- LCA (lowest common ancestor)
- Serialize / deserialize
- BST validation & ops

### 7. Graphs — DFS, BFS, Union Find (~40 problems)
*Grid problems + component problems*
- DFS flood fill / island counting
- BFS shortest path (unweighted)
- Cycle detection (directed & undirected)
- Topological sort (Kahn's + DFS)
- Union-Find (DSU) with path compression
- Bipartite check

### 8. Binary Search (~25 problems)
*Search on answer, not just array*
- Classic sorted array search
- Search on answer space (min/max)
- Rotated array variants
- First/last occurrence
- 2D matrix binary search
- Capacity / threshold problems

### 9. Heap / Priority Queue (~25 problems)
*Top-K, median, scheduling*
- Top-K elements (min/max heap)
- K-th largest / smallest
- Merge K sorted lists
- Sliding window median (two heaps)
- Task scheduling
- Dijkstra's shortest path

### 10. Recursion & Backtracking (~30 problems)
*Exhaustive search with pruning*
- Subsets / power set
- Permutations (with/without duplicates)
- Combinations (choose K)
- N-Queens / Sudoku solver
- Word search on grid
- Palindrome partitioning

### 11. Dynamic Programming — 1D (~35 problems)
*Overlapping subproblems, memoization*
- Fibonacci / climbing stairs family
- House robber / max non-adjacent
- Coin change (min coins / count ways)
- Longest increasing subsequence
- Word break
- Decode ways

### 12. Dynamic Programming — 2D (~35 problems)
*Grid DP, string DP, knapsack*
- 0/1 Knapsack
- Unbounded knapsack
- Longest common subsequence
- Edit distance
- Unique paths on grid
- Palindromic substrings / subsequences
- Matrix chain / interval DP

---

## Phase 3 — Advanced & Differentiators
**Weeks 13–18 · What separates you from the pack**

### 13. Tries (~15 problems)
*String prefix problems*
- Build trie from words
- Search & startsWith
- Word dictionary with wildcards
- Replace words with prefix
- Maximum XOR pair (binary trie)

### 14. Intervals (~15 problems)
*Merge, overlap, scheduling*
- Sort + merge overlapping intervals
- Insert interval (binary search)
- Meeting rooms (min heap)
- Non-overlapping intervals (greedy)
- Sweep line for overlaps

### 15. Greedy (~20 problems)
*Locally optimal → globally optimal*
- Activity selection
- Jump game family
- Gas station circular tour
- Task assignment / interval scheduling
- Minimum platforms

### 16. Bit Manipulation (~15 problems)
*XOR tricks, bitmask DP*
- XOR find missing / duplicate
- Count set bits (Brian Kernighan)
- Power of 2 / check bit
- Bitmask subsets enumeration
- Single number family

### 17. Advanced Graphs (~20 problems)
*Weighted paths, advanced algos*
- Dijkstra's (single source shortest path)
- Bellman-Ford (negative weights)
- Floyd-Warshall (all pairs)
- Minimum spanning tree (Kruskal / Prim)
- Tarjan's SCC
- Articulation points & bridges

### 18. Segment Trees & Fenwick Tree (~15 problems)
*Range queries — Google loves these*
- Range sum query (mutable)
- Fenwick tree (BIT) construction
- Segment tree with lazy propagation
- Range minimum query
- Count inversions

### 19. Math & Number Theory (~15 problems)
*Sieve, GCD, modular math*
- Sieve of Eratosthenes
- GCD / LCM (Euclidean algorithm)
- Modular exponentiation
- Pascal's triangle / combinatorics
- Prime factorization

---

## Resources

| Resource | Use For |
|---|---|
| NeetCode 150 (leetcode.com) | Primary problem list — follow this order |
| NeetCode.io | Video explanation for every pattern |
| Grokking the Coding Interview (Educative) | Pattern drills with guided walkthroughs |
| Designing Data-Intensive Applications | System design foundation |
| Grokking System Design | System design interview prep |

---

## The Rules That Make You Dangerous

1. **Never just solve.** After every problem ask: *what pattern did I use, and what are 3 other problems that use this same pattern?*
2. **Phase 1 must be automatic.** These should take you under 15 minutes each before you move to Phase 2.
3. **DP gets 3–4 weeks alone.** It's the hardest — don't rush it.
4. **Pattern first, code second.** Spend the first 5 minutes of any problem identifying the pattern before writing a single line.
5. **Do hard problems after 100 mediums.** Not before — you'll just get demoralized.

---

## Timeline

| Phase | Duration | Focus |
|---|---|---|
| Phase 1 | Weeks 1–4 | Foundation — automatic recall |
| Phase 2 | Weeks 5–12 | Core patterns — deep fluency |
| Phase 3 | Weeks 13–18 | Advanced — interview differentiators |
| Mock interviews | Weeks 16–18 | Pramp, Interviewing.io, peer mocks |

---

*Total: ~400 problems across 19 patterns. Master the pattern, not the problem.*