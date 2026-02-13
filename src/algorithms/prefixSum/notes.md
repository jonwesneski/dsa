## Idea

Sum up all of the elements at the given point

```
Array:        [1,  2,  3,  4,  5]

Prefix Sum:   [0,  1,  3,  6, 10, 15]
               ^                   ^
               |                   |
            prefix[0]=0        prefix[5]=15

  Sum of subarray [i..j] = prefix[j+1] - prefix[i]

  Example: sum of [1,2,3] (index 0 to 2)
           = prefix[3] - prefix[0]
           = 6 - 0 = 6  ✓
```

### Prefix sum + hashmap

```
Array:  [1,  1,  1]     k = 2

Step-by-step:
                                       HashMap
  prefix_sum = 0                       { 0: 1 }
       │
       ▼
  ┌─────────────────────────────────────────────────┐
  │  i=0  val=1                                     │
  │  prefix_sum = 0 + 1 = 1                         │
  │  check: prefix_sum - k = 1 - 2 = -1             │
  │         -1 in map? NO  → count stays 0          │
  │  store: map[1] = 1                              │
  │                                map: {0:1, 1:1}  │
  ├─────────────────────────────────────────────────┤
  │  i=1  val=1                                     │
  │  prefix_sum = 1 + 1 = 2                         │
  │  check: prefix_sum - k = 2 - 2 = 0              │
  │         0 in map? YES (count=1) → count += 1    │
  │  store: map[2] = 1                              │
  │                          map: {0:1, 1:1, 2:1}   │
  │                                     count = 1   │
  ├─────────────────────────────────────────────────┤
  │  i=2  val=1                                     │
  │  prefix_sum = 2 + 1 = 3                         │
  │  check: prefix_sum - k = 3 - 2 = 1              │
  │         1 in map? YES (count=1) → count += 1    │
  │  store: map[3] = 1                              │
  │                    map: {0:1, 1:1, 2:1, 3:1}    │
  │                                     count = 2   │
  └─────────────────────────────────────────────────┘

  Answer: 2  →  subarrays [1,1] and [1,1]
                 ^^^^        ^^^^
                idx 0-1    idx 1-2

  KEY INSIGHT:
  ┌──────────────────────────────────────────────┐
  │  If prefix[j] - prefix[i] = k                │
  │  then subarray [i..j] sums to k              │
  │                                              │
  │  So at each j, we look up (prefix[j] - k)    │
  │  in the hashmap to find how many valid i's   │
  │  exist.                                      │
  └──────────────────────────────────────────────┘
```
