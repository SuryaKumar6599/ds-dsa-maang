# Two Heaps (Median Pattern)

```
Lower Half (Max Heap) | Upper Half (Min Heap)
        3             |        5
        2             |        8
```

## Why Two Heaps?
Median lives **between** two halves.

Rules:
1. Size difference ≤ 1
2. Max(lower) ≤ Min(upper)

Used in:
- Find Median from Data Stream