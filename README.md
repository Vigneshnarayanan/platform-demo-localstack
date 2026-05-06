Platform Demo — AWS-first (LocalStack) + Terraform + Automation

![CI](https://github.com/Vigneshnarayanan/platform-demo-localstack/actions/workflows/ci.yml/badge.svg?branch=main)

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
- .github/workflows/ci.yml: CI that runs terraform fmt/validate and integration smoke tests with LocalStack

What the smoke tests validate
- The tests exercise the S3 path: create a bucket (if missing), put an object, and read it back. This validates Terraform provisioning (S3 creation) and the app's ability to access S3 via the local LocalStack endpoint.

Accessing the application locally (browser)
- Run LocalStack: docker-compose up -d
- Apply Terraform (creates the bucket in LocalStack): make tf-init && make tf-apply
- Run the Flask app locally: make run-app
- Open your browser at: http://localhost:8080
  - GET / returns basic health and bucket name
  - GET /put writes a hello.txt object to the bucket
  - GET /get reads the hello.txt object and returns its body

Troubleshooting
- Docker daemon not running: ensure Docker Desktop is started. Error: "Cannot connect to the Docker daemon at unix:///.../docker.sock" → start Docker and retry.
- LocalStack license/pro version errors: some LocalStack images require a token. This repo pins a compatible older image (0.14.3). If CI fails due to image pull or license, update docker-compose.yml and the workflow to use a supported LocalStack image.
- Terraform errors (connection refused): ensure LocalStack is running and listening on port 4566. On macOS with Docker Desktop, LocalStack is reachable at http://localhost:4566.
- Python environment issues: use the included Makefile target which sets up a virtualenv before running the app/tests. If pip fails due to system-managed Python, create and activate a virtualenv: python3 -m venv venv && source venv/bin/activate && pip install -r app/requirements.txt
- Port conflicts: if port 4566 or 8080 is in use, stop the process using that port or change mappings in docker-compose.yml and app/app.py respectively.
- Terraform state: for local testing the state is local. For production switch to remote state (S3 backend + DynamoDB lock).

Pre-commit (Terraform fmt & validate)

- Install pre-commit (recommended):
  - brew install pre-commit  # macOS (or)
  - python3 -m pip install --user pre-commit
- Install the git hook in your repo:
  - pre-commit install
- What the hook runs: terraform fmt -check, terraform init -backend=false, terraform validate. This ensures Terraform is formatted and valid before commits.

If something breaks, collect logs:
- Docker containers: docker ps -a && docker logs <container>
- LocalStack: docker logs <localstack-container>
- Terraform: run terraform plan and terraform apply with -no-color to see clear errors

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
Interview talking points (use these in the README section during interviews)
- Ownership: explain tradeoffs of AWS-first design while enabling local dev with LocalStack
- Terraform: module boundaries, testing with LocalStack, idempotency and state handling recommendations
- Automation: CI runs LocalStack and smoke tests; Makefile automates common developer flows
- Leadership: mention mentoring approach (module templates, code reviews, policy-as-code), cross-team collaboration examples (shared modules, governance)

Notes
- This repo is intentionally runnable locally using LocalStack to avoid needing AWS credentials.
- For real deployments, switch provider endpoint configuration and use remote state (S3 + DynamoDB locks) and CI secrets for AWS credentials.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>