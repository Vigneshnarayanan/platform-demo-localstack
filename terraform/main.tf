module "s3" {
  source = "./modules/s3"
  bucket = var.bucket_name
}

output "bucket_name" {
  value = module.s3.bucket
}
