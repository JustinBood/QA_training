output "vm_public_ip" {
    value = aws_instance.demo1.id
}

output "s3_domain" {
    value = aws_s3_bucket.my_bucket.bucket_domain_name
}

output "vpc_id" {
  value = aws_vpc.example_vpc.id
}

output "subnet_id" {
  value = aws_subnet.example_subnet.id
}

output "sg_id" {
    value = aws_security_group.ssh_access_sg.id
}