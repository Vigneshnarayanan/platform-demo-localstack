Platform Demo — AWS-first (LocalStack) + Terraform + Automation

This repository demonstrates platform ownership (AWS-first), Terraform modules, automation, and technical leadership — runnable locally without a cloud account using LocalStack.

Highlights
- AWS-first design: Terraform modules and app designed for AWS (S3, Lambda placeholders), but tested locally with LocalStack.
- Platform ownership: repo includes infra modules, CI workflow, automation scripts, and documentation to show platform decisions and tradeoffs.
- Terraform & Automation: modular Terraform (modules/s3), Makefile targets, and CI that exercises infrastructure and smoke tests.
- Technical leadership: README documents design choices, tradeoffs, and suggested interview talking points.

Quick start (Macbook, no cloud account)
1. Start LocalStack: docker-compose up -d
2. Create the S3 resource with Terraform (against LocalStack):
   make tf-init
   make tf-apply
3. Run app locally:
   make run-app
4. Run smoke tests (creates bucket, puts/gets object):
   make test

Files of interest
- terraform/: provider config and module examples (s3)
- app/: small Flask app demonstrating S3 usage against LocalStack
- docker-compose.yml: starts LocalStack for local testing
- .github/workflows/ci.yml: CI that starts LocalStack and runs smoke tests

Interview talking points (use these in the README section during interviews)
- Ownership: explain tradeoffs of AWS-first design while enabling local dev with LocalStack
- Terraform: module boundaries, testing with LocalStack, idempotency and state handling recommendations
- Automation: CI runs LocalStack and smoke tests; Makefile automates common developer flows
- Leadership: mention mentoring approach (module templates, code reviews, policy-as-code), cross-team collaboration examples (shared modules, governance)

Notes
- This repo is intentionally runnable locally using LocalStack to avoid needing AWS credentials.
- For real deployments, switch provider endpoint configuration and use remote state (S3 + DynamoDB locks) and CI secrets for AWS credentials.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>