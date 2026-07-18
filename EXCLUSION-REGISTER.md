# Portfolio Exclusion Register

This register defines material that must never be uploaded, copied, lightly edited, screenshotted or reconstructed too closely in the portfolio.

## Core rule

> Rebuild the professional insight. Never migrate the source file.

A private GitHub repository is still not an appropriate archive for credentials, personal records, production data or employer-owned material.

## 1. Credentials and account-recovery material

**Classification: Never include**

Examples:

- Password exports
- API keys and tokens
- Backup or verification codes
- Recovery keys
- Private certificates
- Session cookies
- Environment files
- Authentication secrets
- Payment-platform backup codes
- Source-control deployment keys

Required action:

- Do not open for portfolio purposes
- Do not quote, summarise or copy
- Do not store encrypted versions in the portfolio
- Rotate any credential believed to have been exposed elsewhere

## 2. Identity and personal records

**Classification: Never include**

Examples:

- Passports and identity documents
- Companies House identity-verification documents
- Addresses, personal phone numbers and dates of birth
- Family information
- Medical or absence records
- Travel documents
- Personal photographs unrelated to professional evidence
- Tax records and government identifiers

Required action:

- Exclude completely
- Do not use screenshots with personal information in the background
- Do not preserve hidden metadata containing personal details

## 3. Employment and financial records

**Classification: Never include**

Examples:

- Payslips and tax forms
- Employment contracts
- Settlement agreements
- Compensation records
- Equity documents
- Bank or card records
- Expense reports
- Invoices and purchase orders
- Signed statements of work
- Recruitment records containing third-party personal data

Required action:

- Exclude completely
- Use only a high-level, independently written role chronology where needed

## 4. Legal and contractual material

**Classification: Never include unless independently rewritten and clearly safe**

Examples:

- NDAs
- Client contracts
- Vendor agreements
- Legal correspondence
- Signed terms
- Internal compliance investigations
- Procurement documentation

Safe treatment:

- A generic change-control or Definition-of-Done framework may be independently authored
- No clause, commercial term, party name, signature, date or negotiated position may be copied

## 5. Production and customer data

**Classification: Never include**

Examples:

- CRM exports
- Lead, contact, account or opportunity lists
- Campaign-member data
- Event attendee lists
- Customer usage or product telemetry
- Support records
- Revenue, forecast or pipeline exports
- Employee directories
- Email lists
- Raw analytics workbooks
- Database backups

Required action:

- Replace with synthetic datasets created from scratch
- Ensure synthetic values cannot be reverse-engineered to a real company or person
- Do not use disguised or partially masked production records

## 6. Employer and customer source artefacts

**Classification: Reconstruct; never copy**

Examples:

- Internal presentations
- Operating manuals
- Process documentation
- Architecture diagrams
- Business requirements
- QBR decks
- Dashboards
- System screenshots
- Internal wikis and Notion pages
- Field dictionaries
- Migration plans
- Transformation trackers
- Training decks

Safe treatment:

- Extract the transferable problem and reasoning privately
- Write a new company-neutral artefact from a blank page
- Change structure, examples, terminology and visual design
- Use synthetic data and generic systems
- Remove all distinctive internal identifiers

Redaction is not sufficient. The rule is **rebuild, not redact**.

## 7. Proprietary source code and technical configuration

**Classification: Never include without explicit ownership confirmation**

Examples:

- Code copied from an employer or client repository
- Production workflow definitions
- Infrastructure configuration
- Database schemas tied to a live product
- Deployment files
- Prompt or agent libraries built as employer property
- Private product implementation details

Safe treatment:

- Build a new demonstration from scratch
- Use a new architecture and synthetic inputs
- Document the transferable design principle, not the proprietary implementation

ThinkBud, NXClarity and any other separate source repositories remain outside the portfolio repository unless a specific, reviewed artefact is independently created for the portfolio.

## 8. Confidential metrics and commercial information

**Classification: Verify, generalise or exclude**

Examples:

- Exact pipeline and revenue values
- Conversion rates
- Budgets and costs
- Contract values
- Forecasts
- Customer counts
- Internal performance targets
- Tool pricing and negotiated discounts
- Headcount or restructuring plans

Permitted treatment:

- Use a verified public value where appropriate
- Express the result directionally
- Use a broad range where it cannot identify the company
- Describe the operational outcome without a number

A metric appearing in a CV, interview document or internal retrospective is not sufficient verification.

## 9. Employer-identifying detail in anonymised cases

**Classification: Remove or generalise**

Examples:

- Company and product names
- Logos and brand colours
- Internal programme names
- Employee and stakeholder names
- Exact dates combined with distinctive events
- Unique field or object names
- Private URLs
- Geographic and organisational detail that reveals the employer
- Tool combinations unique enough to identify the environment

Permitted treatment:

- Describe company stage, complexity and operating context in broad terms
- Use generic role labels
- Use neutral diagrams and terminology
- State that details have been combined or altered to preserve confidentiality

## 10. Third-party intellectual property

**Classification: Reference only**

Examples:

- Analyst training programmes
- Vendor templates
- Published assessment tools
- Purchased decks and icon libraries
- Conference materials
- Articles, books and external frameworks
- Copied spreadsheets and calculators

Required action:

- Do not upload the original
- Do not present the structure as Christopher’s work
- Cite the source where its concept materially informs an artefact
- Demonstrate original application, extension or critique

## 11. Interview and assessment work

**Classification: Independent strategic exercise**

These materials may demonstrate judgement, but they must not be represented as implemented transformation work.

Required label:

> Independently created strategic exercise based on information available during a recruitment or assessment process. It does not claim implementation or access to the company’s internal operating environment beyond the supplied brief.

Employer names should normally be removed from the portfolio version.

## 12. Owned ventures

**Classification: Venture-specific review**

Owned ventures may be named, but ownership does not mean every document is safe to share.

Still excluded:

- Credentials and admin records
- Private founder or investor communications
- Non-public financial information
- Customer or beta-user data
- Proprietary source code unless deliberately published
- Security architecture that increases operational risk
- Private legal or company-formation documents

Each venture case study needs its own confidentiality and publication review.

## 13. Images and screenshots

**Classification: High risk**

Before any image is used, confirm that it contains no:

- Names or profile photographs
- Email addresses
- Customer or employee data
- Browser tabs, bookmarks or notifications
- Internal URLs
- Account identifiers
- Company logos in an anonymised case
- System IDs or live record values
- Hidden EXIF or document metadata

Preferred treatment:

- Redraw the concept as a neutral vector diagram
- Recreate the interface with synthetic content
- Strip metadata before committing

## 14. File formats restricted by default

The following formats should not be committed without explicit review:

- `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.xlsm`, `.xlsb`
- `.pdf` derived from employer files
- `.zip`, `.rar` and other archives
- Database exports and backups
- Images copied from internal systems

Portfolio artefacts should default to:

- Markdown
- Clean SVG or PNG diagrams built for the portfolio
- CSV or JSON containing synthetic data
- Source code created specifically for the portfolio

## 15. Pre-commit exclusion test

Before committing any artefact, answer all of the following:

- Was this written or built from a blank page for the portfolio?
- Is every person, company and customer identifier removed where required?
- Is all example data synthetic?
- Are metrics verified, generalised or omitted?
- Is the structure original rather than a lightly edited source template?
- Are external ideas attributed?
- Are links public and safe?
- Has document and image metadata been checked?
- Has the Git history been checked for earlier unsafe versions?
- Could the artefact reasonably cause harm if access were accidentally widened?

Any uncertain answer blocks the commit until reviewed.

## Current Drive risk findings

The Drive contains examples of every high-risk category above, including credentials, recovery material, identity and employment records, contracts, raw operational data, internal system material and third-party intellectual property.

Their presence in Drive does not make them portfolio candidates. They are explicitly outside scope.

## Final rule

> Show judgement, design and impact. Do not expose the evidence source.