# 04 — REST API Health Monitor

An async tool that concurrently pings multiple API endpoints, measures their response times, and displays a real-time health dashboard in the terminal. Built with `asyncio` for concurrent execution and `rich` for formatted output.

## Features

- Checks multiple endpoints simultaneously using `asyncio`
- Measures response time in milliseconds per endpoint
- Displays a color-coded terminal table (green = UP, red = DOWN)
- Configurable endpoints via JSON file — no code changes needed
- Handles timeouts and connection errors gracefully

## Usage

```bash
# Install dependencies
pip install httpx rich

# Run the monitor
python monitor.py endpoints.json
```

## Sample Output

```
                 API Health Monitor
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Name            ┃ URL             ┃ Status ┃ Response Time ┃ Result ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ GitHub API      │ https://api...  │ 200    │ 351.82ms      │ ✓ UP   │
│ HTTPBin         │ https://http... │ 200    │ 492.29ms      │ ✓ UP   │
│ JSONPlaceholder │ https://json... │ 200    │ 315.37ms      │ ✓ UP   │
└─────────────────┴─────────────────┴────────┴───────────────┴────────┘
```

## Endpoints Config (`endpoints.json`)

```json
[
    {
        "name": "GitHub API",
        "url": "https://api.github.com",
        "timeout": 5
    }
]
```

Add as many endpoints as needed — they all run simultaneously.

## Concepts Covered

| Concept | Description |
|---------|-------------|
| `asyncio` | Concurrent execution — all checks run simultaneously |
| `async/await` | Non-blocking I/O pattern |
| `asyncio.gather()` | Running multiple coroutines at once |
| `httpx.AsyncClient` | Async HTTP client with shared connection pool |
| `rich` | Beautiful formatted terminal output |
| HTTP status codes | 200, 4xx, 5xx and what they mean |
| JSON config files | Separating configuration from code |
| Error handling | Graceful degradation on network failures |
