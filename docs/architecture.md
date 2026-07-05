# Cloud Cost Optimization Agent Architecture

FinOps agent that continuously analyzes cloud spending, identifies waste (idle resources, oversized instances, unused storage), recommends rightsizing, manages reserved instance purchases, and enforces budget policies across multi-cloud environments.

## Domain Tools

- **analyze_spending**: Analyze cloud spending by service, team, and environment
- **detect_waste**: Identify idle, underutilized, or orphaned resources
- **recommend_rightsizing**: Recommend instance size changes based on actual CPU/memory usage
- **plan_reservations**: Calculate optimal reserved instance or savings plan purchases
- **enforce_budget**: Check spending against budgets and trigger alerts
- **generate_cost_report**: Generate cost allocation and showback report