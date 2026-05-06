terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
  }
}

provider "aws" {
  access_key = "test"
  secret_key = "test"
  region     = var.region
  skip_credentials_validation = true
  skip_requesting_account_id = true
  endpoints {
    s3 = "http://localhost:4566"
  }
}
