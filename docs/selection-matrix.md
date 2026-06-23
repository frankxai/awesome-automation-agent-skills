# Selection Matrix

Use the narrowest tool that can safely own the workflow.

| Workflow need | Best tool | Why |
| --- | --- | --- |
| GitHub, Vercel, Gmail, Calendar, Slack operations | Native connector | Structured permissions and review surface |
| Recurring judgment and reports | Codex automation | Reasoning plus scheduled follow-up |
| Search, recall, source gathering, context recovery | Hermes/retrieval agent | Context before execution |
| Agent-facing typed tool access | MCP | Explicit schemas and bounded calls |
| Fast SaaS glue | Make.com | Low-code speed and broad integrations |
| Technical branching and templates | n8n | Durable workflow logic and JSON review |
| Multi-agent cross-repo work | Swarm queue | Bounded worker lanes and synthesis owner |
| Deterministic repo checks | Script or GitHub Actions | Repeatable validation |

## Default Approval Gates

- Human approves sends, posts, spends, deletes, invites, production deploys, and permission changes.
- Dry-run first for migrations and workflow activation.
- Public examples use mock payloads.
- Fail closed on auth, transport, schema, or confidence errors.
