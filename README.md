# Cloud Cost Optimization Agent

[![CI](https://github.com/kogunlowo123/cloud-cost-optimization-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/cloud-cost-optimization-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

FinOps agent that continuously analyzes cloud spending, identifies waste (idle resources, oversized instances, unused storage), recommends rightsizing, manages reserved instance purchases, and enforces budget policies across multi-cloud environments.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `analyze_spending` | Analyze cloud spending by service, team, and environment |
| `detect_waste` | Identify idle, underutilized, or orphaned resources |
| `recommend_rightsizing` | Recommend instance size changes based on actual CPU/memory usage |
| `plan_reservations` | Calculate optimal reserved instance or savings plan purchases |
| `enforce_budget` | Check spending against budgets and trigger alerts |
| `generate_cost_report` | Generate cost allocation and showback report |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/costs/analyze` | Analyze cloud spending |
| `GET` | `/api/v1/costs/waste` | Detect wasted resources |
| `POST` | `/api/v1/costs/rightsize` | Get rightsizing recommendations |
| `POST` | `/api/v1/costs/reservations` | Plan reservation purchases |
| `GET` | `/api/v1/costs/budget/{budget_id}` | Check budget status |
| `POST` | `/api/v1/costs/report` | Generate cost report |

## Features

- Cost Analysis
- Waste Detection
- Rightsizing
- Reservation Planning
- Budget Enforcement

## Integrations

- Aws Cost Explorer
- Azure Cost Management
- Gcp Billing
- Cloudhealth
- Infracost

## Architecture

```
cloud-cost-optimization-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── cloud_cost_optimization_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**AWS Cost Explorer + Azure Cost Management + GCP Billing**

---

Built as part of the Enterprise AI Agent Platform.
