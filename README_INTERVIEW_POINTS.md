Suggested interview talking points — map these to your experience when presenting the project:

1) Ownership & Strategy (AWS-first)
- Explain why designing AWS-first (use of AWS APIs, terraform modules) helps product teams and platform consistency.
- Discuss how LocalStack enables developer productivity and reduces cloud cost/risk during iteration.

2) Terraform & Automation
- Module design: small, focused modules (s3, lambda, network) for reuse and collaboration.
- Testing strategy: use LocalStack in CI for smoke tests; integrate terraform fmt/validate and policy checks (OPA/terraform-compliance) in pipeline.

3) Platform Operations
- State management: recommend remote state (S3 + DynamoDB locks) for production; local state only for dev/testing.
- Observability: instrument provisioning with auditing and tag policies; include drift detection jobs.

4) Leadership & Cross-team
- Provide module templates, docs, and onboarding sessions; create a platform working group to define shared primitives and upgrade cadence.
- Mentoring: code reviews focusing on infra-as-code best practices, runbooks, and playbooks for incidents.

Use these points to narrate your role in designing the platform and mentoring teams.
