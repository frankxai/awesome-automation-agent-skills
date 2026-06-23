# Awesome Automation Agent Skills

A curated index of agent-ready automation patterns, skills, and tool-selection
doctrine for Make.com, n8n, MCP, Codex automations, SaaS connectors, and
multi-agent queues.

This repo is public-safe by design. It links to reusable patterns and mock
templates, not live workflows or private operational data.

## Start Here

- [Selection Matrix](docs/selection-matrix.md)
- [Public Safety Rules](docs/public-safety.md)
- [Workflow Card Template](templates/workflow-card.md)

## Core Categories

### Tool Routers

- Automation tool router skills that decide when to use native connectors,
  Codex automations, MCP, Make.com, n8n, or a swarm queue.

### Make.com

- Scenario maps for low-code SaaS glue.
- On-demand scenario patterns for MCP exposure.
- Lead intake, purchase follow-up, and approval workflow sketches.

### n8n

- Workflow JSON review patterns.
- Self-hosted and private-data workflow guidance.
- Public template skeletons with credentials removed.

### MCP

- Typed tool boundary checklists.
- Scope and auth review patterns.
- Make MCP and n8n MCP exposure notes.

### Codex Automations

- Recurring repo health checks.
- Inbox and calendar briefings.
- Deployment and PR monitors.

### Swarm Queues

- Multi-agent handoff formats.
- Bounded worker-lane templates.
- Evaluation and synthesis gates.

## Public Boundary

Do publish:

- generic workflow maps
- mock payloads
- screenshots with no private data
- validation scripts
- installable public-safe skills

Do not publish:

- credentials
- live webhook URLs
- customer data
- inbox or calendar contents
- private memory
- revenue or partner pipeline details

## First Companion Repo

- `frankxai/starlight-automation-agent-skills` for installable Codex skills and
  public-safe Starlight automation doctrine.

