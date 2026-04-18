## Idea

In-order traversal visits nodes in **Left → Root → Right** order. For a Binary Search Tree (BST), this always produces nodes in ascending sorted order — which is its most powerful property. You can think of it as "reading" the tree from left to right.

There are two approaches: recursive (clean, simple) and iterative (uses an explicit stack, avoids call stack overflow on deep trees).

```
        4
       / \
      2   6
     / \ / \
    1  3 5  7

In-order visit order: 1 → 2 → 3 → 4 → 5 → 6 → 7
```

### Walkthrough

```
        4
       / \
      2   6
     / \ / \
    1  3 5  7

Step 1: go left from 4 → go left from 2 → reach 1 (no left child)
        visit 1
Step 2: back to 2 (no more left)
        visit 2
Step 3: go right from 2 → reach 3 (no left child)
        visit 3
Step 4: back to 4 (no more left subtree)
        visit 4
Step 5: go left from 6 → reach 5 (no left child)
        visit 5
Step 6: back to 6 (no more left)
        visit 6
Step 7: go right from 6 → reach 7 (no left child)
        visit 7

result = [1, 2, 3, 4, 5, 6, 7]
```

#### psuedo code (recursive)

```
function inOrder(node, result):
    if node is null:
        return

    inOrder(node.left, result)   // 1. go all the way left
    result.append(node.val)      // 2. visit current node
    inOrder(node.right, result)  // 3. go right
```

#### psuedo code (iterative)

```
stack = []
current = root
result = []

while current is not null OR stack is not empty:
    while current is not null:
        stack.push(current)      // save node, keep going left
        current = current.left

    current = stack.pop()        // leftmost unvisited node
    result.append(current.val)   // visit it
    current = current.right      // now explore its right subtree
```

## When you SHOULD use in-order traversal

✅ You need BST nodes in sorted order

✅ You're validating a BST (sorted output = valid BST)

✅ You need the kth smallest/largest element

✅ You're converting a BST to a sorted array or linked list

✅ You need in-order predecessor or successor of a node

✅ You're building a BST iterator

Interview keyword triggers:

- "sorted order"
- "kth smallest"
- "ascending"
- "BST validation"
- "inorder successor / predecessor"
- "convert BST to sorted list"

## When you should NOT use it

❌ You need level-by-level processing → use BFS / level-order

❌ You need to process the root before its children → use pre-order

❌ You need to process children before the root (e.g. delete a tree, evaluate expression trees) → use post-order

❌ The tree is not a BST and sorted order isn't meaningful

❌ You only need to find a node and the tree is a BST → use BST search instead (O(log n) vs O(n))

## Common in-order mistakes:

🚫 Forgetting the base case (null check) in recursive version

🚫 Confusing Left→Root→Right (in-order) with Root→Left→Right (pre-order)

🚫 In the iterative version: popping before finishing the left subtree

🚫 Assuming in-order produces sorted output on a non-BST tree

🚫 Stack overflow on a highly unbalanced tree using recursion — prefer iterative
