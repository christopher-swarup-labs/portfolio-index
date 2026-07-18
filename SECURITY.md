# Security Policy

## Scope

This policy applies to every repository in `christopher-swarup-labs`.

The organisation is a private portfolio environment, not a production-data store and not a backup location for other repositories.

## Repository boundaries

Approved portfolio work must remain inside explicitly authorised repositories in `christopher-swarup-labs`.

Access to other repositories, including ThinkBud, does not permit copying their source, secrets, history or configuration into this organisation.

## Prohibited content

Never commit:

- `.env` files
- API keys, access tokens or private keys
- Passwords or authentication exports
- Recovery or backup codes
- Production connection strings
- Customer, employee or child data
- Raw CRM or marketing automation exports
- Internal company documents
- Private URLs containing access tokens
- Full database backups
- Unreviewed generated files or archives

## Data rules

- Use synthetic data by default.
- Keep synthetic data obviously fictional.
- Do not preserve real email domains, account names, identifiers or timestamps.
- Do not use production screenshots.
- Do not include hidden spreadsheet tabs, comments, speaker notes or document metadata.

## Access control

- Repositories remain private unless a separate approval is recorded.
- Invite collaborators only for a defined review period.
- Grant the lowest level of access required.
- Remove access when the review is complete.
- Do not share organisation-wide access when repository-level access is sufficient.

## Change control

For foundational changes, direct commits by the organisation owner are allowed.

As the portfolio grows:

1. Create a feature branch.
2. Open a pull request.
3. Run the review checklist.
4. Confirm no restricted information is included.
5. Merge only after the checks pass.

## Local checks before upload

Run at least:

- Secret scanning
- Personal-data search
- Employer and customer name search
- File metadata review
- Large-file review
- Link review

Recommended tools include `gitleaks` or `trufflehog` for secrets and a manual search for known names, domains and identifiers.

## Safe file formats

Prefer:

- Markdown
- Plain text
- Source-controlled diagrams
- Small synthetic JSON or CSV files
- Recreated images with verified metadata

Treat Office files, PDFs, exports and archives as high risk until reviewed.

## Incident response

If restricted information is committed:

1. Stop further work.
2. Remove the file from the current branch.
3. Determine whether it exists in Git history.
4. Rotate any exposed secret immediately.
5. Rewrite history when required.
6. Revoke external access until the issue is resolved.
7. Record what happened and the preventive action taken.

Deleting a file in a later commit is not sufficient when the original remains in Git history.

## Reporting

Security concerns should be raised directly with the organisation owner. Do not create a public issue containing sensitive details.