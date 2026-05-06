resource "aws_s3_bucket" "this" {
  bucket = var.bucket
  force_destroy = true
  acl = "private"
}
