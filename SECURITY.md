# Security Policy

This public portfolio contains professional writing, synthetic examples and small demonstration tools. It is not a production-data store or a backup location for other repositories.

## Never commit

- `.env` files
- API keys, access tokens, private keys or passwords
- Recovery or backup codes
- Production connection strings
- Customer, employee, user or child data
- Raw CRM, marketing automation, product or financial exports
- Employer-owned internal documents
- Private URLs containing access tokens
- Database backups or production configuration

## Data and demonstration rules

- Use synthetic data by default
- Keep synthetic identities obviously fictional
- Do not preserve real customer domains, account identifiers or personal records
- Do not use production screenshots
- Keep owned venture source code and production environments separate from this portfolio
- Label reconstructed, synthetic and conceptual work clearly

## Change checks

Before publishing material, check for:

1. Secrets and credentials
2. Personal or customer data
3. Employer-owned or confidential source material
4. Private links and identifiers
5. Unnecessary metadata in uploaded files
6. Broken public links

## If restricted information is exposed

Remove it from the current branch, determine whether it remains in Git history, rotate any affected credentials immediately, and rewrite history where necessary. Deleting a sensitive file in a later commit is not sufficient if the original remains retrievable.

Security concerns should be raised directly with the organisation owner rather than posted publicly with sensitive details.