output "vm_public_ip" {
    value = aws_instance.demo1.public_ip
}

output "s3_domain" {
    value = aws_s3_bucket.my_bucket.bucket_domain_name
}