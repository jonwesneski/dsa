## Structure

Order of operations: "FJ WGH SO L" →
From → Join → Where → Group → Having → Select → Order → Limit

```
SELECT                               // 6. Choose output columns & aggregates
    u.name,
    COUNT(o.id) AS total_orders,
    SUM(o.amount) AS total_spent
FROM users u                         // 1. Start with base table
INNER JOIN orders o                  // 2. Bring in other tables
    ON u.id = o.user_id
WHERE o.status = 'completed'         // 3. Filter
GROUP BY u.name                      // 4. Group remaining rows (GROUP BY is required when there are aggregates)
HAVING SUM(o.amount) > 500           // 5. Filter grouped results
ORDER BY total_spent DESC            // 7. Sort the results
LIMIT 5 OFFSET 0;                    // 8. Trim final result set
```

## JOINS

- INNER JOIN: returns rows that match the condition/clause
- LEFT OUTER JOIN: returns all rows and fills in NULL columns on the joined table where the condition/clause is not met/satisfied
- RIGHT OUTER JOIN: returns all rows and fills in NULL columns on the FROM table where the condition/clause is not met/satisfied

## INNER JOIN

```sql
SELECT
  users.name,
  users.email,
  orders.product,
  orders.amount
FROM users
INNER JOIN orders
  ON users.id = orders.user_id;
```

| name  | email                                     | product  | amount |
| ----- | ----------------------------------------- | -------- | ------ |
| Alice | [alice@email.com](mailto:alice@email.com) | Laptop   | 1200   |
| Alice | [alice@email.com](mailto:alice@email.com) | Mouse    | 25     |
| Bob   | [bob@email.com](mailto:bob@email.com)     | Keyboard | 75     |

## LEFT OUTER JOIN

```sql
SELECT
  users.name,
  users.email,
  orders.product,
  orders.amount
FROM users
LEFT OUTER JOIN orders
  ON users.id = orders.user_id;
```

| name    | email                                         | product  | amount |
| ------- | --------------------------------------------- | -------- | ------ |
| Alice   | [alice@email.com](mailto:alice@email.com)     | Laptop   | 1200   |
| Alice   | [alice@email.com](mailto:alice@email.com)     | Mouse    | 25     |
| Bob     | [bob@email.com](mailto:bob@email.com)         | Keyboard | 75     |
| Charlie | [charlie@email.com](mailto:charlie@email.com) | NULL     | NULL   |

## RIGHT OUTER JOIN

```sql
SELECT
  users.name,
  users.email,
  orders.product,
  orders.amount
FROM users
RIGHT OUTER JOIN orders
  ON users.id = orders.user_id;
```

| name  | email                                     | product  | amount |
| ----- | ----------------------------------------- | -------- | ------ |
| Alice | [alice@email.com](mailto:alice@email.com) | Laptop   | 1200   |
| Alice | [alice@email.com](mailto:alice@email.com) | Mouse    | 25     |
| Bob   | [bob@email.com](mailto:bob@email.com)     | Keyboard | 75     |
| NULL  | NULL                                      | Monitor  | 300    |

## GROUP BY

You mainly `GROUP BY` when you have 1 or more aggregates in your query to help deduplicate rows. (You can `GROUP BY` without an aggregate to help remove duplicate values for a column; or you can use the `DISTINCT` keyword in the `SELECT` statement)

```sql
SELECT
    user_id,
    SUM(amount) AS total_amount
FROM orders;
```

Here, `user_id` shows up more than once
| id | user_id | amount |
| --- | ------- | ------ |
| 1 | 1 | 100 |
| 2 | 1 | 50 |
| 3 | 2 | 200 |
| 4 | 2 | 75 |
| 5 | 3 | 40 |

```sql
SELECT
    user_id,
    SUM(amount) AS total_amount
FROM orders
GROUP BY user_id;
```

Here, `user_id` shows up once
| user_id | total_amount |
| ------: | -----------: |
| 1 | 150 |
| 2 | 275 |
| 3 | 40 |

## PARTITION BY (AKA Window Function)

When you want to keep the aggregate and the duplicated fields
Example data:
| id | user_id | amount | created_at |
| -- | ------- | ------ | ---------- |
| 1 | 1 | 100 | Jan 1 |
| 2 | 1 | 50 | Jan 5 |
| 3 | 2 | 200 | Jan 3 |
| 4 | 2 | 75 | Jan 8 |
| 5 | 3 | 40 | Jan 2 |

```sql
SELECT
  user_id,
  SUM(amount) AS total_spent
FROM orders
GROUP BY user_id;
```

| user_id | total_spent |
| ------- | ----------- |
| 1       | 150         |
| 2       | 275         |
| 3       | 40          |

```sql
SELECT
  id,
  user_id,
  amount,
  SUM(amount) OVER (PARTITION BY user_id) AS total_spent_by_user.  // Keep `user_id` and store their total amount in `total_spent_by_user`
FROM orders;
```

| id  | user_id | amount | total_spent_by_user |
| --- | ------- | ------ | ------------------- |
| 1   | 1       | 100    | 150                 |
| 2   | 1       | 50     | 150                 |
| 3   | 2       | 200    | 275                 |
| 4   | 2       | 75     | 275                 |
| 5   | 3       | 40     | 40                  |

## CASE WHEN

When you want to display a different value for something; like 0 instead of NULL

```sql
SELECT
    u.name,
    SUM(CASE WHEN o.status = 'completed' THEN o.amount ELSE 0 END) AS total_amount
FROM users u
LEFT OUTER JOIN orders o
    ON u.id = o.user_id
GROUP BY u.name;
```
