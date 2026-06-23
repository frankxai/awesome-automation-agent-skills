# Public Safety Rules

Automation examples are unusually easy to leak because useful workflow exports
often include IDs, webhook URLs, credential labels, or payload samples.

## Remove Before Publishing

- API keys, tokens, passwords, cookies, and OAuth refresh tokens.
- Live webhook URLs and private endpoint paths.
- Customer, inbox, calendar, CRM, and Slack data.
- Private memory and operator notes.
- Local machine paths and cache paths.
- Revenue, partner, or account details that are not meant for public release.

## Replace With

- mock domains
- fake payloads
- placeholder environment variables
- generic account names
- screenshots with sensitive areas removed
- tables that describe the shape rather than the live data

## Go/No-Go

Publish only when a reader can understand the pattern without being able to
call, infer, or enumerate the live system.

