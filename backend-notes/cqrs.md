# Command Query Responsibility Separation

Having 1 DB model/schema writing and 1 model/materialized-view/schema for reading.

Pros:

- Optimize write models
- Optimize read models

Cons:

- Complex to setup
- Eventual Consistency
- Data sychronization can be difficult on large or complicated transformations or big data sets

When to use:

- Handling complex read queries
- Scaling reads and writes independently
- Event driven systems
- When write models are different than read models

## Flow

1. API to mutate state comes in and creates a Command to update write model db (The command doesn't return db data)
2. The Command handler sends an event that Query is listening to
3. Query handler then takes that data and updates its model/materialized-view/schema
4. What gets returned to the user is minimal it can be one of:
   - Status: 202 Accepted, Data: {id: "u123"}
   - Status: 201 Created, Data: {id: "u123", email: "a@example.com", createdAt: "..." } // keep minimal
5. User then makes a GET API call than queries the read model for the remainder of the data

```
// API handler
app.post('/users', async (req, res) => {
  const result = await commandBus.execute('createUser', req.body);
  if (result.success) {
    res.status(202).json({ id: result.id }); // Client queries next
  }
});

// Command Handler
async createUserCommand({ email }) {
  const id = generateId();
  const user = { id, email, createdAt: new Date() };

  await writeRepo.insert(user);

  events.emit('UserCreated', user);

  return { success: true, id };
}


// Read model projection / query handler
// Listens to events, updates materialized view
class UserReadModel {
  constructor(private db: Database) {}

  // This gets registered as an event listener
  async handleUserCreated(event: UserCreatedEvent) {
    const { id, email, createdAt } = event;

    // Simple UPSERT into denormalized read table
    await this.db.query(`
      INSERT INTO user_profiles (id, email, fullName, orderCount, lifetimeValue, createdAt)
      VALUES (?, ?, ?, 0, 0.00, ?)
      ON DUPLICATE KEY UPDATE
        email = VALUES(email),
        createdAt = VALUES(createdAt)
    `, [id, email, '', createdAt]);
  }

  ...
}

type AppEvents = {
  UserCreated: { id: string; email: string; createdAt: Date };
  UserEmailUpdated: { id: string; email: string };
  OrderCompleted: { userId: string; total: number };
};
// In app startup / bootstrap
const events = new EventEmitter<AppEvents>();
const readModel = new UserReadModel(db);

// Register listeners (projections)
events.on('UserCreated', (event) => readModel.handleUserCreated(event));
...

```

### Example Command - Creating a User (Write Path with Read Model Sync)

```

┌─────────┐
│ Client  │
└────┬────┘
     │
     │ POST /users
     │ { name: "Alice", email: "alice@example.com" }
     ▼
┌─────────────────────┐
│  Command Handler    │
│  (CreateUserCmd)    │
└──────────┬──────────┘
           │
           │ 1. Validate & Process
           ▼
    ┌──────────────────────┐
    │   WRITE MODEL        │
    │  ┌────────────────┐  │
    │  │  Users Table   │  │
    │  │ ┌────────────┐ │  │
    │  │ │ id: 123    │ │  │
    │  │ │ name: Alice│ │  │
    │  │ │ email: ... │ │  │
    │  │ │ version: 1 │ │  │
    │  │ └────────────┘ │  │
    │  └────────────────┘  │
    └──────────┬───────────┘
               │
               │ 2. Emit Event
               ▼
        ┌──────────────┐
        │ Event Bus    │
        │ UserCreated  │
        └──────┬───────┘
               │
               │ 3. Event Handler Syncs
               ▼
    ┌──────────────────────┐
    │   READ MODEL         │
    │  ┌────────────────┐  │
    │  │ UserView Cache │  │
    │  │ ┌────────────┐ │  │
    │  │ │ id: 123    │ │  │
    │  │ │ name: Alice│ │  │
    │  │ │ email: ... │ │  │
    │  │ │ created_at │ │  │
    │  │ └────────────┘ │  │
    │  └────────────────┘  │
    └──────────────────────┘
               │
               │ 4. Return Success
               ▼
        ┌─────────────┐
        │   Client    │
        │ Response:   │
        │ { id: 123,  │
        │   status:   │
        │   "created" │
        │ }           │
        └─────────────┘
```

### Example Query - Getting a User (Read Path)

```

┌─────────┐
│ Client  │
└────┬────┘
     │
     │ GET /users/123
     │
     ▼
┌─────────────────────┐
│   Query Handler     │
│  (GetUserQuery)     │
└──────────┬──────────┘
           │
           │ 1. Route to Read Model
           │
           │              ┌──────────────────────┐
           │              │   WRITE MODEL        │
           │              │  ┌────────────────┐  │
           │              │  │  Users Table   │  │
           │              │  │ (not accessed) │  │
           │              │  └────────────────┘  │
           │              └──────────────────────┘
           │                        ↑
           │                     (not used)
           │
           ▼
    ┌──────────────────────┐
    │   READ MODEL         │
    │  ┌────────────────┐  │
    │  │ UserView Cache │  │
    │  │ ┌────────────┐ │  │
    │  │ │ id: 123    │ │◄─┼── 2. Fast Query
    │  │ │ name: Alice│ │  │
    │  │ │ email: ... │ │  │
    │  │ │ created_at │ │  │
    │  │ └────────────┘ │  │
    │  └────────────────┘  │
    └──────────┬───────────┘
               │
               │ 3. Return Data
               ▼
        ┌─────────────────┐
        │     Client      │
        │   Response:     │
        │ {               │
        │   id: 123,      │
        │   name: "Alice",│
        │   email: "...", │
        │   created_at: "…"│
        │ }               │
        └─────────────────┘
```
