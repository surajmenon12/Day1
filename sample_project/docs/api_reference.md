# API Reference

## Endpoints

### GET /
Returns the main dashboard HTML page.

### GET /api/stats
Returns current dashboard statistics.

**Response:**
```json
{
  "users": 1542,
  "active_sessions": 87,
  "revenue": 24350.75,
  "uptime": "99.97%"
}
```

### GET /api/users
Returns the list of registered users.

**Response:**
```json
[
  {"id": 1, "name": "Alice", "role": "admin"},
  {"id": 2, "name": "Bob", "role": "editor"}
]
```
