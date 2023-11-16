provider "aws" {
 access_key   = var.access_key
 secret_key   = var.secret_key
 region       = "eu-west-2"
}

resource "aws_instance" "demo1" {
 ami            = var.ami
 instance_type  = "t2.micro"
 key_name       = "mykey"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = var.bucket
  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

resource "aws_security_group" "ssh_access" {
  name        = "ssh_access_sg"
  description = "Security group for SSH access"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "ssh_access_sg"
  }
}
