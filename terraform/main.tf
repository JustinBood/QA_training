provider "aws" {
 access_key   = var.access_key
 secret_key   = var.secret_key
 region       = "eu-west-2"
}

resource "aws_vpc" "example_vpc" {
  cidr_block = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "example-vpc"
  }
}

resource "aws_subnet" "example_subnet" {
  vpc_id     = aws_vpc.example_vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "example-subnet"
  }
}

resource "aws_internet_gateway" "example_igw" {
  vpc_id = aws_vpc.example_vpc.id

  tags = {
    Name = "example-igw"
  }
}
 

resource "aws_route_table" "example_rt" {
  vpc_id = aws_vpc.example_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.example_igw.id
  }

  tags = {
    Name = "example-rt"
  }
}

resource "aws_route_table_association" "example_rta" {
  subnet_id      = aws_subnet.example_subnet.id
  route_table_id = aws_route_table.example_rt.id
}

resource "aws_security_group" "ssh_access_sg" {
  vpc_id = aws_vpc.example_vpc.id
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



resource "aws_instance" "demo1" {
 ami              = var.ami
 instance_type    = "t2.micro"
 key_name         = "mykey"
 subnet_id        = aws_subnet.example_subnet.id
 security_groups  = [aws_security_group.ssh_access_sg.id]

 tags = {
  Name = "demo1"
 }
}

resource "aws_s3_bucket" "my_bucket" {
  bucket         = var.bucket
  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}
