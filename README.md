# Structured Logging Module

A lightweight, structured logging library that provides consistent, context‑rich JSON logs across an application.  
Includes decorators for operations, stages, and functions, plus a unified `log_event()` API for emitting well‑formed events.

---

## Why This Project Exists

This module was built to demonstrate clean software design, test‑driven development, and production‑ready logging patterns.  
It reflects how I approach building maintainable, observable systems.

---

## Features

- Structured JSON logs for easy parsing and observability  
- Automatic context injection:
  - `context_id`
  - `service`, `operation`, `stage`
  - optional `user`, `request`, `payload`
- Decorators for instrumenting operations, stages, and utility functions  
- Simple, unified API (`log_event()`)  
- Minimal dependencies and easy to integrate into any Python project  

---

## Quick Example

```python
from structured_logging.decorators import instrument_operation

@instrument_operation("load_data", service="example_service")
def load_data():
    return {"records": 42}
```

Running this function produces structured JSON logs for both the start and end of the operation.

---

## Architecture Overview

### Instrumentation Layer
Decorators that wrap functions and automatically emit:
- start and end events for operations  
- stage‑level events  
- function‑level events  

### Core Logging API
`log_event()` enforces:
- consistent field names  
- JSON formatting  
- timestamp generation  
- optional payload support  

### Context Management
A lightweight context system that:
- generates a `context_id`  
- propagates it across nested calls  
- keeps logs correlated within a workflow  

### Structured Output
All logs follow a predictable schema, making them ideal for:
- log aggregation tools  
- distributed tracing  
- debugging complex workflows  

---

## Running Tests

From the project root:

```
pytest
```

All tests validate:
- decorator behavior  
- context propagation  
- JSON structure  
- event sequencing  

---

## Example Output

```json
{
  "timestamp": "2026-01-16T08:37:47.474528+00:00",
  "context_id": "dddf15dd-7ddf-4272-b259-d5b80b2279e6",
  "service": "example_service",
  "operation": "load_data",
  "stage": "start",
  "user": null,
  "request": null,
  "payload": {"records": 42}
}
```

---

## MIT License

Copyright (c) 2026 Drew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

(license text continues…)
