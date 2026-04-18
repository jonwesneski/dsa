## Idea

Level-order traversal visits nodes **level by level**, left to right, starting from the root. It uses a **queue** (FIFO) to process nodes in the order they were discovered. This is also called **BFS (Breadth-First Search)** on a tree.

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7

Level-order visit order: 1 → 2 → 3 → 4 → 5 → 6 → 7
```

### Walkthrough

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7

Start: queue = [1]

Step 1: dequeue 1, enqueue its children → queue = [2, 3]
        level result = [1]

Step 2: dequeue 2, enqueue its children → queue = [3, 4, 5]
        dequeue 3, enqueue its children → queue = [4, 5, 6, 7]
        level result = [2, 3]

Step 3: dequeue 4, 5, 6, 7 (no children) → queue = []
        level result = [4, 5, 6, 7]

final result = [[1], [2, 3], [4, 5, 6, 7]]
```

#### pseudo code (iterative — standard BFS)

```
queue = deque([root])
result = []

while queue is not empty:
    node = queue.popleft()         // process node
    result.append(node.val)
    if node.left:  queue.append(node.left)
    if node.right: queue.append(node.right)
```

#### pseudo code (level-grouped — most common interview variant)

```
queue = deque([root])
result = []

while queue is not empty:
    level_size = len(queue)        // snapshot: how many nodes are on this level
    level = []

    for _ in range(level_size):
        node = queue.popleft()
        level.append(node.val)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)

    result.append(level)
```

The `level_size` snapshot is the key trick — it freezes how many nodes belong to the current level before you start enqueuing the next level's children.

#### pseudo code (recursive — less common but valid)

```
function bfs(queue, result):
    if queue is empty:
        return

    next_queue = []
    level = []

    for node in queue:
        level.append(node.val)
        if node.left:  next_queue.append(node.left)
        if node.right: next_queue.append(node.right)

    result.append(level)
    bfs(next_queue, result)
```

## When you SHOULD use level-order traversal

✅ You need nodes processed level by level (e.g. level averages, level max)

✅ You need the rightmost (or leftmost) node at each level → right/left side view

✅ You need to find the minimum depth of a tree (BFS finds it faster than DFS)

✅ You need to connect nodes at the same level (next right pointer problems)

✅ You need to serialize/deserialize a tree

✅ You need the zigzag level order (alternate direction each level)

Interview keyword triggers:

- "level by level"
- "row by row"
- "right side view" / "left side view"
- "level averages" / "level max"
- "minimum depth"
- "zigzag"
- "connect next pointers"
- "cousins" (same level, different parents)

## When you should NOT use it

❌ You need nodes in sorted order on a BST → use in-order

❌ You need to process children before parents (e.g. delete tree, evaluate expressions) → use post-order

❌ You need to clone/serialize using pre-order logic → use pre-order

❌ The problem is about paths from root to leaf → use DFS

❌ Memory is a concern on a very wide tree — BFS holds an entire level in the queue at once, which can be O(n) space at the widest level

## Common level-order mistakes

🚫 Forgetting to snapshot `level_size = len(queue)` before the inner loop — without it you'll mix nodes from different levels

🚫 Using a stack instead of a queue — a stack gives DFS, not BFS

🚫 Not handling the `root is None` edge case before adding to the queue

🚫 Appending children before dequeueing the parent — enqueue children only after processing the parent

🚫 Off-by-one: using `while queue` with no level grouping when the problem needs per-level results
