# Security Policy

## Reporting a vulnerability

**Do not open a public GitHub issue for security problems.**

Use [GitHub private vulnerability reporting](../../security/advisories/new)
for this repository, or contact the maintainer directly.

We commit to an initial response within **14 days** of a report.

## Scope

In scope: the quiz engine and dashboard (`91_Dashboard/`), shared toolbox
scripts (`90_Shared_Toolbox/tools/`), and the Android client builder.

Out of scope: personal study notes, textbooks, and documents (most live
outside git by design), plus third-party services.

## Secrets hygiene

- Real API keys, `.env` files, keystores (`*.keystore`, `*.jks`), and signed
  APKs must never be committed. They are gitignored and CI does not need them.
- Use `.env.example` as the template for required environment variables.
