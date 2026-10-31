# API contract

## `GET /`

Returns HTTP 200 with the project identity and running status:

```json
{
  "project": "Decision Ledger",
  "status": "running"
}
```

## `GET /health`

Returns HTTP 200 when the application is healthy:

```json
{
  "status": "healthy"
}
```
