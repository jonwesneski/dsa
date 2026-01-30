# Frontend

## React

What triggers re-renders:

- Its props change
- Its own state changes
- Its parent re-renders AND it's not memoized AND (Its props change OR Its order in the tree changes)
